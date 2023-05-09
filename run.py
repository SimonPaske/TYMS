import gspread
from google.oauth2.service_account import Credentials
import os
from datetime import datetime, timedelta

from pyfiglet import Figlet
custom_fig = Figlet(font='Colossal')
print(custom_fig.renderText('TYMS'))

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
mvt = SHEET.worksheet('mvt').get_all_values()
trk_trl = SHEET.worksheet('trk_trl').get_all_values()
sta = SHEET.worksheet('sta').get_all_values()
seal = SHEET.worksheet('seal').get_all_values()

def main_menu():
    """
    Main menu for TYMS
    """
    while True:
        print('Welcome to TYMS\n')
        print('Please select an option:')
        print('1. View TYMS information')
        print('2. Update information in TYMS')
        print('3. Add new information to TYMS')
        print('4. Delete information from TYMS')
        print('5. Exit TYMS')

        choice = input('Enter your selection: \n')
        try:
            choice = int(choice)
        except ValueError:
            print('Please enter a number between 1 and 5')
            continue

        os.system('clear')
        if choice == 1:
            print('\n')
            print('You selected: 1. View all TYMS information\n')
            print('Please select an option\n')

            while True:
                print('1. View all information')
                print('2. View latest 3 arrivals')
                print('3. View  earliest 3 arrivals')
                print('4. Back to Main Menu\n')

                subchoice_str = input('Enter your selection (1-3):\n')

                try:
                    subchoice = int(subchoice_str)
                except ValueError:
                    print('Please enter a number between 1 and 2\n')
                    continue

                if subchoice == 1:
                    print('\n')
                    print('1. View all TYMS information\n')
                    print(SHEET.worksheet('info').get_all_values())
                elif subchoice == 2:
                    print('You selected: 2.\n')
                    
                elif subchoice == 3:
                    print('You selected: 3.\n')
                    
                elif subchoice == 4:
                    print('You selected: 4.\n')
                    
                    break
                else:
                    print('Please enter a number between 1 and 3\n')
        elif choice == 2:
            print('You selected: 2. Update information in TYMS')
            print('Please update the new information')
            
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





# main_menu()

# def tyms_info():
#     """
#     Display all information in TYMS
#     """
#     print('------\n')


#     tyms_information = {
#         'Movement code,': mvt,
#         'Truck and Trailer number': trk_trl,
#         'Arrival time': sta,
#         'Seal number': seal
#     }
#     return tyms_information

# tyms_info()
