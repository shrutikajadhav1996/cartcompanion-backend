import mysql.connector
import MySQLdb
from mysql.connector import Error
import sys
import pymysql


def get_db_connection():
    # Replace with your actual connection details
    cnx = pymysql.connect(
        # unix_socket='cartcompanion:us-central1:cartcompanion-db',  # Public IP of your Cloud SQL instance
        host= '34.28.129.223', #='./cloudsql/cartcompanion-bc44dc2a32b1.json',  # Public IP of your Cloud SQL instance
        user='shrutika',    # Your MySQL username
        password='shrutika', # Your MySQL password
        db='cartcompanion'  # Your database name
    )
    
    try:
        with cnx.cursor() as cursor:
            # Execute a sample query
            cursor.execute("SELECT VERSION();")
            result = cursor.fetchone()
            print("Database version:", result)

            return cnx
    except Exception as e:
        print(f'Connection Fail : {e}')
        # cnx.close()

# def get_db_connection():
#     # Replace these values with your Cloud SQL instance details
#     db_user = "shrutika"
#     db_password = "shrutika"
#     db_name = "cartcompanion"
#     db_connection_name = "cartcompanion:us-central1:cartcompanion-db"
# #     db_connection_name = "cartcompanion-430417:us-east1:cartcompanion-db"

#     try:
#         cnx = mysql.connector.connect(
#                 user=db_user,
#                 password=db_password,
#                 database=db_name,
#                 host=f'/cloudsql/{db_connection_name}'
#             )

#         if cnx.is_connected():
#                 print("Successfully connected to the database.")
#         return cnx
#     except Error as e:
#         print(f"Error while connecting to MySQL: {e}")
#         sys.exit()
#     # except Error as err:
#     #    print(f"Error: '{err}'")
#     #    return None


# def get_db_connection():
# #    cnx = mysql.connector.connect(
#    cnx = MySQLdb.connect(
#        host="localhost",
#        user="root",
#        password="root",
#        database="cartcompanion",
#        auth_plugin="mysql_native_password"
#    )
#    return cnx

#def get_db_connection():
#    cnx = mysql.connector.connect(
#        host="34.28.129.223",
#       user="shrutika",
#       password="shrutika",
#       database="cartcompanion",
#       auth_plugin="mysql_native_password"
#   )
#   return cnx


def insert_order_item(order_id, dress_id, quantity, a_price):
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "INSERT INTO ordertable (OrderId, DressId, Quantity, TotalPrice) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (order_id, dress_id, quantity, a_price))
        cnx.commit()
        return 0
    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")
        cnx.rollback()
        return -1
    finally:
        cursor.close()
        cnx.close()


def insert_order_tracking(order_id, status):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    query = "INSERT INTO trackingtable (OrderId, Status) VALUES (%s, %s)"
    cursor.execute(query, (order_id, status))
    cnx.commit()
    cursor.close()


def insert_order_summury(order_id, total_order_price):
    cnx = get_db_connection()
    cursor = cnx.cursor()
    query = "INSERT INTO order_summury (OrderId, Total_Price) VALUES (%s, %s)"
    cursor.execute(query, (order_id, total_order_price))
    cnx.commit()
    cursor.close()


def get_dress_id(dresstype, size, gender):
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "SELECT DressId FROM dress WHERE DressType = %s AND Dress = %s AND Gender = %s"
        cursor.execute(query, (dresstype, size, gender))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error finding your order item: {err}")
        return None
    finally:
        cursor.close()
        cnx.close()


def get_dress_price(dress_id):
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = f"SELECT price FROM dress WHERE DressId = {dress_id}"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except mysql.connector.Error as err:
        return None
    finally:
        cursor.close()
        cnx.close()


def get_total_order_price(order_id):
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "SELECT SUM(a_price) FROM ordertable WHERE OrderId = %s"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error calculating order total price: {err}")
        return None
    finally:
        cursor.close()
        cnx.close()


def get_next_order_id():
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "SELECT MAX(OrderId) FROM ordertable"
        cursor.execute(query)
        result = cursor.fetchone()
        if result[0] is None:
            return 1
        else:
            return result[0] + 1
    except mysql.connector.Error as err:
        print(f"Error inserting order item: {err}")
        return None
    finally:
        cursor.close()
        cnx.close()


def get_order_status(order_id):
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "SELECT status FROM trackingtable WHERE OrderId = %s"
        cursor.execute(query, (order_id,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except mysql.connector.Error as err:
        print(f"Error finding next order ID: {err}")
        return None
    finally:
        cursor.close()
        cnx.close()
print(get_dress_id('Yellow Short Dress', 'small', 'women'))


