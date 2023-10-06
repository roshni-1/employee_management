import random
from faker import Faker
import csv

# Initialize Faker to generate fake data
fake = Faker()

# Number of employees
num_employees = 500

# Generate sample data for employees
employees = []
for _ in range(num_employees):
    employee_id = fake.unique.random_int(min=1001, max=9999)
    employee_name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    department = fake.random_element(elements=('IT', 'Sales', 'Marketing', 'HR'))
    performance = round(random.uniform(1, 10), 2)  # Random performance score between 1 and 10
    salary = round(random.uniform(30000, 120000), 2)  # Random salary between $30,000 and $120,000
    hiring_date = fake.date_this_century(before_today=True, after_today=False).strftime('%Y-%m-%d')
    job_title = fake.job()
    work_experience = random.randint(1, 20)  # Random work experience in years (1 to 20 years)
    current_task = fake.random_element(elements=('Working on Project A', 'Meeting with Client', 'Coding', 'Research'))
    idle_time_hours = round(random.uniform(0, 5), 2)  # Random idle time in hours (0 to 5 hours)

    employees.append([employee_id, employee_name, email, phone_number, address, department, performance, salary,
                      hiring_date, job_title, work_experience, current_task, idle_time_hours])

# Write data to CSV file
with open('employees_data1.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['EmployeeID', 'EmployeeName', 'Email', 'PhoneNumber', 'Address', 'Department', 'Performance', 'Salary',
                         'HiringDate', 'JobTitle', 'WorkExperience', 'CurrentTask', 'IdleTimeHours'])
    csv_writer.writerows(employees)

print("Sample employee data has been generated and saved to 'employees_data.csv'.")
