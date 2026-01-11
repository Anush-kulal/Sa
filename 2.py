import pandas as pd
import re

dataset = pd.DataFrame({
    'Name': ['John Smith', 'Mary Johnson', 'David Lee'],
    'Address': ['123 Main St', '456 Elm St', '789 Oak St']
})
print(dataset)
dataset['Name'] = dataset['Name'].str.lower()
dataset['Address'] = dataset['Address'].str.lower()
print(dataset['Name'],'  ',dataset['Address'])

dataset['Name'] = dataset['Name'].str.upper()
dataset['Address'] = dataset['Address'].str.upper()
print(dataset['Name'],'  ',dataset['Address'])


dataset['Name'] = dataset['Name'].str.strip()
dataset['Address'] = dataset['Address'].str.strip()
print(dataset['Name'],'  ',dataset['Address'])

dataset['Name'] = dataset['Name'].str.replace('JOHN', 'JONATHAN')
dataset['Address'] = dataset['Address'].str.replace('ST', 'STREET')
print(dataset['Name'],'  ',dataset['Address'])



dataset = pd.DataFrame({
    'Email': ['john@example.com', 'mary@example.org', 'david@example.net'],
    'Phone': ['123-456-7890', '098-765-4321', '555-123-4567']
})

dataset['Domain'] = dataset['Email'].str.extract(r'@(.*)', expand=False)

dataset['Valid Phone'] = dataset['Phone'].str.contains(r'^\d{3}-\d{3}-\d{4}$', regex=True)

dataset[['AreaCode','Prefix','LineNumber']] = dataset['Phone'].str.extract(r'(\d{3})-(\d{3})-(\d{4})')

print(dataset)

