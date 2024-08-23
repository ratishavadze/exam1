print("hello and welcome to my online bank where you can invest youre money also you can put and withdraw tanks for listening")
print("Register")
print("fill these up")

info = []

name = input("please enter youre name: ")
surname = input("please enter youre surmane: ")                                                                 
age = int(input("please enter youre age: "))
password = input("please neter youre pasword: ")
repeat_password = input("repeat youre password: ")
if password != repeat_password:
    print("password is inccorect please try again")
    repeat_password = input("repeat youre password: ")
info.append(name)
info.append(password)

print(info)

#login
print("LOGIN")
print("fill these up")
lname = input("please enter youre name: ")
if name != lname:
    print("name is incorrect please try again")
    repeat_name = input("repeat youre name: ")


lpassword = input("please neter youre pasword: ")
if name != lname:
    print("password is incorrect please try again")
    repeat_password = input("repeat youre password")
    
ballance = 0
print ("youre ballance = 0")
ballance = int(input("enter number of quantity want to deposit"))
print(ballance)

withdraw = input("enter number of quantity you want to withdraw")

if withdraw > ballance:
    print("NO there's not enough cash on youre ballance")
    print("enter lower number please")
    withdraw = input("enter number of quantity you want to withdraw")

ballance = ballance - withdraw

print(ballance)



exit()