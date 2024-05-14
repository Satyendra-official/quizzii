import mysql.connector as my
import random
import result as res
import exit

conn = my.connect(host="localhost",user = "root",password = "123456",database= "vishnu_test")
cur = conn.cursor()

# Attempt Quiz function
def attemptQuiz(uname):
    
    # if uname==False:
    #     print("Please Login First")
    #     login()
    ch = input("Choose an option\n 1. Python\n 2. Maths\n 3. Java ")

    if ch == '1':
        sql = "select * from question where Category = 'Python'"
        cur.execute(sql)
        ques = cur.fetchall() #fetchone()
        # print(ques) #[(),(),(),()]
        qu = [] #100
        for i in ques:
            qu.append(i) #[, , , , ,]
        qs = random.sample(qu,1) #14, 25, 89, 99
        n = 1
        correct = 0
        for i in qs:
            # op = [f"{i[2]}",f"{i[3]}",f"{i[4]}",f"{i[5]}"]
            # random.shuffle(op)
            
            print(f"HEllo {uname} you are attempting quiz of {i[-1]}")
            print(f"Q.{n}. {i[1]}\n A. {i[2]}\n B. {i[3]}\n C. {i[4]}\n D. {i[5]}\n")
            
            # print(f"Q.{n}. {i[1]}")
            # print(f" A. {op[0]}\n B. {op[1]}\n C. {op[2]}\n D. {op[3]}")

            ans = input("Your Answer A/B/C/D: ").upper()
            if ans == i[-2]:
                correct += 1

            n = n+1
        print(f"Your Result is '{correct}' out of '10'. ")

        try:
            quiz_data = (correct,uname)
            sql = "insert into result (score,enrollment) values(%s,%s)"
            cur.execute(sql,quiz_data)
            conn.commit()

        except:
            print("Some error has occured. Please try again.")
        
    

        
        print("""
                1. choose 1 to re attempt the quiz
                2. choose 2 to see the result
                3. choose 3 to exit.
                """)

        ch=input("Enter your choice :   ")
        if ch=='1':
            attemptQuiz(uname)
        elif ch=='2':
            res.result(uname)
        elif ch=='3':
            exit.exitt()
        else:
            print("Invalid choice.")
            exit.exitt()


    elif ch == '2':
        sql = "select * from question where category = 'Maths'"
        cur.execute(sql)
        ques = cur.fetchall() #fetchone()
        # print(ques) #[(),(),(),()]
        qu = [] #100
        for i in ques:
            qu.append(i) #[, , , , ,]
        qs = random.sample(qu,10) #14, 25, 89, 99
        n = 1
        correct = 0
        for i in qs:
            # op = [f"{i[2]}",f"{i[3]}",f"{i[4]}",f"{i[5]}"]
            # random.shuffle(op)
            
            print(f"HEllo {uname} you are attempting quiz of {i[-1]}")
            print(f"Q.{n}. {i[1]}\n A. {i[2]}\n B. {i[3]}\n C. {i[4]}\n D. {i[5]}\n")
            
            # print(f"Q.{n}. {i[1]}")
            # print(f" A. {op[0]}\n B. {op[1]}\n C. {op[2]}\n D. {op[3]}")

            ans = input("Your Answer A/B/C/D: ").upper()
            if ans == i[-2]:
                correct += 1

            n = n+1
        
        print(f"Your Result is '{correct}' out of '10'. ")

        

        try:
            quiz_data = (correct,uname)
            sql = "insert into result (score,enrollment) values(%s,%s)"
            cur.execute(sql,quiz_data)
            conn.commit()

        except:
            print("Some error has occured. Please try again.")

        
        print("""
                1. choose 1 to re attempt the quiz
                2. choose 2 to see the result
                3. choose 3 to exit.
                """)

        ch=input("Enter your choice :   ")
        if ch=='1':
            attemptQuiz(uname)
        elif ch=='2':
            res.result(uname)
        elif ch=='3':
            exit.exitt()
        else:
            exit.exitt()

    elif ch == '3':
        sql = "select * from question where category = 'Java'"
        cur.execute(sql)
        ques = cur.fetchall() #fetchone()
        # print(ques) #[(),(),(),()]
        qu = [] #100
        for i in ques:
            qu.append(i) #[, , , , ,]
        qs = random.sample(qu,10) #14, 25, 89, 99
        n = 1
        correct = 0
        for i in qs:
            # op = [f"{i[2]}",f"{i[3]}",f"{i[4]}",f"{i[5]}"]
            # random.shuffle(op)
            
            print(f"HEllo {uname} you are attempting quiz of {i[-1]}")
            print(f"Q.{n}. {i[1]}\n A. {i[2]}\n B. {i[3]}\n C. {i[4]}\n D. {i[5]}\n")
            
            # print(f"Q.{n}. {i[1]}")
            # print(f" A. {op[0]}\n B. {op[1]}\n C. {op[2]}\n D. {op[3]}")

            ans = input("Your Answer A/B/C/D: ").upper()
            if ans == i[-2]:
                correct += 1

            n = n+1
        print(f"Your Result is '{correct}' out of '10'. ")


        try:
            quiz_data = (correct,uname)
            sql = "insert into result (score,enrollment) values(%s,%s)"
            cur.execute(sql,quiz_data)
            conn.commit()
        
        except:
            print("Some error has occured. Please try again.")

        
        print("""
                1. choose 1 to re attempt the quiz
                2. choose 2 to see the result
                3. choose 3 to exit.
                """)

        ch=input("Enter your choice :   ")
        if ch=='1':
            attemptQuiz(uname)
        elif ch=='2':
            res.result(uname)
        elif ch=='3':
            exit.exitt()
        else:
            exit.exitt()

    else:
        print("Invalid choice.")
        exit.exitt()
