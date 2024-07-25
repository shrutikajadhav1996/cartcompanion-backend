import pymysql


def connect_to_mysql(host, user, password, database):
    try:
        # Establish a connection to the MySQL database
        connection = pymysql.connect(host=host, user=user, password=password, database=database)

        with connection.cursor() as cursor:
            print("Connected to MySQL database")

            # Example query
            cursor.execute("SELECT DATABASE();")
            database_name = cursor.fetchone()
            print(f"Connected to database: {database_name[0]}")

            # Execute another query
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            print("Tables in the database:")
            for table in tables:
                print(table[0])

    except pymysql.MySQLError as e:
        print(f"Error: {e}")
    finally:
        connection.close()
        print("MySQL connection is closed")


if __name__ == "__main__":
    # Replace with your MySQL instance credentials
    HOST ='34.28.129.223'
    USER = "shrutika"
    PASSWORD = "shrutika"
    DATABASE = "cartcompanion"

    connect_to_mysql(HOST, USER, PASSWORD, DATABASE)
