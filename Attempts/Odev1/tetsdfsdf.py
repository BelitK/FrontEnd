#! /usr/bin/env python3
import json
import locale
import sys
from reports imoprt generate as report
from emails import generate as email_generate
from emails import send as email_send

def load_data(filename):
    with open(filename) as json_file:
        new_data = json.load(json_file)
        data = sorted(new_data, key=lambda i: i['total_sales'])
    return data

def format_car(car):
    return "{} {} ({})".format(car["car_make"],car["car_model"],car["car_year"])

def process_data(data):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    max_revenue = {"revenue": 0}
    sales = {"total_sales": 0}
    best_car = {}
    for items in data :
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"]= item_revenue
            max_revenue = item
        if item["total_sales"]>sales["total_sales"]:
            sales = item
        if not item["car"]["car_year"] in best_car.keys():
            best_car[item["car"]["car_year"]]= item["total_sales"]
        else :
            best_car[item["car"]["car_year"]] += item["total_sales"]

        all_values = best_car.values()
        max_value = max(all_values)
        max_key = max(best_car, key=best_car.get)
    summary = ["The {} generated the most revenue: $()".format(format_car(max_revenue["car"]),max_revenue["revenue"]),"The {} had the most sales: {}".format(sales["car"],sales["total_sales"]),"The most popular year was {} with {} sales.".format(max_key, max_value),
    ]
    return summary
def cars_dict_to_table(car_date):
    table_data = [["ID","Car","Price","Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]),item["price"],item["item_sales"]])
    return table_data
    
def main(argv):
    data = load_data("/home/student-04-b36fbde96c4c/car_sales.json")
    summary = process_data(data)
    new_summary = '<br/>'.join(summary)
    print(summary)
    report('/tmp/cars.pdf',"Cars report",new_summary,cars_dict_to_table(data))
    msg = email_generate("automation@example.com","student-04-b36fbde96c4c@example.com","Sales summary for last month", new_summary, "/tmp/cars.pdf")
    email_send(msg)

if __name__="__main__":
    main(sys.argv)