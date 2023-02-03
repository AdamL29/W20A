import mariadb
from dbhelpers import connect_db, disconnect_db, execute_statement 

def login():
    cursor = connect_db()
    alias = input("Please provide a username: ")
    password = input("Please provide a password: ")
    cursor.execute("SELECT * FROM hackers WHERE alias = ? AND password = ?", [alias,password])
    results = cursor.fetchone()
    global id
    id = results[0]
    if results != None:
        print("Welcome: ", results[0])
        selection()
    else:
        print("Incorrect Username and/or Password")
    disconnect_db(cursor)

def new_exploit():
    cursor = connect_db()
    content = input("Post Content: ")
    id = input("User's ID: ")
    cursor.execute("CALL new_exploit(?,?)", [content, id])
    print("Your exploit has been posted")

def exploits():
    cursor = connect_db()
    inputs = id
    cursor.execute("CALL user_exploits(?)", [inputs])
    results = cursor.fetchall()
    for input in results:
        print(input[0])

def all_exploits():
    cursor = connect_db
    user = cursor.fetchall()
    cursor.execute("SELECT * FROM exploits INNER JOIN hackers ON WHERE user_id != ?", [user[0]])
    results = cursor.fetchall()
    for input in results:
        print(input[0])

def quit():
    print("G00db73")

def selection():
    print("1. Make a new exploit!")
    print("2. See your exploits!")
    print("3. See all exploits!")
    print("4. Exit")
    while True:
        inputs = int(input("Please select from the following: "))
        if inputs == 1:
            new_exploit()
        elif inputs == 2:
            exploits()
        elif inputs == 3:
            all_exploits()
        elif inputs == 4:
            quit()
        else:
            print("Please make a selection")
            break

login()