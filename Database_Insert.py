import mysql.connector as mc
conn_bds=mc.connect(user="root",password="",host="localhost",database="data")
cursor_bds=conn_bds.cursor()

def user_insert(tup):
    try:
        cursor_bds.execute("insert into bds(name,RegNo,BloodGroup,PhoneNo) values(%s,%s,%s,%s)",tup)
        conn_bds.commit()
        return True
    except:
        return False

def show_details():
    cursor_bds.execute("select * from bds")
    return cursor_bds.fetchall()
def delete_details(tup):
    cursor_bds.execute("delete from bds where RegNo=%s", tup)
    conn_bds.commit()
    return True
def update_details(tup):
    cursor_bds.execute("update bds set name=%s,RegNo=%s,BloodGroup=%s,PhoneNo=%s where RegNo=%s",tup)
    conn_bds.commit()
    return True

def search_details(tup):
    cursor_bds.execute("select * from bds where  RegNo=%s",tup)
    return cursor_bds.fetchall()

def search_details_bg(tup):
    cursor_bds.execute("select * from bds where  bloodGroup=%s",tup)
    return cursor_bds.fetchall()

def get_name():
    cursor_bds.execute("select name from bds")
    return cursor_bds.fetchall()


def get_regno():
    cursor_bds.execute("select RegNo from bds")
    return cursor_bds.fetchall()
