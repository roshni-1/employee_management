import mysql.connector
from tkinter import *
from tkinter import messagebox
from faker import Faker

# Establish a connection to the MySQL database

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee_management_new"
)


# Create a cursor object to interact with the database
cursor = conn.cursor()

# Initialize Faker instance
fake = Faker()

# Function to add employee data to the database
def add_employee():
    # Generate fake employee data
    employee_name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.address()
    department = fake.random_element(elements=('IT', 'Sales', 'Marketing', 'Finance'))
    performance = fake.random_int(min=1, max=5)
    salary = fake.random_int(min=30000, max=80000)

    # SQL query to insert data
    sql = """
    INSERT INTO employees (EmployeeName, Email, PhoneNumber, Address, Department, Performance, Salary)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    # Data values as a tuple
    data = (employee_name, email, phone_number, address, department, performance, salary)

    try:
        # Execute the query with the data tuple
        cursor.execute(sql, data)
        # Commit the transaction
        conn.commit()
        messagebox.showinfo("Success", "Employee data added successfully!")
    except Exception as e:
        # Handle any errors that occur during insertion
        messagebox.showerror("Error", f"Failed to add employee data: {e}")

# Function to view employee details
def view_employee():
    # Get EmployeeID from the user input
    employee_id = entry_employee_id.get()

    # SQL query to retrieve employee data
    sql = f"SELECT * FROM employees WHERE EmployeeID = {employee_id}"

    # Execute the query
    cursor.execute(sql)
    employee_data = cursor.fetchone()

    # Display employee details in the GUI
    text_output.delete(1.0, END)
    if employee_data:
        text_output.insert(END, f"Employee ID: {employee_data[0]}\n")
        text_output.insert(END, f"Employee Name: {employee_data[1]}\n")
        text_output.insert(END, f"Email: {employee_data[2]}\n")
        text_output.insert(END, f"Phone Number: {employee_data[3]}\n")
        text_output.insert(END, f"Address: {employee_data[4]}\n")
        text_output.insert(END, f"Department: {employee_data[5]}\n")
        text_output.insert(END, f"Performance: {employee_data[6]}\n")
        text_output.insert(END, f"Salary: {employee_data[7]}\n")
    else:
        text_output.insert(END, "Employee not found!")

# Create the Tkinter application window
root = Tk()
root.title("Employee Management System")

# Labels and Entry for EmployeeID input
label_employee_id = Label(root, text="Enter Employee ID:")
label_employee_id.pack()

entry_employee_id = Entry(root)
entry_employee_id.pack()

# Button to view employee details
button_view = Button(root, text="View Employee", command=view_employee)
button_view.pack()

# Text widget to display employee details
text_output = Text(root, height=10, width=50)
text_output.pack()

# Button to add employee data
button_add_employee = Button(root, text="Add Employee", command=add_employee)
button_add_employee.pack()

# Run the Tkinter main loop
root.mainloop()

# Close the cursor and connection after the application window is closed
cursor.close()
conn.close()
