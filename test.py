import difflib




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
