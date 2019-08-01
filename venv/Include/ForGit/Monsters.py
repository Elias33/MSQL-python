import pymysql
connection= pymysql.connect(host="localhost", user="root", passwd="", db="mydb")
myCursor= connection.cursor()
'''
myCursor.execute("""create table detail 

(
    id int primary key,
    name varchar (20)
    

)""")
'''

'''
myCursor.execute("insert into detail(id,name) values(2, 'elias');")
'''

'''
myCursor.execute("update detail set name='lol' where id=2;")


print("Data insert succesfully")
'''

myCursor.execute("delete from detail where id=2;")
print("Delete done")






connection.commit()
connection.close()
