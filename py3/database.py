
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='cv7511jj',
                             password='#Movingon2022#',
                             db='cv7511jj_newUniversity',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        x = input("Please enter a last name:")
        sql = "SELECT * from Student WHERE lName = %s "


        # execute the SQL command
        cursor.execute(sql, x)
        
        # get the results
        for result in cursor:

             print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()

