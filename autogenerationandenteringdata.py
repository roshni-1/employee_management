import mysql.connector
from faker import Faker  # For generating fake data
import random
import json
from datetime import date


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

# Number of employees to generate
num_employees = 1000

for _ in range(num_employees):
    # Generate fake employee data
    employee_name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.address()
    department = fake.random_element(elements=('IT', 'Sales', 'Marketing', 'Finance','Accounts','PR','Legal','Customer Service'))
    performance = random.choice([4.5, 4.0, 3.5, 3.0, 2.5,3.2,6.8,5.5,8.8,9.0,10.0,1.0,7.0,8.1,5.1,6.2,3.4])
    salary = fake.random_int(min=30000, max=900000)
    hiring_date = fake.date_between(start_date='-9y', end_date='today')
    job_title = fake.job()
    work_experience = fake.random_int(min=1, max=20)
    current_task = fake.random_element(elements=('Working on Project A', 'Meeting with Client', 'Coding', 'Research','Testing','Accounting','Documentation','Working on Project B','Working on Project C'))
    training_completed = fake.random_int(min=0, max=30)
    certifications = fake.random_int(min=0, max=15)
    projects_completed = fake.random_int(min=0, max=20)
    positive_feedback_count = fake.random_int(min=0, max=50)
    innovative_ideas_submitted = fake.random_int(min=0, max=30)
    mentorship_status = fake.random_element(elements=('Active', 'Inactive'))
    workshops_attended = fake.random_int(min=0, max=10)
    customer_satisfaction_rating = random.choice([4.5, 4.0, 3.5, 3.0, 2.5, 2.0,3.2,4.4,2.8,5.0,2.2,1.9,1.5])
    team_project_success = fake.random_element(elements=(0, 1))

    # SQL query to insert data
    sql = """
    INSERT INTO employees (EmployeeName, Email, PhoneNumber, Address, Department, Performance, Salary, HiringDate, JobTitle, WorkExperience, CurrentTask,
                            TrainingCompleted, Certifications, ProjectsCompleted, PositiveFeedbackCount, InnovativeIdeasSubmitted, MentorshipStatus,
                            WorkshopsAttended, CustomerSatisfactionRating, TeamProjectSuccess)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    # Data values as a tuple
    data = (employee_name, email, phone_number, address, department, performance, salary, hiring_date, job_title, work_experience, current_task,
            training_completed, certifications, projects_completed, positive_feedback_count, innovative_ideas_submitted, mentorship_status,
            workshops_attended, customer_satisfaction_rating, team_project_success)

    try:
        # Execute the query with the data tuple
        cursor.execute(sql, data)
        # Commit the transaction
        conn.commit()
    except Exception as e:
        # Handle any errors that occur during insertion
        print(f"Error: {e}")

# Close the cursor and connection
cursor.close()
conn.close()

print(f"{num_employees} employees' data inserted successfully!")
