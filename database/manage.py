""""Module providing function to database connection"""
import sqlite3


def connect():
    """Function to create the database connection"""
    return sqlite3.connect("app.db")


def close_connection(conn):
    """Function to close the database connection"""
    conn.close()


def execute_query(query, params=()):
    """Function to execute a sql query and commit the action"""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()


def fetch_results(query, params=()):
    """Function to execute a sql query and fetch the results"""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results


def table_exists(table_name):
    """Function to validate if a table exists"""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists


def count_rows(table_name):
    """Function to count the number of records in a table"""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    conn.close()
    return count
