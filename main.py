import csv
from csv import reader
from csv import writer

resultdico = {}

print('----- Reservation -----')

reservationsfile = 'C:/Users/steph/OneDrive/Documents/bca/2021/agility/SmarterAgility_reservations_1807.csv'
vendredifile = 'C:/Users/steph/OneDrive/Documents/bca/2021/agility/SmarterAgility__BAF2019__1806.csv'
samedifile = 'C:/Users/steph/OneDrive/Documents/bca/2021/agility/SmarterAgility__BAF2019__1807.csv'
dimanchefile = 'C:/Users/steph/OneDrive/Documents/bca/2021/agility/SmarterAgility__BAF2019__1808.csv'
resultfile = 'C:/Users/steph/OneDrive/Documents/bca/2021/agility/Reservations_generated.csv'

# open file in read mode
reservations = open(reservationsfile, 'r')
# pass the file object to reader() to get the reader object
csv_reader = reader(reservations, delimiter=';')
# Iterate over each row in the csv using reader object
for row in csv_reader:
    email = row[7]
    if email in resultdico:
        result = resultdico[email]
    else:
        result = [None] * 12
        result[3] = email
        resultdico[email] = result

    if row[1].startswith('Camping'):
        if result[7] is None:
            result[7] = 0
        result[7] = result[7] + int(row[8])

    if row[1].startswith('Petit') and row[2].startswith('sam'):
        if result[10] is None:
            result[10] = 0
        result[10] = result[10] + int(row[8])

    if row[1].startswith('Petit') and row[2].startswith('dim'):
        if result[11] is None:
            result[11] = 0
        result[11] = result[11] + int(row[8])

    if row[1].find('Barbecue') > -1:
        if result[8] is None:
            result[8] = 0
        result[8] = result[8] + int(row[8])

print('----- Vendredi -----')

# open file in read mode
vendredi = open(vendredifile, 'r')
# pass the file object to reader() to get the reader object
csv_reader = reader(vendredi, delimiter=';')
# Iterate over each row in the csv using reader object
for row in csv_reader:
    email = row[25]
    if email in resultdico:
        result = resultdico[email]
    else:
        result = [None] * 12
        result[3] = email
        resultdico[email] = result

    if result[0] is None:
        result[0] = row[6]
        result[1] = row[5]
        result[2] = row[23]

    if result[4] is None:
        result[4] = 0
    result[4] = result[4] + 1

print('----- Samedi -----')

# open file in read mode
samedi = open(samedifile, 'r')
# pass the file object to reader() to get the reader object
csv_reader = reader(samedi, delimiter=';')
# Iterate over each row in the csv using reader object
for row in csv_reader:
    email = row[25]
    if email in resultdico:
        result = resultdico[email]
    else:
        result = [None] * 12
        result[3] = email
        resultdico[email] = result

    if result[0] is None:
        result[0] = row[6]
        result[1] = row[5]
        result[2] = row[23]

    if result[5] is None:
        result[5] = 0
    result[5] = result[5] + 1

print('----- Dimanche -----')

# open file in read mode
dimanche = open(dimanchefile, 'r')
# pass the file object to reader() to get the reader object
csv_reader = reader(dimanche, delimiter=';')
# Iterate over each row in the csv using reader object
for row in csv_reader:
    email = row[25]
    if email in resultdico:
        result = resultdico[email]
    else:
        result = [None] * 12
        result[3] = email
        resultdico[email] = result

    if result[0] is None:
        result[0] = row[6]
        result[1] = row[5]
        result[2] = row[23]

    if result[6] is None:
        result[6] = 0
    result[6] = result[6] + 1

    print(result)

with open(resultfile, 'w', newline='') as csvfile:
    csvwriter = writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in resultdico.values():
        csvwriter.writerow(row)