import mysql.connector

# Define the database connection parameters
username = 'root'
password = 'root123'
host = 'localhost'
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

# Retrieve data from all tables
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
    results = cursor.fetchall()
    print(f"Table: {table}")
    for row in results:
        print(row)
    print()

# Close the cursor and connection
cursor.close()
cnx.close()