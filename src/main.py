import os.path
#from colored import Fore, Back, Style
#from prettytable import PrettyTable


#from inventory_functions import list
from inventory_functions import (view_inventory, add_product)
#from inventory_functions import (view_inventory, sort_alphabetically, read_csv, write_csv, sort_csv, 
#add_product)
 #remove_product, update_quantity, update_price, update_sizes_available
#from inventory_functions import clear_console, general_menu, check_csv
#from inventory_functions import (
  #  main_options_list,
   # si_file_path,
   # si_header,
   
#)

#check_csv(si_file_path, si_header)


#clear_console()

#print(
    #f"{Style.BOLD}{Fore.BLUE}Welcome to the Shoe Shop Inventory!{Style.reset}\n"
#)
print("Welcome to the Shoe Shop Inventory!")
   
#general_menu("Main", main_options_list)

def create_menu():
    print("1. Enter 1 to view Shoe Shop Inventory List")
    print("2. Enter 2 to add a product")
    print("3. Enter 3 to remove a product")
    print("4. Enter 4 to update quantity of a product")
    print("5. Enter 5 to update price of a product")
    print("6. Enter 6 to update sizes available of a product")
    print("7. Enter 7 to sort list alphabetically")
    print("8. Enter 8 to exit")
#add sort list alphabetically function?
    user_choice = input("Enter your selection: ")
    print(user_choice)
    return user_choice

file_name="inventory_list.csv"
#data = view_inventory(file_name)
#sorted_data = sort_alphabetically(data)
#data = list

if (not os.path.isfile(file_name)):
   print("Creating inventory file as it doesn't exist")
   f = open(file_name, "w")
   f.write("product,quantity,price,sizes_available_US")
   f.close()

choice =""

while choice!="8":
   choice = create_menu()
   if(choice == "1"):
      view_inventory(file_name)
   elif (choice == "2"):
      add_product(file_name),
   elif (choice == "3"):
      remove_product(file_name)
   elif (choice == "4"):
      update_quantity(file_name)
   elif (choice == "5"):
      update_price(file_name)
   elif (choice == "6"):
      update_sizes_available(file_name)
   elif (choice == "7"):
      read_csv(file_name)
      # stack on top? sort_alphabetically(data), write_csv(file_name, sorted_data), sort_csv(file_name)
   elif (choice == "8"):
      print("You have exited the inventory")
   else:
      print("Please only enter the options shown above")

print("Thanks for using the Shoe Shop Inventory List")

