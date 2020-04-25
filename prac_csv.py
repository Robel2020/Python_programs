import csv

with open("csv_file.csv", 'r') as csvfile:
    #field_names = ['First_name', 'LastName', 'Street_name', 'City', 'State', 'Zip_Code']
    csv_read = csv.DictReader(csvfile)
    for line in csv_read:
        print(line['First_name'])


    # for line in csv_read:
    #     csv_writer.writerow(line)
    # for line in csv_read:
    #     print(line[3])
