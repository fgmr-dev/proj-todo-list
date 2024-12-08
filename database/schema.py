# model/schema.py
from database.manage import connect


def create_tables():
    """Function to create the application data model"""
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS MEMBER_STATUS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS MEMBER (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        created_date TEXT NOT NULL,
        status_id INTEGER,
        FOREIGN KEY(status_id) REFERENCES MEMBER_STATUS(id)
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS TASK_STATUS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS TASK (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        created_date TEXT NOT NULL,
        status_id INTEGER NOT NULL,
        schedule_id INTEGER,
        FOREIGN KEY(status_id) REFERENCES MEMBER_STATUS(id)
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS TASK_SCHEDULE (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER,
        frequency TEXT NOT NULL,
        interval INTEGER
        days_week TEXT,
        status INTEGER,
        start_date DATE,
        end_date DATE
    )
    """
    )

    conn.commit()
    conn.close()
