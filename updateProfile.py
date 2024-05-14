import mysql.connector as my
import random
import exit
import pass_val as ps



conn = my.connect(host="localhost",user = "root",password = "123456",database= "vishnu_test")
cur = conn.cursor()


# Update Profile Function
def updateProfile(user,logedIn_info):
    
    user_udate = user[1]
    logged = logedIn_info
    # print(user_udate)
    # print(logged)

    print("""
        Choose 1 to Update Name
        Choose 2 to Update College
        Choose 3 to Update Password 
        Choose 4 to Update Contact 
    """)
    ch = input("Enter your choice: ")
    if(ch=='1'):
        newName = input("Enter your New name : ")
        sqlfor="update register set name= %s where enrollment = %s"
        cur.execute(sqlfor,(newName,user_udate))
        conn.commit()
        conn.close()

    elif(ch=='2'):
        newClg = input("Enter your New College Name : ")
        sqlfor="update register set college= %s where enrollment = %s"
        cur.execute(sqlfor,(newClg,user_udate))
        conn.commit()
        conn.close()
    elif(ch=='3'):
        
        while True:
            newPwd = ps.validPass()
            if newPwd:
                print("VALID PASSWORD")
                break
            else:
                print("Not a valid Password.")
                print("Your Password should contain upper case, lower case, digit and a special character.")
                print("Your Password should contain 8 to 20 Letters")

        sqlfor="update register set password= %s where enrollment = %s"
        cur.execute(sqlfor,(newPwd,user_udate))
        conn.commit()
        conn.close()
    elif(ch=='4'):
        newCon = input("Enter your New Contact : ")
        sqlfor="update register set contact= %s where enrollment = %s"
        cur.execute(sqlfor,(newCon,user_udate))
        conn.commit()
        conn.close()
    else:
        print("Invalid Choice. ")
        print("Press y to continue updation Or n to exit.")
        ch =  input("Enter the Choice : ")
        if ch=='y':
            updateProfile(user,logedIn_info)
        else:
            exitt()
 