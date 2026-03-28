class chatbook:
    def __init__(self):
        self.__name='Default user'
        self.username=""
        self.password=""
        self.logged_in=False
       # self.menu()

    def menu(self):
        choice=input(""" 
              1.Want to sign up.
              2.Want to sign in.
              3.Send a message to a friend.
              4.Upload a post.
              5.Press any other key to exit
                           

""")
        if choice=='1':
            self.sign_up()
            self.menu()
        elif choice=='2':
            self.sign_in()
            self.menu()
        elif choice=='3':
            self.send_message()
            self.menu()
        elif choice=='4':
            self.upload_post()
            self.menu()
        else:
            print('invalid choice')
            exit()        
                
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name
    def sign_up(self):  
        if self.username=='' and self.password==''  :
            usd=input('create a username')
            pwd=input('create a password')
            self.username=usd
            self.password=pwd
        else:
            print('please sigin using 2')    

    def sign_in(self):
        if self.username=='' and self.password=="":
            print('Please sigup using 1')
        else:
            usd=input("Please enter your username")    
            pwd=input("Please enter your password")    
            if self.username==usd and self.password== pwd:
                self.logged_in=True
                print('you are logged in')
            else:
                print('invalid username or password')

    def send_message(self):
        if self.logged_in:
            friend=input('enter your friend name')
            message=input('enter your message')
            print(f"you sent {message} to {friend}")
        else:
            print('please login to send a message')   

    def upload_post(self):
        if self.logged_in:
            post=input("Enter your post here" )    
            print("your post has been uploaded")  
        else:
            print("please login to upload post")                   
        

sam=chatbook()
