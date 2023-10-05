import mysql.connector as mysql
con = mysql.connect(host='localhost',password='password',database='feedback',user='root')
cursor=con.cursor()
def insert(class1,box,text):
    querry=f'insert into feedback1 values("{box}","{text}","{class1}");'
    cursor.execute(querry)
    con.commit()
def count(id):
    querry=f'select count(*) from feedback1 where option="green" and classID="{id}"'
    cursor.execute(querry)
    green=cursor.fetchall()[0][0]
    querry = f'select count(*) from feedback1 where option="red" and classID="{id}"'
    cursor.execute(querry)
    red=cursor.fetchall()[0][0]
    querry = f'select count(*) from feedback1 where option="amber" and classID="{id}"'
    cursor.execute(querry)
    amber = cursor.fetchall()[0][0]
    t=(green,amber,red)
    return t
def comments(id):
    l=[]
    querry=f'select description from feedback1 where classID="{id}";'
    cursor.execute(querry)
    data=cursor.fetchall()
    for i in data:
        for j in i:
            l.append(j)
    return l
def insert_class(id,no,year):
    query=f'insert into classes values("{id}",{no},{year})'
    cursor.execute(query)
    con.commit()
def classnames():
    l=[]
    querry='select class from classes'
    cursor.execute(querry)
    data=cursor.fetchall()
    for i in data:
        for j in i:
            l.append(j)
    return l



