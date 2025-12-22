# simple if
'''if condition:
    #statement
'''
# if else
'''
if condition:
    #stmts
else:
    #stmts
    '''
#  example
'''data={
    'lohit':'l@123',
    'surya':'b$123',
    'thanmai':'a@wer',
    'swetha':'S@5346'
}
uname,pwd=input("Enter the user name and pasword").split()
if data.get(uname)==pwd:
    print(f'Hello {uname} \nYour login successfull')
else:
    print("incorrect user name and password")'''

# if-else-if
'''
if condition:
    #stmts
elif condition:
    #stmts
elif condition:
    #stmts
else:
    #stmts
'''
# Example

'''ch=input("Enter the char: ")
vol='aeiouAEIOU'
if ch.isalpha():
    if ch.vol:        
elif ch.isdigit():
    print("digit")
else:
    print("special char")
'''

#nested if else

'''
if condition:
    if condition:
        if condition:
            #stmnts
        else:
            #stmts
    else:
        #stmts
else:
    #stmts
'''
#example

'''data={
    'lohit':'l@123',
    'surya':'b$123',
    'thanmai':'a@wer',
    'swetha':'S@5346'
}
uname,pwd=input("Enter the user name and pasword").split()
if uname in data:
    if data[uname]==pwd:
        print(f'Welcome {uname}')
    else:
        print("incorrect pssword")
else:
    print("incorrect user name")'''


'''amount = int(input("Enter the amount: "))

if amount > 10000:
    print("Trip to Goa")
elif 8000 <= amount < 10000:
    print("Clubings")
elif 5000 <= amount < 8000:
    print("Go for Cafe")
elif 3000 <= amount < 5000:
    print("Shopping")
elif 1000 <= amount < 3000:
    print("Visit Local Places ")
elif 500 <= amount < 1000:
    print("Order Somethings")
else:
    print("Go for chai and sleep")

hrs,mins = tuple(map(int,input("enter the hours and mins: ").split(':')))

if 0<=hrs<4 and 0<=mins<=59:
    print("It's high time. better go to sleep")

elif 4<= hrs < 12 and 0<=mins<=59:
    print("Good Morning. Have a great day")

elif 12<= hrs < 16 and 0<=mins<=59:
    print("Good Afternoon. Have a great lunch")

elif 16<=hrs<21 and 0<=mins<=59:
    print("Good Evening. Have a great dinner")

elif 21<=hrs<24 and 0<=mins<=59:
    print("Good Night. Scroll Reels")'''

# 0- sent
# 1-Delivered
# 2 - Seen

'''chatstatus= int(input("Enter the chat status: "))

if chatstatus == 0:
    print("sent, display single tick")

elif chatstatus == 1:
    print("Delivered, display double tick")

elif chatstatus ==2:
    print("seen, display blue tick")

else:
    print("Unable sent message, try again!!!")'''