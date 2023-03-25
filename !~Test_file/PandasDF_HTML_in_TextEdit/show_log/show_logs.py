from glob import glob
import argparse

import json

import pandas as pd



def parse_args():
    
    parser = argparse.ArgumentParser(description="zebrafish project: crop images into small pieces")
    parser.add_argument(
        "--read_log_dir",
        type=str,
        default=".\log\copy_rename",
        help="The path of logs to read.",
    )
    parser.add_argument(
        "--log_index",
        type=int,
        required=True,
        help="The number of file, e.g. '-1' will read the last file in the directory.",
    )
    
    args = parser.parse_args()
    return args



if __name__ == "__main__":

    args = parse_args()

    json_logs = glob(f"{args.read_log_dir}\*.json")
    with open(json_logs[args.log_index], "r") as f:
        info = json.load(f)
    df = pd.DataFrame(info)

    print("\n", f"{json_logs[args.log_index]}\n", "="*100, "\n")
    print(df)
    

    print("="*70, "\n", "process all complete !")