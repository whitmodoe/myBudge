import datetime
from calendar import monthcalendar
import json

# Define functions
#Gets keys and values for monthly bills dictionary
def get_values():
    keys = []
    values = []
    
    keys.append('name')
    values.append(input('Enter bill name: '))
    keys.append('due date')
    values.append(input('Enter due date DD/MM: '))
    keys.append('amount due')
    values.append(input('Enter amount due to 2 decimal places: '))
    
    return keys, values

# Create list to populate
nov2024_bills = []

# Get values for monthly bills
num_bills = int(input('Enter number of bills: '))

for i in range(0, num_bills):
    keys, values = get_values()
    bill_name = 'bill_name' + str(i + 1)
    bill_name = {}
    
    # Populate dictionary with keys & values
    for j in range(0,3): 
        bill_name[keys[j].strip()] = values[j].strip()

    nov2024_bills.append(bill_name)


# Create file to write bills values to 
bill_file = 'nov2024_bills.txt'
# date = datetime.datetime.now()
# month = date.strftime('%b')
# year = date.year
# file_name = month + '_' + str(year) + '.txt'
#^^^^^^^HARDCODING FILE RN--AUTOMATE IN LATER VERSION^^^^^^^^^
for bill in nov2024_bills:
    #format bill dictionary to json string
    str_bill = json.dumps(bill)
    with open(bill_file, 'a') as f:
        f.write(str_bill)

with open(bill_file, 'r') as f:
    content = f.read()

print(content)







