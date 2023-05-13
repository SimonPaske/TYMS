import os
import datetime
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate


from pyfiglet import Figlet

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('tyms.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('tyms')

info = SHEET.worksheet('info').get_all_values()


def main_menu():
    """
    Main menu for TYMS
    """
    os.system('clear')
    startup()
    while True:
        print('Welcome to TYMS\n')
        print('Please select an option:')
        print('1. View TYMS information')
        print('2. Update information in TYMS')
        print('3. Add new information to TYMS')
        print('4. Delete information from TYMS')
        print('5. Exit TYMS')
        print('\n')

        choice = input('Enter your selection: \n')
        try:
            choice = int(choice)
        except ValueError:
            print('Please enter a number between 1 and 5\n')
            print('\n')
            continue

        os.system('clear')
        if choice == 1:
            print('\n')
            print('You selected: 1.\n')
            print('Please select an option\n')

            while True:
                print('1. View all information')
                print('2. View latest 3 arrivals')
                print('3. View  earliest 3 arrivals')
                print('4. Back to Main Menu\n')

                subchoice_str = input('Enter your selection (1-4):\n')

                try:
                    subchoice = int(subchoice_str)
                except ValueError:
                    os.system('clear')

                    print('\n')
                    print('Please enter a number between 1 and 2\n')
                    print('\n')
                    continue

                if subchoice == 1:
                    os.system('clear')
                    print('\n')
                    print('1. View all TYMS information\n')
                    print('\n')
                    print(tyms_info())
                    print('\n')
                    print('\n')

                elif subchoice == 2:
                    os.system('clear')
                    print('2. View latest 3 arrivals')
                    print('\n')
                    print(last_3_arrivals())
                    print('\n')
                    print('\n')

                elif subchoice == 3:
                    os.system('clear')
                    print('3. View  earliest 3 arrivals')
                    print('\n')
                    print(earliest_3_arrivals())
                    print('\n')
                    print('\n')

                elif subchoice == 4:
                    print('\n')
                    print('4. Back to Main Menu\n')
                    os.system('clear')
                    main_menu()
                    break
                else:
                    print('Please enter a number between 1 and 3\n')
                    print('\n')

        elif choice == 2:
            print('\n')
            print('You selected: Update information in TYMS')
            print('\n')
            print(tyms_info())
            print('\n')
            find_and_replace_value_in_sheet()
            print('\n')
            subchoice_str = input('Do you want to update another information? (y/n)\n')

            while subchoice_str.lower() == 'y':
                print('\n')
                os.system('clear')
                print('\n')
                print(tyms_info())
                print('\n')
                find_and_replace_value_in_sheet()
                print('\n')
                subchoice_str = input('Do you want to update another information? (y/n)\n')
            startup()
            main_menu()

        elif choice == 3:
            print('You selected: 3. Add new information to TYMS')
            print('Please select an option')

        elif choice == 4:
            print('You selected: 4. Delete information from TYMS')
            print('Please select an option')

        elif choice == 5:
            print('Thank you for using TYMS')
            os.system('clear')
            break

        else:
            print('Please enter a number between 1 and 5')
            continue


def headers():
    """
    Return the headers for the table
    """
    return ['Movement nr', 'Truck', 'Trailer', 'Arrival time', 'Seal']


def tabulate_info(tabular_data):
    """
    Display information in a table
    """
    if not tabular_data:
        return ""
    table = tabulate(headers=headers(), tabular_data=tabular_data, tablefmt='presto')
    return table

def last_3_arrivals():
    """
    Display latest 3 arrivals in the table
    """
    return tabulate_info(info[-3:])

def earliest_3_arrivals():
    """
    Display earliest 3 arrivals in the table
    """
    return tabulate_info(info[1:4])

def tyms_info():
    """
    Display all information in TYMS in the table
    """
    global info
    info = SHEET.worksheet('info').get_all_values()
    return tabulate_info(info[1:])

def startup():
    """
    Display startup screen
    """
    f = Figlet(font='Colossal')
    print(f.renderText('TYMS'))
    print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M\n"))

def print_table(rows):
    """
    Print the rows in a formatted table.
    """
    table_data = [[f'{i+1}.'] + row for i, row in enumerate(rows)]
    table = tabulate_info(table_data)
    print(table)
    print('\n')

def find_and_replace_value_in_sheet():
    """
    Find and replace a value in the spreadsheet.
    """
    info_worksheet = SHEET.worksheet('info')

    def search_cells(search_value):
        """
        Search for cells with a given value in the worksheet and return the list of cells.
        """
        cells = info_worksheet.findall(search_value)
        print('Searching for data...')
        print('\n')

        if not cells:
            print("No data found!")
        else:
            rows = info_worksheet.get_all_values()
            if len(cells) == 1:
                cell = cells[0]
                cell_row_info = get_duplicate_rows(rows, cell, search_value)
                print_table(cell_row_info)
                replace_value_in_cell(cell)
            else:
                print('Multiple cells found:\n')
                duplicates = []
                for cell in cells:
                    duplicate_row = rows[cell.row - 1]
                    if duplicate_row not in duplicates:
                        duplicates.append(duplicate_row)
                print_table(duplicates)
                selected_duplicate = select_duplicate(duplicates)
                for cell in cells:
                    row = rows[cell.row - 1]
                    if row == selected_duplicate:
                        replace_value_in_cell(cell)
                        return

    def replace_value_in_cell(cell):
        """
        Prompt the user for a replacement value for the given cell and update the cell in the worksheet.
        """
        replacement_value = input(f'Please enter the replacement value for cell {cell.value}:\n').upper()
        cell.value = replacement_value
        info_worksheet.update_cell(cell.row, cell.col, replacement_value)
        print('\n')
        print(f'Replaced cell {cell.value} with:')
        print(f'{replacement_value}')

    def select_duplicate(duplicates):
        """
        Prompt the user to select a duplicate row from a list of duplicate rows and return the selected row.
        """
        selected_duplicate_index = int(input(f'Please select a duplicate row to replace (1-{len(duplicates)}):\n'))
        print('\n')
        selected_duplicate = duplicates[selected_duplicate_index-1]
        return selected_duplicate

    def get_duplicate_rows(rows, cell, search_value):
        """
        Return the rows in the worksheet that have the same value as the given cell.
        """
        cells = info_worksheet.findall(search_value)
        cell_row_info = []
        for cell in cells:
            cell_row_info.append(rows[cell.row - 1])
        return cell_row_info

    def validate_search_value(search_value):
        """
        Validate the search value entered by the user.
        """
        if not isinstance(search_value, str) or len(search_value) > 8:
            os.system('clear')
            print('\n')
            print('Please enter a valid search value (up to 8 characters):')
            print(f'Your entered data: {search_value}')
            print('Please try again.\n')
            print(tyms_info())
            find_and_replace_value_in_sheet()

    print('\n')
    print('If you want to exit, type "quit".\n')
    search_value = input('Enter the data you are looking for:\n ').upper()
    print('\n')
    if search_value == 'QUIT':
        os.system('clear')
        print('\n')
        print('Thank you for using TYMS')
        print('Back to menu...\n')
        os.system('clear')
        return main_menu()

    validate_search_value(search_value)
    search_cells(search_value)



main_menu()
