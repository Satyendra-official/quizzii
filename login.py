import mysql.connector as my
import random
import attemptQuiz as aq 
import result as res
import exit
import updateProfile as update
import showProfile as show


conn = my.connect(host="localhost",user = "root",password = "123456",database= "quizzii")
cur = conn.cursor()

# Login function
def login():
    global username
    global logged_in
    uname = input("Enter username: ")
    # cur.execute('select password from register where enrollment = %s',(uname,))
    cur.execute('select * from register where enrollment = %s',(uname,))
    data = cur.fetchone() #fetchall
    # print(data)
    if data is not None:
        pwd = input("Enter password: ")
        if data[3] == pwd:
            print(f"Welcome {data[0]}")
            username = uname
            logged_in = True
        else:
            print("Wrong password!!!")
            # cur.close()
            login()
    else:
        print("Wrong Username or you didn't registered with us!!!")
        ch = input("do you want to register!!! y/n : ")
        if ch=='y' or ch == 'Y':
            register()
        else:
            login()
        
    print("""
        Choose 1 for Attempt quiz
        Choose 2 for View result
        Choose 3 for Show profile
        Choose 4 for Update Profile
        Choose 5 for Exit
    """)
    ch = input("Enter your choice: ")
    if ch == '1':
        aq.attemptQuiz(username)
    elif ch == '2':
        res.result(username)
    elif ch == '3':
        show.showProfile(data,logged_in)
    elif ch == '4':
        update.updateProfile(data,logged_in)
    elif ch == '5':
        exit.exitt()

