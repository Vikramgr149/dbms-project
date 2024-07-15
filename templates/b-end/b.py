import mysql.connector

# Define the database connection parameters
username = 'root'
password = 'root123'
host = 'localhost'  # replace with your actual host
database = 'DBMS_PROJECT'

# Establish the connection
cnx = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database
)

# Create a cursor object to execute queries
cursor = cnx.cursor()

# Define a function to get column names for a table
def get_column_names(table_name):
    query = f"DESCRIBE {table_name}"
    cursor.execute(query)
    columns = [row[0] for row in cursor.fetchall()]
    return columns

# Define a function to manipulate table values
def manipulate_table_values(table_name, query):
    try:
        cursor.execute(query)
        cnx.commit()
        print(f"Successfully manipulated values in {table_name} table")
    except mysql.connector.Error as err:
        print(f"Error manipulating values in {table_name} table: {err}")

# Retrieve all values from all tables
tables = [
    'login',
    'User',
    'Patient',
    'Donor',
    'Organ_available',
    'Organization',
    'Doctor',
    'Organization_head',
    'Organization_phone_no',
    'Doctor_phone_no',
    'user_phone_no',
    'Transaction',
    'log'
]

for table in tables:
    query = f"SELECT * FROM {table}"
    cursor.execute(query)
    rows = cursor.fetchall()
    print(f"Values in {table} table:")
    for row in rows:
        print(row)

# Manipulate values in all tables
for table in tables:
    # Insert a new row into each table
    columns = get_column_names(table)
    query = f"INSERT INTO {table} VALUES ({', '.join(['NULL'] * len(columns))})"
    manipulate_table_values(table, query)

    # Update a row in each table
    query = f"UPDATE {table} SET {columns[0]} = 'Updated value' WHERE {columns[0]} = 'Old value'"
    manipulate_table_values(table, query)

    # Delete a row from each table
    query = f"DELETE FROM {table} WHERE {columns[0]} = 'Value to delete'"
    manipulate_table_values(table, query)

cursor.execute("insert into User(user_id, name, date_of_birth, medical_insurance, medical_history, street, city, state) values (%s, %s, %s, %s, %s, %s, %s, %s)",
               (100, "name-100", '1978-09-09', 1, None, "Street-1", "New Delhi", "Delhi"))

# Close the cursor and connection
cursor.close()
cnx.close()