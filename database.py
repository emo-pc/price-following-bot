import sqlite3
import pandas as pd

def create_link():
    conn=sqlite3.connect("tracker.db")
    return conn

def create_table():
    conn=create_link()
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE,
            target_price REAL NOT NULL,
            current_price REAL
        )
    ''')

    conn.commit()
    conn.close()

def add_product(product_name,url,target_price,current_price=None):
    try:
        conn=create_link()
        cursor=conn.cursor()
        cursor.execute('''
            INSERT INTO products (product_name,url,target_price,current_price)
            VALUES (?,?,?,?)
        ''', (product_name,url,target_price,current_price))

        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_all_products():
    conn=create_link()
    df=pd.read_sql_query("SELECT * FROM products",conn)
    conn.close()
    return df

#########
##if __name__=="__main__":
##    print("database tables are being set")
##    create_table()
##    print("a product is being added")
##    add_product("Powerbank","https://amzn.eu/d/04QlQjuP",300.0)
##    print(get_all_products())
##