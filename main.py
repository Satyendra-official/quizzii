import mysql.connector as my
import random
import register as reg
import login as log
import attemptQuiz as aq 
import result as res
import exit


conn = my.connect(host="localhost",user = "root",password = "123456",database= "vishnu_test")
cur = conn.cursor()
# print(conn)

username = ""
logged_in = False



# Main function
def main():
    print("#"*30)
    print("#"*12, "QUIZ", "#"*12)
    print("""
            1. Register
            2. Login
            3. Attempt Quiz
            4. Result
            5. Exit
    """)
    print("#"*30)
    print("#"*30)

    choice = input("Choose an option 1/2/3/4/5 to process: ")
    if choice == '1':
        reg.register()
    elif choice  == '2':
        log.login()
    elif choice == '3':
        if logged_in==False:
            print("Please Login First.")
            log.login()
        
        else:
            aq.attemptQuiz()
        # attemptQuiz(False)


    elif choice == '4':
        if logged_in==False:
            print("Please Login First.")
            log.login()
        # result(False)

        else:
            res.result()

    elif choice == '5':
        exit.exitt()
    else:
        print("Please enter coorect option")
        main()

# print("#"*30)

if __name__ == "__main__":
    main()

