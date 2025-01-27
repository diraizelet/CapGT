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
            create_db_query = "CREATE DATABASE IF NOT EXISTS AIGUARD;"
            cursor.execute(create_db_query)
            connection.commit()
            print("Database 'AIGUARD' created successfully.")
        except Error as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()
            connection.close()

def create_firewalllogs_table():
    connection = create_db_connection('AIGUARD')
    if connection:
        try:
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS firewalllogs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp DATETIME,
                ip VARCHAR(15),
                port INT,
                traffic_type VARCHAR(50),
                action VARCHAR(50),
                createdat DATETIME DEFAULT CURRENT_TIMESTAMP,
                updatedat DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
            print("Firewall logs table created successfully in AIGUARD database.")
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            cursor.close()
            connection.close()

def import_csv_to_db(csv_file_path):
    connection = create_db_connection('AIGUARD')
    if connection:
        try:
            cursor = connection.cursor()
            insert_query = """
            INSERT INTO firewalllogs (timestamp, ip, port, traffic_type, action, createdat, updatedat)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
            """

            # Get current timestamp for createdat and updatedat columns
            current_time = datetime.now()

            # Open CSV file and insert data into the database
            with open(csv_file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    # Extract data from CSV row and insert into DB
                    cursor.execute(insert_query, (
                        row['timestamp'], row['ip'], row['port'], row['traffic_type'], row['action'],
                        current_time, current_time
                    ))

            connection.commit()
            print(f"Data from {csv_file_path} imported successfully into the database.")
        except Error as e:
            print(f"Error importing CSV data: {e}")
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    # Create the AIGUARD database if not already exists
    create_database()

    # Create the firewalllogs table within the AIGUARD database
    create_firewalllogs_table()

    # Specify the path to your CSV file
    csv_file_path = "D:\\Unityprojects\\CapGT\\MYSQL LEARNING\\firewall_logs.csv"
 # Change this path if needed

    # Import CSV data into the database
    import_csv_to_db(csv_file_path)

    


# import csv
# import mysql.connector
# from mysql.connector import Error

#                 # Commit the transaction after all rows are inserted
#                 connection.commit()
#                 print(f"{cursor.rowcount} records inserted successfully.")

#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         # Close the database connection
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("Connection closed.")


# if __name__ == "__main__":
#     db_config = {
#         'host': 'localhost',  # Database host
#         'user': 'root',       # Database username
#         'password': '1234',  # Database password
#         'database': 'AIGUARD'  # Database name
#     }
#     upload_csv_to_db('firewall_logs.csv', db_config)