import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='whl123lrh',
    charset='utf8')

cursor = conn.cursor()
cursor.execute("create database if not exists testbase;")
conn.commit()
cursor.execute("use testbase;")
cursor.execute("show tables;")
databases = cursor.fetchall()
print(databases)
cursor.execute("drop table if exists student")
conn.commit()
cursor.execute("create table if not exists student("
               "id int not null auto_increment primary key, "
               "email varchar(20), "
               "name varchar(20) null,"
               "age int default 18"
               ") default charset=utf8;")
conn.commit()
cursor.execute("show tables;")
databases = cursor.fetchall()
print(databases)

# cursor.execute("drop table student")
# cursor.execute("delete from student")
cursor.execute("desc student")
# for row in cursor.fetchall():
#     print(row)
cursor.execute("alter table student add high int not null default 170")
cursor.execute("desc student")
conn.commit()
for row in cursor.fetchall():
    print(row)



