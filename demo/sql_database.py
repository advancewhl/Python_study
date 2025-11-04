import pymysql
# 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='whl123lrh',
    charset='utf8')
# 创建游标
cursor = conn.cursor()

# # 发送指令

# 1查看数据库
cursor.execute("show databases;")
# 获取结果
databases = cursor.fetchall()
print(databases)

# 2创建数据库（新增、删除、修改）
cursor.execute("create database if not exists testdb;")
# cursor.execute("create database db3 default charset utf8 collate utf8_general_ci;")
conn.commit()  # 提交更改

# 3查看数据库
cursor.execute("show databases;")
databases = cursor.fetchall()
print(databases)

# 4删除数据库 
cursor.execute("drop database testdb;")
conn.commit()  # 提交更改

cursor.execute("show databases;")
databases = cursor.fetchall()
print(databases)

# 5进入数据库
cursor.execute("use mysql;")
cursor.execute("show tables;")
databases = cursor.fetchall()
print(databases)

# 6关闭连接
cursor.close()
conn.close()