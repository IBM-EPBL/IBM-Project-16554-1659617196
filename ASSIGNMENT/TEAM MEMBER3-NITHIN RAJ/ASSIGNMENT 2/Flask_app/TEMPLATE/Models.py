import curses
import sqlite3 as sql

def retrieveUsers():
    con = sql.connect("user_database.db")
    con = con.cursor()
    curses.execute("SELECT username, pin FROM users")
    users = curses.fetchone()
    con.close()
    return users
