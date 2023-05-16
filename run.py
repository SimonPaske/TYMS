import re
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

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('tyms')

INFO_VALUES = SHEET.worksheet('info').get_all_values()
headers = ['Movement nr', 'Truck', 'Trailer', 'Arrival time', 'Seal']


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
                    startup()
                    break

                else:
                    print('Please enter a number between 1 and 3\n')
                    print('\n')

        elif choice == 2:
            print('\n')
            print('You selected: Update information in TYMS\n')
            find_and_replace_value_in_sheet()
            yes_or_no_question(find_and_replace_value_in_sheet)

        elif choice == 3:
            print('You selected: Add new information to TYMS\n')
            add_new_data()
            yes_or_no_question(add_new_data)

        elif choice == 4:
            print('You selected: Delete information from TYMS\n')
            print('\n')
            delete_selected_row()
            yes_or_no_question(delete_selected_row)

        elif choice == 5:
            print('Thank you for using TYMS')
            os.system('clear')
            os.sys.exit("done")

        else:
            print('Please enter a number between 1 and 5')
            continue


def last_3_arrivals():
    """
    Display latest 3 arrivals in the table
    """
    return tabulate_info(INFO_VALUES[-3:])


def earliest_3_arrivals():
    """
    Display earliest 3 arrivals in the table
    """
    return tabulate_info(INFO_VALUES[1:4])


def tyms_info():
    """
    Display all information in TYMS in the table
    """
    global INFO_VALUES
    INFO_VALUES = SHEET.worksheet('info').get_all_values()
    return tabulate_info(INFO_VALUES[1:])


def startup():
    """
    Display startup screen
    """
    # Startup screen with Figlet and datetime
    f = Figlet(font='o8')
    print(f.renderText('TYMS'))
    print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M\n"))


def tabulate_info(tabular_data):
    """
    Display information in a table
    """
    if not tabular_data:
        return ""
    table = tabulate(
        headers=headers, tabular_data=tabular_data, tablefmt='presto')
    return table


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
    print(tyms_info())

    def search_cells(search_value):
        """
        Search for cells with a given value
        in the worksheet and return the list of cells.
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
        Prompt the user for a replacement value for
        the given cell and update the cell in the worksheet.
        """
        while True:
            replace_value = input(
                f'Please enter the replacement for {cell.value}:\n').upper()
            if replace_value.lower() == "quit":
                return main_menu()
            else:
                cell.value = replace_value
                info_worksheet.update_cell(cell.row, cell.col, replace_value)
                print('\n')
                print(f'Replaced cell {search_value} with:')
                print(f'{replace_value}\n')
                break

    def select_duplicate(duplicates):
        """
        Prompt the user to select a duplicate row from
        a list of duplicate rows and return the selected row.
        """
        selected_duplicate = None
        while selected_duplicate is None:
            selected_duplicate_index = input(f'Please select a row to replace \
                (1-{len(duplicates)})\n')
            print('\n')
            if selected_duplicate_index.lower() == 'quit':
                print('Thank you for using TYMS')
                print('Back to menu...\n')
                return main_menu()

            try:
                selected_duplicate_index = int(selected_duplicate_index)
                selected_duplicate = duplicates[selected_duplicate_index-1]
            except (ValueError, IndexError):
                print('Invalid input. Please select a valid row or type "quit".\n')
        return selected_duplicate

    def get_duplicate_rows(rows, cell, search_value):
        """
        Return the rows in the worksheet
        that have the same value as the given cell.
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
            print(f'Your entered data: {search_value}\n')
            print('Please try again.\n')
            find_and_replace_value_in_sheet()

    print('\n')
    print('If you want to exit, type "quit".\n')
    search_value = input('Enter the data you are looking for:\n').upper()
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


def yes_or_no_question(continue_func):
    """
    Prompt the user to answer a yes or no question.
    If the user answers "y", continue with the given function.
    If the user answers "n", return to the main menu.
    """
    while True:
        subchoice_str = input('Do you want to continue? (y/n)\n').lower()
        print('\n')
        if subchoice_str == 'y':
            os.system('clear')
            continue_func()
        elif subchoice_str == 'n':
            os.system('clear')
            print('\n')
            print('Thank you for using TYMS')
            print('Back to menu...\n')
            return startup(), main_menu()
        else:
            print('Invalid input. Please enter "y" or "n".')


def add_new_data():
    """
    Add new data to the table by prompting the user to enter
    data for each column, and suggesting headers.
    """
    print(tyms_info())
    print('\n')
    print('Type "quit" to return to the main menu.\n')
    print('Please add new information for:\n')

    global headers
    headers = ['Movement nr', 'Truck', 'Trailer', 'Arrival time', 'Seal']
    new_row = []

    while True:
        for i, header in enumerate(headers):
            if i < 3:
                # Add validator to allow up to 10 strings
                value = input(f'{header}: ')
                while len(value) >= 10:
                    print('\n')
                    print('Invalid input. Please enter up to 10 letters.\n')
                    value = input(f'{header}: ')
            else:
                value = input(f'{header}: ')

            if value.lower() == 'quit':
                print('\n')
                print('Returning to the main menu...')
                print("Type 'y' if you want to restart adding data.")
                print("Type 'n' if you want to exit.")
                print('\n')
                return main_menu()

            if i == 3:
                while not re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', value):
                    print('\n')
                    print(f'Invalid {header} format. Please use HH:MM.\n')
                    value = input(f'{header} (HH:MM): ')

            elif i == 4:
                while not re.match(r'^\d{1,10}$', value):
                    print('\n')
                    print(f'Invalid {header} format. Please use digits.\n')
                    value = input(f'{header}: \n')

            new_row.append(value.upper())

        info_worksheet = SHEET.worksheet('info')
        info_worksheet.append_row(new_row)
        print('\n')
        print('Row added successfully!\n')
        print('\n')
        input('Please press ENTER to continue.')
        os.system('clear')
        add_new_data()
        print_table(info_worksheet.get_all_values()[1:])
        new_row = []


def delete_selected_row():
    """
    Delete the selected row from the worksheet.
    """
    rows = SHEET.worksheet('info').get_all_values()
    print_table(rows)
    print('\n')
    print('Type "quit" to return to main menu. \n')
    # Validate user input for row selection
    while True:
        selected_row_num = input('Please select row to delete:\n').upper()
        if selected_row_num == "QUIT":
            return main_menu()
        elif not selected_row_num.isdigit() \
                or int(selected_row_num) > len(rows):
            print('\n')
            print('Invalid input! Please enter a valid row number.\n')
        else:
            selected_row_num = int(selected_row_num)
            print('\n')
            break

    # Confirm deletion
    print('Press ENTER to delete or type "cancel" to return to the main menu.')
    confirm = input(
        f'\nAre you sure you want to delete row {selected_row_num}?\n')
    if confirm.lower() == "cancel":
        return main_menu()
    elif confirm != "":
        print("Invalid input. Please press ENTER to delete the row.\n")
        return delete_selected_row()

    SHEET.worksheet('info').delete_rows(selected_row_num)

    print(f'\nRow {selected_row_num} has been deleted.\n')
    # Update the table to reflect the changes
    rows = SHEET.worksheet('info').get_all_values()
    print_table(rows)


main_menu()
