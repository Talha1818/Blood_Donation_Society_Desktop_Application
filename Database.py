import mysql.connector as mc
conn_login=mc.connect(user="root",password="",host="localhost",database="data")

cursor_login=conn_login.cursor()


def user_login(tup):
    try:
      cursor_login.execute("select * from login where username=%s and password=%s",tup)
      return (cursor_login.fetchone())
    except:
        return False


def search_record(tup):
    try:
        cursor_login.execute("select * from login where username=%s",tup)
        return (cursor_login.fetchall())
    except:
        return False


