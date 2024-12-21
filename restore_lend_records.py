import json
import os

def restore_lend_records(lend_records):
    try:
        # check if file exists and is not empty
        if os.path.exists('lend_records.json') and os.path.getsize('lend_records.json') > 0:
            with open("lend_records.json", "r") as fp:
                lend_records = json.load(fp)
        else:
            # if file doesn't exist or is empty, create it with an empty list
            with open("lend_records.json", "w") as fp:
                json.dump([], fp)
            lend_records = []
    except (FileNotFoundError, json.JSONDecodeError):
        # handle any other potential errors
        lend_records = []
        with open("lend_records.json", "w") as fp:
            json.dump([], fp)

    return lend_records