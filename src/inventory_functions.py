import os
import csv

from colored import Fore, Back, Style
from prettytable import PrettyTable
#from datetime import datetime
import math as mt

si_file_path="./data/inventory_list.csv"
si_header="product,quantity,price,sizes_available_US\n"

menu_list = []

# Main Menu Options
main_options_list = {
    
    " View Shoe Shop Inventory List": "general_menu('Shoe Shop Inventory List', si_options_list)",
    " Enter Stock Entry Menu": "general_menu('Stock Entry', se_options_list)",
   
}

si_options_list {
    " View Shoe Shop Inventory List": "si_display(si_file_path)",
   
}

se_options_list{
    #" Enter a new stock item": "enter_stock_item('Entry', se_file_path, si_file_path)",
    " Enter a new stock item": "create_submenu('New Stock Item', si_file_path)",
    " Delete a stock item": "delete_submenu('Stock Items', si_file_path, si_header)",
}

#men-and-boys, women-and-girls
#sizes_available_US(use -- to indicate size unavailable)
#sort list alphabetically function?