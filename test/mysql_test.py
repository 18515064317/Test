
import mysql.connector
conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()
# cursor.execute('drop table user')
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#cursor.execute('insert into user (id,name) values(%s,%s)',['3','tomkhhj'])
cursor.execute('select * from user')
r = cursor.fetchall()
# cursor.rowcount
# conn.commit()
conn.close()
print(r)
a = []
for i in r:
    d = list(i)
    a.append(d)
print(a)

for i, v in enumerate(a):
    print('index = %s, value = %s'%(i,v))
    print("=================================\r")
    for j, k in enumerate(v):
        print('index = %s, value = %s' % (j, k))
#     print(r[i])