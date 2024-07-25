import mysql.connector
import MySQLdb
from mysql.connector import Error
import sys
import pymysql


def get_db_connection():
   
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




def insert_order_item(order_id, dress_id, quantity, a_price):   #add to cart
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "INSERT INTO ordertable (OrderID, DressID, Quantity, TotalPrice) VALUES (%s, %s, %s, %s)"
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


def insert_order_tracking(order_id, status):  #track order
    cnx = get_db_connection()
    cursor = cnx.cursor()
    query = "INSERT INTO trackingtable (OrderID, Status) VALUES (%s, %s)"
    cursor.execute(query, (order_id, status))
    cnx.commit()
    cursor.close()


def insert_order_summury(order_id, total_order_price):  #purchase order
    cnx = get_db_connection()
    cursor = cnx.cursor()
    query = "INSERT INTO order_summury (OrderID, Total_Price) VALUES (%s, %s)"
    cursor.execute(query, (order_id, total_order_price))
    cnx.commit()
    cursor.close()


def get_dress_id(dresstype, size, gender): #accessing dress id
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "SELECT DressID FROM dress WHERE DressType = %s AND Dress = %s AND Gender = %s"
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


def get_dress_price(dress_id):   #for dress price
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "SELECT Price FROM dress WHERE DressID = %s"
        cursor.execute(query, (dress_id,))
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


def get_total_order_price(order_id):   # total amount of order
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "SELECT SUM(TotalPrice) FROM ordertable WHERE OrderID = %s"
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


def get_next_order_id():    #assign next order id to newly added oredr
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "SELECT MAX(OrderID) FROM ordertable"
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


def get_order_status(order_id): #track status
    cnx = get_db_connection()
    cursor = cnx.cursor()

    try:
        query = "SELECT status FROM trackingtable WHERE OrderID = %s"
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


