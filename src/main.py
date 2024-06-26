import os.path
#from colored import Fore, Back, Style
#from prettytable import PrettyTable
# (colored==2.2.4)
# (wcwidth==0.2.13)


from inventory_functions import (view_inventory, view_updated_inventory, view_sorted_inventory, 
add_product, remove_product_list, remove_product_updatedlist, remove_product_sortedlist, update_product, read_csv, product_data)

print("Welcome to the Shoe Shop Inventory!")

def create_menu():
    print("1. Enter 1 to view the Inventory List")
    print("2. Enter 2 to view Updated Inventory")
    print("3. Enter 3 to view Alphabetically Sorted Inventory")
    print("4. Enter 4 to add a product to Inventory List")
    print("5. Enter 5 to remove a product from Inventory List")
    print("6. Enter 6 to remove a product from Updated Inventory List")
    print("7. Enter 7 to remove a product from Sorted Inventory List")
    print("8. Enter 8 to update quantity, price, sizes available of a product")
    print("9. Enter 9 to sort list alphabetically")
    print("10. Enter 10 to view widespread shoe retail data (US data)")
    print("11. Enter 11 to exit")
#add sort list alphabetically function?
    user_choice = input("Enter your selection: ")
    print(user_choice)
    return user_choice

file_name="inventory_list.csv"
#data = view_inventory(file_name)
#sorted_data = sort_alphabetically(data)
#data = list
api_url="https://amazon-merchant-data.p.rapidapi.com/search-products"

if (not os.path.isfile(file_name)):
   print("Creating inventory file as it doesn't exist")
   f = open(file_name, "w")
   f.write("product,quantity,price,sizes_available_US,ID_No\n")
   f.close()

file_name2="updated_inventory_list.csv"

if (not os.path.isfile(file_name2)):
   print("Creating inventory file as it doesn't exist")
   f = open(file_name2, "w")
   f.write("product,quantity,price,sizes_available_US,ID_No\n")
   f.close()

file_name3="sorted_inventory_list.csv"

if (not os.path.isfile(file_name3)):
   print("Creating inventory file as it doesn't exist")
   f = open(file_name3, "w")
   f.write("product,quantity,price,sizes_available_US,ID_No\n")
   f.close()

choice =""

while choice!="11":
   choice = create_menu()
   if(choice == "1"):
      view_inventory(file_name)
   elif (choice == "2"):
      view_updated_inventory(file_name2)
   elif (choice == "3"):
      view_sorted_inventory(file_name3)
   elif (choice == "4"):
      add_product(file_name)
   elif (choice == "5"):
      remove_product_list(file_name)
   elif (choice =="6"):
      remove_product_updatedlist(file_name2)
   elif (choice =="7"):  
      remove_product_sortedlist(file_name3)
   elif (choice == "8"):
      update_product(file_name2)
   elif (choice == "9"):
       read_csv(file_name)
       #sort_alphabetically(data)
       #write_csv(file_name, sorted_data)
       #sort_csv(file_name)
   elif (choice == "10"):
      product_data(api_url)
   elif (choice == "11"):
      print("You have exited the inventory...")
   else:
      print("Please only enter the options shown above")

print("Thanks for using the Shoe Shop Inventory List")

