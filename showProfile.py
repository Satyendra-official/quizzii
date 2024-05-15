import mysql.connector as my
import random
import exit
import updateProfile as update

conn = my.connect(host="localhost",user = "root",password = "123456",database= "quizzii")
cur = conn.cursor()

# Show Profile function
def showProfile(user,log):
    if log:
        print(f"Hello {user[0]} Your college is {user[2]} Your contact number is {user[-1]}")
    ch = input("Do you want to update your profile: y/n : ")
    if ch == 'y' or ch == 'Y':
        update.updateProfile(user,log)
    else:
        exit.exitt()
