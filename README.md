# Truck Yard Management System

![example](docs/screenshots/example.gif)

## Table Of Contents

- [Truck Yard Management System](#truck-yard-management-system)
  - [Table Of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Goals](#goals)
    - [Target Audience](#target-audience)
    - [Users Feedback](#users-feedback)
    - [Features Planned](#features-planned)
  - [Structure](#structure)
    - [Features](#features)
    - [Logical Flow](#logical-flow)
    - [Database Design](#database-design)
  - [Technologies](#technologies)
- [Testing](#testing)
  - [Testing Documentation for TYMS Code](#testing-documentation-for-tyms-code)
  - [Test Cases](#test-cases)
    - [Case 1: View TYMS Information](#case-1-view-tyms-information)
    - [Case 2: Update Information in TYMS](#case-2-update-information-in-tyms)
    - [Case 3: Add New Information to TYMS](#case-3-add-new-information-to-tyms)
    - [Case 4: Delete Information from TYMS](#case-4-delete-information-from-tyms)
    - [Case 5: Invalid Input Handling](#case-5-invalid-input-handling)
    - [Case 6: Quitting the Application](#case-6-quitting-the-application)
  - [Conclusion](#conclusion)
    - [Pep8 Validation](#pep8-validation)

---

## Introduction

Transport yards play a crucial role in the logistics industry, serving as hubs for the temporary storage and transfer of goods. Effective management of these yards is essential to ensure smooth operations and timely delivery of cargo. TYMS offers a simplified solution to streamline the tracking and administration of truck movements within a transport yard.

### Goals

The primary goals of TYMS are as follows:

Efficient Information Management: TYMS enables users to store, organize, and access essential information related to truck movements, trailers, arrival times, and seals. The program provides functionalities to view, update, add, and delete data, ensuring accurate and up-to-date records.
Improved Operational Visibility: By providing different views of the transport yard information, such as all entries, latest arrivals, and earliest arrivals, TYMS allows users to gain valuable insights into the current status of the yard. This visibility helps optimize resource allocation, monitor truck movements, and make informed decisions.
Simplified Data Manipulation: TYMS simplifies the process of updating and modifying data within the system. It offers search and replace functionalities to quickly find specific entries and replace values as needed. Additionally, the program allows for the convenient addition of new data, ensuring comprehensive and complete records.
Integration with Google Sheets: TYMS leverages the power of Google Sheets as a backend storage solution. By utilizing the Google Sheets API, the program provides seamless synchronization and real-time collaboration capabilities, allowing multiple users to work on the same data simultaneously.

### Target Audience

TYMS is designed for individuals or teams involved in the management and operation of transport yards. The program caters to a wide range of users, including logistics managers, yard supervisors, dispatchers, and administrative staff. TYMS offers a simple and intuitive interface, making it accessible to users with varying levels of technical expertise.

Whether it is tracking truck movements, managing trailer information, monitoring arrival times, or maintaining seal records, TYMS provides a convenient and centralized solution for efficiently managing transport yard operations.

### Users Feedback

The TYMS program is a helpful tool for managing information related to movements in the transportation industry. It provides a user-friendly interface. It gives a professional feel to the program. Adding new information to TYMS is straightforward. The program prompts the user to enter data for each column, suggesting the headers as a guide. It validates the input format for specific columns, such as the arrival time and the seal number. This ensures data consistency and accuracy.

### Features Planned

- Search and Filter Functionality: Allow users to search for specific information based on criteria such as truck number, trailer number, or arrival time. This would make it easier to find specific entries in a large dataset.
- Sorting: Implement sorting options to organize the information in ascending or descending order based on different columns, such as arrival time or movement number. This would help users analyze the data more effectively.
- Notifications and Reminders: Integrate notification functionality to send reminders or notifications when a truck is expected to arrive or when an entry is modified.

---

## Structure

### Features

IMPLEMENTATION

---

- Main Menu Options:

  - When the program starts, a main menu option will appear with the following options:
    1. View TYMS Information
    2. Update Information in TYMS
    3. Add New Information to TYMS
    4. Delete Information from TYMS
    5. Exit TYMS
  - The user must input a correct number corresponding to each menu or they will be alerted of an incorrect choice and the menu will be presented again.
  - This feature will allow the user to easily access the sub-menus to each category to perform the operations needed.

**Main Menu**
![main menu](docs/screenshots/main_menu.png)

**Invalid input**
![invalid main menu](docs/screenshots/main_menu_invalid.png)

---

- Sub-menu options for "View TYMS Information":
  - When a user selects "View TYMS Information" from the main menu, the following options will appear:
    1. View All Information - This option will print all information in the table.
    2. View Latest Three Arrivals - This option will print the latest 3 arrivals.
    3. View Earliest Three Arrivals - This option will print the earliest 3 arrivals.
    4. Back to Main Menu - This option will bring the user to the main menu.
  - The user must input a correct number corresponding to each menu or they will be alerted of an incorrect choice and the menu will be presented again.
  - This feature will allow the user to easily access the sub-menus to each category to perform the operations needed.

**View TYMS Information**
![information](docs/screenshots/sub_menu_view_tyms_information.png)

**View All Information**
![all information](docs/screenshots/view_all_tyms_information.png)

**View Latest Three Arrivals**
![3 latest](docs/screenshots/view_3_latest.png)

**View Earliest Three Arrivals**
![3 earliest](docs/screenshots/view_3_earliest.png)

**Invalid input**
![invalid information](docs/screenshots/view_tyms_information_invalid.png)

---

- Options for "Update Information in TYMS":
  - When a user selects Update Information in TYMS from the main menu, the following options will appear and the table will be printed:
    1. Find and Replace a Value - This option will ask the user to enter a value that is in the table and replace it with the new value. Each time value is found it will be printed as a whole row containing that value.
    2. Back to Main Menu - This option will bring the user back to the main menu when "quit is typed.
  - The user must input a correct value corresponding to the table or they will be alerted of an incorrect choice and the table will be presented again.
  - This feature will allow the user to easily perform the operations needed.

**Update Information in TYMS**
![update info](docs/screenshots/update_info.png)

**Info found**
![info found](docs/screenshots/update_found.png)

**Duplicate found**
![duplicate found](docs/screenshots/update_duplicate.png)

**Replaced Info**
![replaced info](docs/screenshots/update_replaced.png)

**Invalid input**
![invalid info](docs/screenshots/update_invalid.png)

---

- Options for "Add New Information to TYMS":
  - When the user selects Add New Information to TYMS, the table will be printed and will be prompted to enter new information in the following order.
      1. Movement nr - This option lets the user enter up to 10 characters in the string.
      2. Truck - This option lets the user enter up to 10 characters in the string.
      3. Trailer - This option lets the user enter up to 10 characters in the string.
      4. Arrival time - This option asks the user to enter time in HH:MM format.
      5. Seal - This option lets the user enter up to 10 digits.
  - The user must input a correct value corresponding to the table or they will be alerted of an incorrect choice.
  - This feature will allow the user to easily perform the operations needed.
  - Users can type "quit" while entering new information to back to the main menu.

**Add New Information to TYMS**
![add new](docs/screenshots/add_new.png)

**Add New Info**
![add new info](docs/screenshots/add_new_info.png)

**Press ENTER**
![add new enter](docs/screenshots/add_new_enter.png)

**Invalid Add New**
![invalid add new](docs/screenshots/invalid_add_new.png)

**Invalid Add Seal**
![invalid seal](docs/screenshots/invalid_seal_add_new.png)

**Invalid Add Time**
![invalid time](docs/screenshots/invalid_time_add_new.png)

---

- Option for "Delete Information from TYMS":
  - When the user selects Delete Information from TYMS, the table will be printed with the row numbers and the user will be prompted to enter the corresponding row number to delete it.
  - When the user enters the row number they will be asked to confirm their choice by pressing the "Enter" button on a keyboard or typing "cancel" to cancel the operation and back to the main menu.
  - If a user press the "Enter" the program deletes the selected row and asks the user to continue or leave the operation by typing "y" or "n" respectively.
  - Back to Main Menu - When the user type "quit" instead of row number, the program goes back to the main menu.

**Delete**
![delete](docs/screenshots/delete.png)

**Delete Invalid**
![invalid delete](docs/screenshots/invalid_delete.png)

**Delete Enter**
![delete enter](docs/screenshots/delete_enter.png)

**Delete Continue**

![delete continue](docs/screenshots/delete_continue.png)

---

### Logical Flow

**Main Menu**
![start program](docs/flowchart/start_program.png)

**View Information**
![View info](docs/flowchart/view_tyms_info.png)

**Update Tyms**
![update info](docs/flowchart/update_tyms_info.png)

**Add Information**
![add info](docs/flowchart/add_new_info.png)

**Delete Information**
![delete info](docs/flowchart/delete_info.png)

---

### Database Design

Google Sheets was used for storing data. In the sheet are stored the Movement number (A row), Truck number (B row), Trailer number (C row), Arrival time (D row) and Seal number (E row).

Google Sheets automatically saves changes and maintains version history, providing a level of data security and ensuring that previous versions of the database can be restored if necessary. Additionally, Google's robust infrastructure helps protect against data loss or corruption.

![google sheets](docs/screenshots/google_sheets.png)

---

## Technologies

- Python - Python was the main language used to build the application.
  - Python packages used:
    - gspread - used for working with Google Sheets. It provides a convenient API for accessing and manipulating spreadsheet data, such as reading, writing, and formatting cells, creating and deleting sheets, and managing permissions.
    - datetime - used to create, manipulate, and format date and time.
    - tabulate - useed to convert data into nicely formatted tables.
    - pyfiglet - used to create ASCII art from the text.
    - google.auth - used to provides authentication-related functionality for Google APIs.
    - os - used to provide functions for interacting with the operating system.
    - re - used to for data validation.

---

# Testing

---

## Testing Documentation for TYMS Code

## Test Cases

### Case 1: View TYMS Information

1. Description: Verify that the user can view all the information in the TYMS system.
2. Test Steps:
   - Launch the TYMS application.
   - Select the option to view TYMS information.
   - Verify that all the information is displayed correctly.
3. Expected Result: The TYMS information is displayed accurately in a tabular format.

### Case 2: Update Information in TYMS

1. Description: Ensure that the user can update information in the TYMS system.
2. Test Steps:
   - Launch the TYMS application.
   - Select the option to update information.
   - Enter the data to be searched for.
   - If found, provide a replacement value.
   - Verify that the value is updated correctly.
3. Expected Result: The specified information in the TYMS system is successfully updated.

### Case 3: Add New Information to TYMS

1. Description: Test the ability to add new information to the TYMS system.
2. Test Steps:
   - Launch the TYMS application.
   - Select the option to add new information.
   - Enter the data for each column as prompted.
   - Verify that the new row is added correctly.
3. Expected Result: The new information is added to the TYMS system accurately.

### Case 4: Delete Information from TYMS

1. Description: Verify the ability to delete information from the TYMS system.
2. Test Steps:
   - Launch the TYMS application.
   - Select the option to delete information.
   - Choose the row to be deleted.
   - Confirm the deletion.
   - Verify that the row is deleted correctly.
3. Expected Result: The specified row is successfully deleted from the TYMS system.

### Case 5: Invalid Input Handling

1. Description: Test the handling of invalid user inputs.
2. Test Steps:
   - Launch the TYMS application.
   - Enter invalid inputs such as non-numeric values or exceeding character limits.
   - Verify that appropriate error messages are displayed.
3. Expected Result: The TYMS application handles invalid user inputs gracefully by providing clear error messages.

### Case 6: Quitting the Application

1. Description: Ensure that the user can exit the TYMS application.
2. Test Steps:
   - Launch the TYMS application.
   - Choose the option to quit the application.
   - Verify that the application terminates successfully.
3. Expected Result: The TYMS application can be exited without any errors.

## Conclusion

The above test cases cover the major functionalities of the TYMS code. Performing these tests will help ensure that the code behaves as expected, handles inputs correctly, and maintains the integrity of the information in the TYMS system.

---

### Pep8 Validation

All python code was run through [PEP8 Python Validator](https://pep8ci.herokuapp.com/)  validator and any warnings or errors were fixed. Code then validated successfully.

![pep8](docs/testing/pep8_validator.png)
