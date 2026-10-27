import csv
import statistics

def slice_file(csv_file, start, end):
    data = []
    for i, line in enumerate(csv_file):
        if i == 0 :
            continue
        if i >=start :
            data_entry = line.split(",")
            data.append(data_entry)
        if  i >=end :
            break
    print(data)
    return data
def find_popular(csv_file):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter = ",")
    drinks = [data["coffee_name"] for data in reader]
    statistics.mode(drinks)

    # for data in reader:
    #     drink = data["coffee_name"]
    #     if drinks.get(drink) is None:
    #         drinks[drink] = 0
    #     drinks[drink] += 1
    # res = max(drinks, key = lambda drink_key: drinks[drink_key])    
    # print(res)

def compute_month_income(csv_file, month):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter = ",")
    income = 0
    for data in reader:
        money = data["money"]
        month = data["Monthsort"]
        if month == month_input:
            income += float(money)
        print(round(income, 2))
        return income

if __name__ == "__main__":
    START = 1
    END = 5
    with open("coffe_sales.csv") as coffe_csv:
        month = input("Введите месяц 1-12: ")
        compute_month_income(coffe_csv, int(month))
        #find_popular(coffe_csv)