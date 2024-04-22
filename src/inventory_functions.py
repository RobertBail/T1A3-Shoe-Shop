import os
import csv

from colored import Fore, Back, Style
from prettytable import PrettyTable
from datetime import datetime

menu_list = []

# Main Menu Options
main_options_list = {
    
    " View Shoe Shop Inventory List": "general_menu('Shoe Shop Inventory List', si_options_list)",
    " Enter Stock Entry Menu": "general_menu('Stock Entry', se_options_list)",
    #" Enter Workout Templates Menu": "general_menu('Workout Templates', wt_options_list)",
}