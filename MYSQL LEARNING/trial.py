import csv
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Database connection configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': ''  # Initially set to empty, as we create the database first
}

def create_db_connection(db_name=None):
    try:
        # If db_name is provided, use it to connect to the specific database
        if db_name:
            DB_CONFIG['database'] = db_name
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database():
    connection = create_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            create_db_query = "CREATE DATABASE IF NOT EXISTS STUDENTDETAILS;"
            cursor.execute(create_db_query)
            connection.commit()
            print("Database 'STUDENTDETAILS' created successfully.")
        except Error as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()
            connection.close()

def create_CLASS7_table():
    connection = create_db_connection('STUDENTDETAILS')
    if connection:
        try:
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS CLASS7 (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(15),
                rollno INT,
                branch VARCHAR(3),
                grade VARCHAR(1)
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
            print("class7 table created successfully in STUDENTDETAILS database.")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            cursor.close()
            connection.close()

def import_data_to_db(data):
    connection = create_db_connection('STUDENTDETAILS')
    if connection:
        try:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO CLASS7 (NAME, ROLLNO, BRANCH, GRADE)
            VALUES (%s, %s, %s, %s);
            """

            # Get current timestamp for createdat and updatedat columns
            current_time = datetime.now()

            # Loop through the provided data and insert each record into the database
            for row in data:
                cursor.execute(insert_query, (
                     row['name'], row['rollno'], row['branch'], row['grade']
                ))

            connection.commit()
            print("Data imported successfully into the database.")
        except Error as e:
            print(f"Error importing data: {e}")
        finally:
            cursor.close()
            connection.close()

def delete_the_data_from_db(rollno):
    connection = create_db_connection('STUDENTDETAILS')
    if connection:
        try:
            cursor = connection.cursor()
            delete_query = "DELETE FROM CLASS7 WHERE ROLLNO = %s;"
            cursor.execute(delete_query, (rollno,))
            connection.commit()
            print(f"Student with rollno {rollno} deleted successfully.")
        except Error as e:
            print(f"Error deleting data: {e}")
        finally:
            cursor.close()
            connection.close()

def get_input_for_insertion():
    row={}
    name=input("Enter the name: ")
    rollno=int(input("Enter the rollno:"))
    branch=input("Enter the branch: ")
    grade=input("Enter the overall grade: ")
    row["name"]=name
    row["rollno"]=rollno
    row["branch"]=branch
    row["grade"]=grade
    return row

def update_the_data_in_db(rollno):
    connection = create_db_connection('STUDENTDETAILS')
    if connection:
        try:
            cursor = connection.cursor()
            # Prompt user for new details to update
            print("Enter the new details to update:")
            new_name = input("Enter new name: ")
            new_branch = input("Enter new branch: ")
            new_grade = input("Enter new grade: ")

            # Update query
            update_query = """
            UPDATE CLASS7
            SET NAME = %s, BRANCH = %s, GRADE = %s
            WHERE ROLLNO = %s;
            """
            cursor.execute(update_query, (new_name, new_branch, new_grade, rollno))
            connection.commit()

            # Check if any row was updated
            if cursor.rowcount > 0:
                print(f"Student with rollno {rollno} updated successfully.")
            else:
                print(f"No student found with rollno {rollno}.")

        except Error as e:
            print(f"Error updating data: {e}")
        finally:
            cursor.close()
            connection.close()



if __name__ == "__main__":
    # Create the AIGUARD database if not already exists
    # create_database()

    # Create the firewalllogs table within the AIGUARD database
    # create_CLASS7_table()

    
    while True:
        print("1. Insert data \n2. Delete the data \n3.Update the data \n4.Exit")
        choice = int(input("Enter the operation you want to perform on the db: "))
        if choice==1:
            data=[]
            data.append(get_input_for_insertion())
            import_data_to_db(data)
        elif choice==2:
            id=int(input("Enter the rollno for deletion: "))
            delete_the_data_from_db(id)
        elif choice==3:
            id=int(input("Enter the roll no for updation: "))
            update_the_data_in_db(id)
        elif choice==4:
            break
        else:
            print("Invalid choice, Try again")
