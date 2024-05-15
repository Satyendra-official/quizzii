import mysql.connector as my

conn = my.connect(host="localhost",user = "root",password = "123456",database= "quizzii")
cur = conn.cursor()

# Result function
def result(uname):
    

    # if uname==False:
    #     print("Please Login First")
    #     login()
    
    try:    
        cur.execute('select max(score) from result where enrollment = %s',(uname,))
        data = cur.fetchone()

        # print(data)
        print(f"Your Highest score is {data[0]}")
        # print(data[1])

        # sql = "select * from result where enrollment = 'Java'"
        # cur.execute(sql)

    except TypeError:
        print("No result Found.")

    except:
        print("Some Error has occured. Please try again.")

