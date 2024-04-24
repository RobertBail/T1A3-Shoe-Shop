import os
import csv
from prettytable import PrettyTable

def view_inventory(file_name):
    #try:
        with open(file_name, "r", newline='') as f:        
             table_contents = csv.reader(f)            
             table = PrettyTable()
             file_data = list(table_contents)
             table.field_names = file_data[0]
             for data in file_data[1:-1]:
              if data:
                 table.add_row(data)
             print(table)


def add_product(file_name):
    print("Add a product to the inventory list")
    product = input("Enter the product: ")
    quantity = input("Enter the quantity: ")
    price = input("Enter the price, $: ")
    sizes_available_US = input("Enter the sizes available (use -- to indicate size unavailable): ")
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([product, quantity, price, sizes_available_US])
# I was intending to add the below if possible
    return print("New product added to the inventory list")


#def remove_product(file_name):
    
#def update_quantity(file_name):

#def update_price(file_name): 
    
#def update_sizes_available(file_name):

def read_csv(file_name):
     with open(file_name, "r", newline='') as f:        
             reader = csv.reader(f)
             data = list(reader)
             return data

def sort_alphabetically(data):
          print(data)
          #header = data[1]         
          sorted_data = sorted(data[1:], key=lambda x: x[0])
          #sorted_data.insert(1, header)
          return sorted_data
          #len or range

def write_csv(file_name, sorted_data):
      with open(file_name, 'w', newline='') as csv_file:
          writer = csv.writer(csv_file)
          writer.writerows(sorted_data)

def sort_csv(file_name):
    data = read_csv(file_name)
    sorted_data = sort_alphabetically(data)
    write_csv("sorted_" + file_name, sorted_data)

sort_csv('inventory_list.csv')
#or sorted_inventory_list.csv