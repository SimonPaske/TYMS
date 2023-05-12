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
# mvt = SHEET.worksheet('mvt').get_all_values()
# trk_trl = SHEET.worksheet('trk_trl').get_all_values()
# sta = SHEET.worksheet('sta').get_all_values()
# seal = SHEET.worksheet('seal').get_all_values()



def main_menu():
    """
    Main menu for TYMS
    """
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
            print('You selected: Update information in TYMS')
            print('\n')
            # print('\n')
            print(tyms_info())
            print('\n')
            find_and_replace_value_in_sheet()
            print('\n')
            print('Information updated successfully.\n')
            print('\n')
            subchoice_str = input('Do you want to update another information? (y/n)\n')
            if subchoice_str.lower() == 'y':
                print('\n')
                os.system('clear')
                print('\n')
                
                print(tyms_info())
                print('\n')
                find_and_replace_value_in_sheet()
                
                continue
            elif subchoice_str.lower() == 'n':
                os.system('clear')
                startup()
                break
            else:
                print('Invalid action. Please enter "y" or "n".\n')
                continue
            # while True:
            #     # print("What do you want to do? ")
            #     # print('1. Update existing information')
            #     # print('2. Add new information')
            #     print('3. Back to Main Menu\n')

            #     subchoice_str = input('Enter your selection (1-3):\n')
            #     try:
            #         subchoice = int(subchoice_str)
            #     except ValueError:

            #         print('Invalid action. Please enter a number between 1 and 3\n')
            #         continue

                # if subchoice == 1:
                

                # else:
                #     print("Invalid action. Please choose add, update, or quit.")
                #     print('6. Back to Main Menu\n')
                # else:
                #     print('Please enter a number between 1 and 3\n')
                    # continue
        elif choice == 3:
            print('You selected: 3. Add new information to TYMS')
            print('Please select an option')

        elif choice == 4:
            print('You selected: 4. Delete information from TYMS')
            print('Please select an option')

        elif choice == 5:
            print('Thank you for using TYMS')
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
    table = tabulate(headers = headers(), tabular_data = tabular_data, tablefmt = 'presto')
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
    return tabulate_info(info[1:])

def startup():
    """
    Display startup screen
    """
    f = Figlet(font='Colossal')
    print(f.renderText('TYMS'))
    print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M\n"))

def find_and_replace_value_in_sheet():
    """
    Find and replace a value in the spreadsheet.
    """
    print('If you want to exit, type "exit".\n')
    search_value = input('Enter the data you are looking for:\n ').upper()

    if search_value == 'EXIT':
        os.system('clear')
        print('\n')
        print('Thank you for using TYMS')
        print('Back to menu...\n')
        return
    print('\n')
    print(f'Your entered data: {search_value}\n')

    print('Searching for data...')
    info_worksheet = SHEET.worksheet('info')
    cells = info_worksheet.findall(search_value)

    if cells:
        print(f'{len(cells)} cells found:')
        print('\n')
        replacement_value = input('Please enter the replacement value:\n').upper()
        print('\n')
        for cell in cells:
            cell.value = replacement_value
            info_worksheet.update_cell(cell.row, cell.col, replacement_value)
            print('Replaced with:')
            print(f'{replacement_value}')
    else:
        print(f'No data found containing "{search_value}".')
        print('Please try again.\n')
        find_and_replace_value_in_sheet()
print('\n')
print('\n')
print('\n')
os.system('clear')

main_menu()

