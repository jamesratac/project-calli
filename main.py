#toDo: build login logic, username unavailable, incorrect password, user locked out

def login(username,password):
    file = open("credentials.txt", "r")
    for i in file:
        a,b = i.split(",")
        #b = b.strip()
        print(a,b)

def register(username,password):
    #print("registered")
        file = open("credentials.txt","a")
        file.write('\n'+username+","+password)
        file.close()

#authentication logic
def access(option):
    if(option=="login"):
        username = input("enter username: ")
        password = input("enter password: ")
        login(username,password)
    elif(option=="register"):
        print("create username and password to register")
        username = input("enter username: ")
        password = input("enter password: ")
        login(username,password)

def run():
    global option
    option = input("login or register: ")
    if(option!="login" and option!="register"):
        run()

run()
access(option)

