import webbrowser

#  function for controlling the data in txt file
def user_info(ussnm, pssd): 
    name = input("Enter your name : ")
    age = input("Enter your age : ")
    ussnm_ = ussnm+" task.txt"
    f = open(ussnm_, 'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Age :")
    f.write(age)
    f.write('\n')
    f.close()

#  function for controlling sign-up
def signup():
    print("\n--------- New User Registration --------\n")
    username = input("Please enter your username : ")
    username = str(username)
    password = input("Please create a password : ")
    password = str(password)
    user_info(username, password)
    print("Signup Completed. Proceed to login")
    login()

#  function for controlling login
def login():
    print("\n--------- User Login --------\n")
    user_nm = input("Enter the username here : ")
    user_nm = str(user_nm)

    #same password while signup
    pass_wrd = input(("Enter Password : "))+'\n'
    pass_wrd = str(pass_wrd)
    try:
        usernm = user_nm+" task.txt"
        f_ = open(usernm, 'r')

        #read file for the entered password
        k = f_.readlines(0)[0]
        f_.close()

        #checking if the entered password is correct
        if pass_wrd == k :
            print("\n-------- Action Menu -------\n")
            print("1--Meditation \n2--Workout \n3--Dinner \n4--Partying \n5--Search the web")
            

            #storing the input from the above menu in 'a'
            a = int(input("select an action : "))
            if a == 1:
                meditation(usernm)
            elif a == 2:
                workout(usernm)
            elif a == 3:
                dinner(usernm)
            elif a == 4:
                party(usernm)
            elif a == 5:
                search()
            else :print("Wrong input")
        else :
            print("------- incorrect details -------")
            login()

    except Exception as e:
        print(e)
        login()


#function to play meditation music
def meditation(username):
    
    print("1--Forest \n2--Rain \n3--Lofi-Music (Hindi) \n4--Lofi-Music (English)\n")
    print("Enter the type of music from the menu given above : ")
   
    m = int(input("select an action : "))
    if m == 1:
        webbrowser.open("https://www.youtube.com/watch?v=Qm846KdZN_c", new=1)
    elif m == 2:
        webbrowser.open("https://www.youtube.com/watch?v=q76bMs-NwRk", new=1)
    elif m == 3:
        webbrowser.open("https://www.youtube.com/watch?v=KRA26LhuTP4", new=1)
    elif m == 4:
        webbrowser.open("https://www.youtube.com/watch?v=1WGCADztYKs", new=1)
    else :print("Wrong input")
    login()

#function to play workout music
def workout(username):
    
    print("1--Rap \n2--EDM \n3--Punjabi \n")
    print("Enter the type of music from the menu given above : ")
   
    w = int(input("select an action : "))
    if w == 1:
        webbrowser.open("https://www.youtube.com/watch?v=mvTt85df-qI", new=1)
    elif w == 2:
        webbrowser.open("https://www.youtube.com/watch?v=YRmD65vT1oA", new=1)
    elif w == 3:
        webbrowser.open("https://www.youtube.com/watch?v=4hr06fDoN4M", new=1)
    else :print("Wrong input")
    login()

#function to play dinner music
def dinner(username):
    
    print("1--Soft \n2--Jazz \n")
    print("Enter the type of music from the menu given above : ")
   
    d = int(input("select an action : "))
    if d == 1:
        webbrowser.open("https://www.youtube.com/watch?v=53nwh1aHCU8", new=1)
    elif d == 2:
        webbrowser.open("https://www.youtube.com/watch?v=xELRGsm7kUA", new=1)
    
    else :print("Wrong input")
    login()

#function to play partying music
def party(username):
    
    print("1--Hindi \n2--English \n")
    print("Enter the type of music from the menu given above : ")
   
    p = int(input("select an action : "))
    if p == 1:
        webbrowser.open("https://www.youtube.com/watch?v=PNXeH3UAKzE", new=1)
    elif p == 2:
        webbrowser.open("https://www.youtube.com/watch?v=dPGPMDduyyA", new=1)
    
    else :print("Wrong input")
    login()

#function to use search the web music option
def search():
    
    key = input("enter the songname (please use the format on+my+way , to enter multiple words) : ")
    if key == "exit":
        login()
    else:
        song = "https://www.youtube.com/results?search_query="+key
        webbrowser.open(song, new=1)
        search()
    

# main function for controlling login and sign-up
if __name__ == '__main__':
    print("\n######---WELCOME TO MY Music Player---######")
    print("\nAre you a new user?\n")
    a = int(input("Type 1 for YES and 0 for NO :: "))
    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("You have provided wrong input!")