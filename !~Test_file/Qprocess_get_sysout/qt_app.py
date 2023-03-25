from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget, QProgressBar)
from PyQt5.QtCore import QProcess
import sys
import re

"""
reference: https://www.pythonguis.com/tutorials/qprocess-external-programs/
"""

# A regular expression, to extract the % complete.
progress_re = re.compile("Total complete: (\d+)%")


def simple_percent_parser(output):
    """
    Matches lines using the progress_re regex,
    returning a single integer for the % progress.
    """
    
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.p = None # Default empty value.

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 100)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.progressBar)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)


    def message(self, s):
        self.text.appendPlainText(s) # auto new_line


    def start_process(self):
        # We'll run our process here.
        if self.p is None:
            self.message("Executin process.")
            self.p = QProcess()
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)
            self.p.start("python", ["dummy_script.py"])
    
    
    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf-8")
        self.message(stdout)
        
        
    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf-8")
        # Extract progress if it is in the data.
        progress_value = simple_percent_parser(stderr)
        if progress_value:
            self.progressBar.setValue(progress_value)
        self.message(stderr)
        
        
    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        self.message(f"State Changed: {state_name}")
            
            
    def process_finished(self):
        self.message("Process Finished")
        self.p = None


app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec_()