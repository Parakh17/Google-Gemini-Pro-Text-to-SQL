import sqlite3

connection = sqlite3.connect("student.db")


cursor=connection.cursor()

table_info = """
Create table if not exists Student ( name varchar(25), class varchar(25), section varchar(25), marks int);
"""


cursor.execute(table_info)

cursor.execute("""INsert into student values("hritihk", "9", "b", 40)""")
cursor.execute("""insert into student values("parakh","12","a",90 )""")
cursor.execute("""Insert into student values("chavi","11","b",99)""")
cursor.execute("""insert into student values("shraddha", "5","d",96)""")
cursor.execute("""Insert into student values("yash","4","a",99)""")
cursor.execute("""insert into student values("harsh","8","f",44)""")

data=cursor.execute("""SELECT * FROM STUDENT WHERE MARKS > 90""")

for r in data:
    print(r)
#print(data) we cannot print this

connection.commit()
connection.close()



