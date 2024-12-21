import json

def save_lend_records(lend_records):
    with open('lend_records.json', 'w') as fp:
        json.dump(lend_records, fp, indent=4)