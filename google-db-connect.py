import pymysql

def connect_to_database():
    # Replace with your actual connection details
    connection = pymysql.connect(
        unix_socket='./cloudsql/cartcompanion-bc44dc2a32b1.json',  # Public IP of your Cloud SQL instance
        user='shrutika',    # Your MySQL username
        password='shrutika', # Your MySQL password
        database='cartcompanion'  # Your database name
    )
    
    try:
        with connection.cursor() as cursor:
            # Execute a sample query
            cursor.execute("SELECT VERSION();")
            result = cursor.fetchone()
            print("Database version:", result)
    finally:
        print('Connection Fail')
        connection.close()

if __name__ == "__main__":
    connect_to_database() 