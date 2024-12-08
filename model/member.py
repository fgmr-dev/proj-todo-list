# model/team_db.py
from datetime import datetime
import database.manage as manage


def fetch_users():
    """Function to fetch data for members"""
    query = """
    SELECT users.id, users.name, users.email, users.created_date, statuses.description
    FROM users
    LEFT JOIN statuses ON users.status = statuses.id
    """
    users = manage.fetch_results(query)

    return users


def add_user(name, email):
    """Function to insert data for members"""
    conn = manage.connect()
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO users (name, email, created_date, status) VALUES (?, ?, ?, ?)
    """,
        (name, email, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 1),
    )

    user_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return user_id


def get_user(user_id):
    """Function to get data for one member"""
    conn = manage.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT name, email FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    return user


def update_user(user_id, name, email, status=1):
    """Function to update data for members"""
    conn = manage.connect()
    cursor = conn.cursor()

    cursor.execute(
        """
    UPDATE users SET name = ?, email = ?, status = ? WHERE id = ?
    """,
        (name, email, status, user_id),
    )

    conn.commit()
    conn.close()


def delete_user(user_id):
    """Function to delete data for members"""
    conn = manage.connect()
    cursor = conn.cursor()

    cursor.execute(
        """
    UPDATE users SET status = 2 WHERE id = ?
    """,
        (user_id,),
    )

    conn.commit()
    conn.close()
