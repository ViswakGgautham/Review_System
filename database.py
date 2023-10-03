import mysql.connector as mysql
con = mysql.connect(host='localhost',password='password',database='feedback',user='root')
cursor=con.cursor()
def insert(box,text):
    querry=f'insert into feedback1 values("{box}","{text}");'
    cursor.execute(querry)
    con.commit()
def count():
    querry='select count(*) from feedback1 where option="green"'
    cursor.execute(querry)
    green=cursor.fetchall()[0][0]
    querry = 'select count(*) from feedback1 where option="red"'
    cursor.execute(querry)
    red=cursor.fetchall()[0][0]
    querry = 'select count(*) from feedback1 where option="amber"'
    cursor.execute(querry)
    amber = cursor.fetchall()[0][0]
    t=(green,amber,red)
    return t
def comments():
    l=[]
    querry='select description from feedback1;'
    cursor.execute(querry)
    data=cursor.fetchall()
    for i in data:
        for j in i:
            l.append(j)
    return l
