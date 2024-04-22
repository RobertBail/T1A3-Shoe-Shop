from colored import Fore, Back, Style

from inventory_functions import clear_console, general_menu, check_csv
from inventory_functions import (
    main_options_list,
    pw_file_path,
    el_file_path,
    wt_file_path,
    pw_header,
    el_header,
    wt_header,
)

check_csv(pw_file_path, pw_header)
check_csv(el_file_path, el_header)
check_csv(wt_file_path, wt_header)

clear_console()

print(
    f"{Style.BOLD}{Fore.BLUE}Welcome to the Shoe Shop Inventory!{Style.reset}\n"
)

general_menu("Main", main_options_list)