# Employee Management System

The Employee Management System is a simple desktop application built using Python and MySQL. It allows users to add new employees and view their details, including performance metrics, growth plans, and feedback suggestions.

## Features

- **Add Employee:** Add new employees to the database with randomly generated data.
- **View Employee:** View employee details including performance metrics, growth plans, and feedback suggestions based on their performance.

## Requirements

- Python 3.x
- MySQL Server

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/employee-management-system.git
    ```

2. **Install required packages:**

    ```bash
    pip install mysql-connector-python faker
    ```

3. **Configure MySQL Database:**
   
   - Create a new database named `employee_management_new`.
   - Import the SQL schema provided in `database_schema.sql` to create the necessary table.

4. **Run the application:**

    ```bash
    python employee_management.py
    ```

## Usage

1. **Add Employee:**
   
   - Click on the "Add Employee" button to add a new employee to the database with random data.

2. **View Employee:**
   
   - Enter the Employee ID in the input field.
   - Click on the "View Employee" button to view the employee details, growth plan, and feedback suggestions based on their performance.



