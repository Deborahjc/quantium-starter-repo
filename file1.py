import csv

file_list = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
for file in file_list:
    with open(file, mode='r') as csv_file0:
        csv_reader = csv.DictReader(csv_file0, delimiter=',')
        data_list = list(csv_reader)
        updated_data = [row for row in data_list if row['product'] == 'pink morsel']
        for row in updated_data:
            row.update({'sales': float(row['price'].replace('$', '')) * int(row['quantity'])})
            del row['price']
            del row['quantity']
            del row['product']

    with open('updated_csv.csv', mode='a') as csv_update0:
        fieldnames = ['sales', 'date', 'region']
        csv_writer = csv.DictWriter(csv_update0, fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in updated_data:
            csv_writer.writerow(row)

print(len(updated_data))