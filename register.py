import mysql.connector as my

import pass_val as ps

conn = my.connect(host="localhost",user = "root",password = "123456",database= "quizzii")
cur = conn.cursor()

def register():
    name = input("NAME : ")
    enr = input("Enrollment : ")
    clg = input("College : ")
    
    # Password validation
    while True:
        pswd = ps.validPass()
        
        # psw = validPass()
        if pswd:
            print("VALID PASSWORD")
            break
        else:
            print("Not a valid Password.")
            print("Your Password should contain upper case, lower case, digit and a special character.")
            print("Your Password should contain 8 to 20 Letters")
            
    # pswd = input("Password : ")

    con = input("contact : ")


    try:
        data = (name,enr,clg,pswd,con)
        sql = "insert into register (name, enrollment, college, password, contact) values(%s,%s,%s,%s,%s)"

        cur.execute(sql,data)
        conn.commit()
        print("Registration Done")

    
    except:
        print("This enrollment number already exists. Please enter your unique enrollment id for registration. ")
        print("Please Try again.\n")

        register()
    


