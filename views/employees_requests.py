import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Bakker",
      "locationId": 2,
      "status": "Active"
    },
    {
      "id": 2,
      "name": "Tanya Rene",
      "locationId": 1,
      "status": "Active"
    },
    {
      "id": 3,
      "name": "Kayla Gill",
      "locationId": 2,
      "status": "Active"
    },
    {
      "id": 4,
      "name": "Jeff Coly",
      "locationId": 1,
      "status": "Active"
    },
    {
      "name": "Boo",
      "locationId": 1,
      "id": 5,
      "status": "Active"
    }
]

def get_all_employees2():
    return EMPLOYEES

def get_single_employee2(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee  
    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee
  
def delete_employee(id):
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
        
def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break

def get_all_employees():
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        employee = Employee(data['id'], data['name'], data['address'], data['location_id'])

        return json.dumps(employee.__dict__)