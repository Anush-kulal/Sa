# Program 2: Data Transformation - String manipulation & regex
# Source: Statistics Lab Program PDF
import pandas as pd
import re

def run():
    dataset = pd.DataFrame({'Name': ['John Smith', 'Mary Johnson', 'David Lee'],
                            'Address': ['123 Main St', '456 Elm St', '789 Oak St']})
    print("Original:\n", dataset, "\n")

    # lowercase then uppercase then strip
    dataset['Name'] = dataset['Name'].str.lower().str.upper().str.strip()
    dataset['Address'] = dataset['Address'].str.lower().str.upper().str.strip()
    print("After case conversion and strip:\n", dataset, "\n")

    # Replace strings
    dataset['Name'] = dataset['Name'].str.replace('JOHN', 'JONATHAN', regex=False)
    dataset['Address'] = dataset['Address'].str.replace('ST', 'STREET', regex=False)
    print("After replace:\n", dataset, "\n")

    # Regex example for emails and phone numbers
    dataset2 = pd.DataFrame({'Email': ['john@example.com', 'mary@example.org', 'david@example.net'],
                             'Phone': ['123-456-7890', '098-765-4321', '555-123-4567']})
    dataset2['Domain'] = dataset2['Email'].str.extract(r'@(.*)', expand=False)
    dataset2['Valid Phone'] = dataset2['Phone'].str.contains(r'^\d{3}-\d{3}-\d{4}$')
    dataset2[['AreaCode','Prefix','LineNumber']] = dataset2['Phone'].str.extract(r'(\\d{3})-(\\d{3})-(\\d{4})')
    print("Regex extraction:\n", dataset2)

if __name__ == '__main__':
    run()
