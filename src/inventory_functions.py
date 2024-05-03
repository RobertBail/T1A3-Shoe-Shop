import os
import csv
import requests
import json
#import itertools
from prettytable import PrettyTable

def product_data(api_url):
    api_url= "https://amazon-merchant-data.p.rapidapi.com/search-products"
    querystring = {"term":"shoes","country":"us"}
    headers = {
	"X-RapidAPI-Key": "1f43f6d9acmsh5e30329605fec9fp1f3b76jsnde6a9580f284",
	"X-RapidAPI-Host": "amazon-merchant-data.p.rapidapi.com"
}

    response = requests.get(api_url, headers=headers, params=querystring)

    print(response.json())
#https://acho.io/blogs/how-to-pull-data-from-an-api
#I tried looking up how (ie. code format) to display this product API data in a PrettyTable but didn't see a good example and possibly too complicated for this data

def view_inventory(file_name):
    try:
        with open(file_name, "r", newline='') as f:        
             table_contents = csv.reader(f)            
             table = PrettyTable()
             file_data = list(table_contents)
             table.field_names = file_data[0]
             for data in file_data[1:-1]:
              if data:
                 table.add_row(data)
             print(table)
    except FileNotFoundError:
        return []

def view_updated_inventory(file_name2):
      try:
        with open(file_name2, "r", newline='') as f:        
             table_contents = csv.reader(f)            
             table = PrettyTable()
             file_data = list(table_contents)
             table.field_names = file_data[0]
             for data in file_data[1:-1]:
              if data:
                 table.add_row(data)
             print(table)
      except FileNotFoundError:
        return []

def view_sorted_inventory(file_name3):
    try:
        with open(file_name3, "r", newline='') as f:        
             table_contents = csv.reader(f)            
             table = PrettyTable()
             file_data = list(table_contents)
             table.field_names = file_data[0]
             for data in file_data[1:-1]:
              if data:
                 table.add_row(data)
             print(table)
    except FileNotFoundError:
        return []

def add_product(file_name):
    print("*Add a product to the inventory list*")
    ID_No = input("Enter new product ID number (add to last): ")
#I was trying to find how to auto-increment ID_No ideally, but couldn't find a great example/solution for this format/situation, 
#eg. they often involved several more steps and a bit confusing, or didn't look to suit this purpose
    product = input("Enter the product: ")
    quantity = input("Enter the quantity: ")
    price = input("Enter the price, $: ")
    sizes_available_US = input("Enter the sizes available (use -- to indicate size unavailable): ")

   # data = []
   try:
     with open(file_name, "a", newline='') as f:
          writer = csv.writer(f, delimiter=',')
          writer.writerow([product, quantity, price, sizes_available_US, ID_No])
#I have to put ID No. at end because the "sort_alphabetically" function/list wasn't working properly with ID No. in first column, "sort_alphabetically" works much better with ID No in last column

     return print("New product added to the inventory list")
    except FileNotFoundError:
        return []


def remove_product_list(file_name):
    ID_No = input("Enter the ID number of product that will be removed: ")
    inventory_list = []
     try:
       with open(file_name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
              if (ID_No != row[0]):
               inventory_list.append(row)
       with open(file_name, "w") as f:
            writer = csv.writer(f)
            writer.writerows(inventory_list)
      except FileNotFoundError:
        return []

def remove_product_UpdatedList(file_name2):
    ID_No = input("Enter the ID number of product that will be removed: ")
    inventory_list = []
     try:
       with open(file_name2, "r") as f:
            reader = csv.reader(f)
            for row in reader:
              if (ID_No != row[0]):
               inventory_list.append(row)
       with open(file_name2, "w") as f:
            writer = csv.writer(f)
            writer.writerows(inventory_list)
     except FileNotFoundError:
        return []


def remove_product_SortedList(file_name3):
    ID_No = input("Enter the ID number of product that will be removed: ")
    inventory_list = []
      try:
       with open(file_name3, "r") as f:
            reader = csv.reader(f)
            for row in reader:
              if (ID_No != row[0]):
               inventory_list.append(row)
       with open(file_name3, "w") as f:
            writer = csv.writer(f)
            writer.writerows(inventory_list)
      except FileNotFoundError:
        return []

def update_product(file_name2):
    print("*Updating a product in the inventory list*")
    ID_No = input("Enter the ID number of product to be updated: ")
    product = input("Enter the product you need to update: ")
    quantity = input("Enter the updated quantity: ")
    price = input("Enter the updated price, $: ")
    sizes_available_US = input("Enter the updated Sizes Available (US): ")
     try:
       with open(file_name2, "a", newline='') as f2:
           writer = csv.writer(f2, delimiter=',')
           writer.writerow([product, quantity, price, sizes_available_US, ID_No])
     except FileNotFoundError:
        return []
#I originally wanted (thought the user could) modify this data individually/separately in each row, ie. separate functions/options for update quantity, price, sizes_available_US, and it wouldn't be much different than add_product function,
#but that doesn't seem to be as possible or easy, haven't seen a good example for this situation with a csv, so the solution for now is adding the updated rows to another file, updated_inventory_list.csv               

#def update_price(file_name): 
    
#def update_sizes_available(file_name):

def read_csv(file_name):
     try:
       with open(file_name, "r", newline='') as f:        
             reader = csv.reader(f)
             data = list(reader)
             return data
     except FileNotFoundError:
        return []

def sort_alphabetically(data):
          print(data)
          header = data[0] 
   #(Error:object is not subscriptable?)        
          sorted_data = sorted(data[1:], key=lambda x: x[0])
          sorted_data.insert(0, header)
          return sorted_data
          #len or range

def write_csv(file_name, sorted_data):
      try:
        with open(file_name, 'w', newline='') as csv_file:
           writer = csv.writer(csv_file)
           writer.writerows(sorted_data)
      except FileNotFoundError:
        return []

def sort_csv(file_name):
    data = read_csv(file_name)
    sorted_data = sort_alphabetically(data)
    write_csv("sorted_" + file_name, sorted_data)

sort_csv('inventory_list.csv')
#or sorted_inventory_list.csv