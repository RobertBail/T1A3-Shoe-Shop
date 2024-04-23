from colored import Fore, Back, Style

from inventory_functions import clear_console, general_menu, check_csv
from inventory_functions import (
    main_options_list,
    si_file_path,
    si_header,
   
)

check_csv(si_file_path, si_header)


clear_console()

print(
    f"{Style.BOLD}{Fore.BLUE}Welcome to the Shoe Shop Inventory!{Style.reset}\n"
)

general_menu("Main", main_options_list)