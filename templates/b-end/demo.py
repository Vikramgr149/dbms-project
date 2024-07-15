from flask import Flask, jsonify
import mysql.connector

# Initialize the Flask app
app = Flask(__name__)

# Connect to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="DBMS_PROJECT"
)

# Create a cursor object
cursor = cnx.cursor()

# Define a route to return the login table
@app.route("/login")
def get_login():
    cursor.execute("SELECT * FROM login")
    rows = cursor.fetchall()
    return jsonify(rows)

# Define a route to insert a new user
@app.route("/user", methods=["POST"])
def add_user():
    user_id = request.json["User_ID"]
    name = request.json["Name"]
    date_of_birth = request.json["Date_of_Birth"]
    medical_insurance = request.json["Medical_insurance"]
    medical_history = request.json["Medical_history"]
    street = request.json["Street"]
    city = request.json["City"]
    state = request.json["State"]

    cursor.execute("""
        INSERT INTO User VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    """, (user_id, name, date_of_birth, medical_insurance, medical_history, street, city, state))

    cnx.commit()

    return jsonify({"message": "User added"})

# Define a route to insert a new patient
@app.route("/patient", methods=["POST"])
def add_patient():
    patient_id = request.json["Patient_ID"]
    organ_req = request.json["organ_req"]
    reason_of_procurement = request.json["reason_of_procurement"]
    doctor_id = request.json["Doctor_ID"]
    user_id = request.json["User_ID"]

    cursor.execute("""
        INSERT INTO Patient VALUES(%s, %s, %s, %s, %s)
    """, (patient_id, organ_req, reason_of_procurement, doctor_id, user_id))

    cnx.commit()

    return jsonify({"message": "Patient added"})

# Define a route to insert a new donor
@app.route("/donor", methods=["POST"])
def add_donor():
    donor_id = request.json["Donor_ID"]
    organ_donated = request.json["organ_donated"]
    reason_of_donation = request.json["reason_of_donation"]
    organization_id = request.json["Organization_ID"]
    user_id = request.json["User_ID"]

    cursor.execute("""
        INSERT INTO Donor VALUES(%s, %s, %s, %s, %s)
    """, (donor_id, organ_donated, reason_of_donation, organization_id, user_id))

    cnx.commit()

    return jsonify({"message": "Donor added"})

# Define a route to insert a new transaction
@app.route("/transaction", methods=["POST"])
def add_transaction():
    patient_id = request.json["Patient_ID"]
    organ_id = request.json["Organ_ID"]
    donor_id = request.json["Donor_ID"]
    date_of_transaction = request.json["Date_of_transaction"]
    status = request.json["Status"]

    cursor.execute("""
        INSERT INTO Transaction VALUES(%s, %s, %s, %s, %s""")