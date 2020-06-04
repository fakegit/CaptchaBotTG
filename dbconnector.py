import sqlite3
#create connect to db - ContainerUsers.db - it's name database
conn = sqlite3.connect('ContainerUsers.db')
#create cursor for work with rows in db
c = conn.cursor()

#Edit db
def edit(query):
    c.execute(query)
    conn.commit()

#Get data from db
def select(query):
    c.execute(query)
    return c.fetchall()

#Get info if result from query contains need row value
def Get_Lenght(query):
    result=c.execute(query)
    if len(c.fetchall())>0:
        return True
    else:
        return False