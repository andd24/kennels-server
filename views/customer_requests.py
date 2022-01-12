CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct",
      "email": "hannah@mail.com"
    },
    {
      "id": 2,
      "name": "Dalton Tall",
      "address": "102 Lake Rd",
      "email": "dalton@mail.com"
    },
    {
      "id": 3,
      "name": "Darren Ball",
      "address": "99 Swiss Ln",
      "email": "darren@mail.com"
    },
    {
      "id": 4,
      "name": "Yusef",
      "address": "88 Dolan Way",
      "email": "yusef@mail.com"
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer  
    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer
  
def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
        
def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
        