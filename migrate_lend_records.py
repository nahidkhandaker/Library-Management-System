import json

def migrate_lend_records():
    try:
        with open('lend_records.json', 'r') as fp:
            records = json.load(fp)

        # fix any records with the typo
        for record in records:
            if 'borrower_name' in record:
                record['borrower_name'] = record.pop('borrower_name')

        # save the corrected records
        with open('lend_records.json', 'w') as fp:
            json.dump(records, fp, indent=4)
        
        print("Successfully migrated lending records.")
    except FileNotFoundError:
        print("No lending records found.")
    except Exception as e:
        print(f"Error migrating records: {e}")