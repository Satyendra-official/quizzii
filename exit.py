import mysql.connector as my

conn = my.connect(host="localhost",user = "root",password = "123456",database= "quizzii")
cur = conn.cursor()

# Exit function
def exitt():
    print("Thanks for visiting!!!")
    cur.close()
    exit()
