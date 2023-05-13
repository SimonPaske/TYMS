import difflib
import re

def add_new_data():
    """
    Add new data to the table by prompting the user to enter data for each column, and suggesting headers.
    """
    print(tyms_info())
    print('\n')
    print('Type "quit" to return to main menu.\n')
    print('Please add new information for:\n')

    global headers
    headers = ['Movement nr', 'Truck', 'Trailer', 'Arrival time', 'Seal']
    new_row = []

    while True:
        for i, header in enumerate(headers):
            value = input(f'{header}: ')

            if value.lower() == 'quit':
                print('\n')
                print('Returning to main menu...')
                print("Type 'y' if you want restart adding data.")
                print("Type 'n' if you want to exit.")
                print('\n')
                return

            if i == 3:
                while not re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', value):
                    print('\n')
                    print(f'Invalid {header} format, please use HH:MM \n')
                    value = input(f'{header} (HH:MM): ')

            elif i == 4:
                while not re.match(r'^\d{1,10}$', value):
                    print('\n')
                    print(f'Invalid {header} format, please use digits\n')
                    value = input(f'{header}: \n')

            new_row.append(value.upper())

        info_worksheet = SHEET.worksheet('info')
        info_worksheet.append_row(new_row)
        print('\n')
        print('Row added successfully!\n')
        print('\n')
        print_table(info_worksheet.get_all_values()[1:])
        new_row = []
        
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

def delete_selected_row():
    """
    Delete the selected row from the worksheet.
    """
    rows = SHEET.worksheet('info').get_all_values()
    print_table(rows)

    # Validate user input for row selection
    selected_row_num = input('Please select row you want to delete: \n')
    while not selected_row_num.isdigit() or int(selected_row_num) > len(rows):
        print('\n')
        print('Invalid input! Please enter a valid row number that corresponds to the table above.\n')
        selected_row_num = input('Please select row you want to delete: ')
    selected_row_num = int(selected_row_num)

    SHEET.worksheet('info').delete_rows(selected_row_num)

    print(f'\nRow {selected_row_num} has been deleted.\n')
    # Update the table to reflect the changes
    rows = SHEET.worksheet('info').get_all_values()
    print_table(rows)
