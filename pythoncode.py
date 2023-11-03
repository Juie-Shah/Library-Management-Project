# Importing modules
import numpy as np
import pandas as pd
import mysql.connector as mc
import pymysql
from sqlalchemy import create_engine
# Creating engine
engine=create_engine('mysql+pymysql://root:12231@localhost/project')
# Naming the engines
alpha=engine.connect()
beta=engine.connect()
gamma=engine.connect()
delta=engine.connect()
# Connecting to mysql
mycon=mc.connect(host="localhost",user="root",passwd="12231",database="project")
if mycon.is_connected():
    df1=pd.read_sql("select * from LibBooks;", mycon)
if mycon.is_connected():
    df2=pd.read_sql("select * from schemes;", mycon)
if mycon.is_connected():
    df3=pd.read_sql("select * from members;",mycon)
if mycon.is_connected():
    df4=pd.read_sql("select * from circulation;",mycon)
# Input user choice
# This function is called when the user has to chose a service
def inputChoice():
    global user_choice
    user_choice = None
    # We use try catch here. If the choice is not an int, the except block gets executed
    try:
        user_choice = int(input("Choose a service: "))
        confirmChoice()
    except:
        print("Please enter a valid option.")
        inputChoice()
        
# Confirm users choice
# This function is called after user has entered a valid choice
def confirmChoice():
    uc = input("Are you sure (y/n)? ")
    if uc == "n":
        # User isn't happy with the choice
        inputChoice()
    elif uc == "y":
        # User is happy with the choice
        pass
    else:
        print("Please enter a valid option.")
        confirmChoice()

while True:
    # Make the main menu
    print("Welcome to the City Library. These are the Library Services:")
    print("1) Books")
    print("2) Schemes")
    print("3) Customers")
    print("4) Circulation")
    # Ask the user to chose a service
    inputChoice()
    # User has chosen and confirmed a choice
    if user_choice == 1:
        # User wishes to use the book services
        # Make the book menu
        print("Choose a book service:")
        print("1) View the books table")
        print("2) Add a book to table")
        print("3) Remove a book from table")
        # Ask the user to chose a service
        inputChoice()
        # User has chosen and confirmed a choice
        if user_choice == 1:
            # User wishes to view the books table
            print(df1)
        elif user_choice == 2:
            # User wishes to add a book to the table
            a = int(input("Enter index: "))
            b = input("Enter book id: ")
            c = input("Enter book name: ")
            d = input("Enter author's name: ")
            e = input("Enter genre: ")
            
            df1.at[a,:] = [b,c,d,e]
            df1.to_sql('books', alpha , if_exists='replace')
        elif user_choice == 3:
            # User wishes to remove a book
            dt=int(input("Enter the index of book you want to remove:"))
            df1.drop([dt])
            print(df1)
        else:
            # User choise wasn't 1 or 2 or 3. Thus, it was invalid
            print("Please enter a valid option")
            # Ask the user to chose a service
            inputChoice()
    elif user_choice == 2:
        # User wishes to use the scheme services
        # Scheme services code goes here ---
        print("Choose a service:")
        print("1.View schemes table")
        print("2.Add schemes to table")
        print("3.Remove schemes from table")
        inputChoice()
        if user_choice==1:
            print(df2)
        elif user_choice==2:
            a=int(input("Enter index:"))
            b=int(input("Enter Sr.No.:"))
            c=input("Enter scheme id:")
            d=input("Enter schemes:")
            e=int(input("Enter time period in months"))
            f=int(input("Enter cost in rupees:"))
            g=int(input("Enter discount in percent:"))
            h=int(input("Enter total amount in rupees:"))
            df2.at[a,:]=[b,c,d,e,f,g,h]
            df2.to_sql('books',beta,if_exists='replace')
        elif user_choice==3:
            dt=int(input("Enter the index of schemes you want to remove:"))
            df2.drop([dt])
            print(df2)

        else:
            #user choice wasnt 1 2 or 3. thus it was invalid
            print("Enter a valid option")
            #ask the user to chose a service
            inputChoice()
         
    elif user_choice == 3:
        # User wishes to use the customer services
        # Customer services code goes here ---
        print("Choose a service:")
        print("1.View members table")
        print("2.Add a new member")
        print("3.Remove a member")
        #Ask the user to chose a service
        inputChoice()
        #user has chosen and confirmed a service
        if user_choice == 1:
            #user wishes to see the table
            print(df3)
        elif user_choice ==2:
            #user wishes to add a new member
            a=int(input("Enter index:"))
            b=input("Enter member id:")
            c=input("Enter member name:")
            d=int(input("Enter member's mobile number:"))
            e=input("Enter member's email-id:")
            f=input("Enter date of membership taken:")
            g=input("Enter last date of membership")
            h=input("Enter scheme id:")
            df3.at[a,:]=[b,c,d,e,f,g,h]
            df3.to_sql('members',gamma, if_exists='replace')
        elif user_choice == 3:
            #user wishes to remove a member
            dt=int(input("Enter the index of member you want to remove:"))
            df3.drop([dt])
            print(df3)
        else:
            #user choice wasnt 1 2 or 3. thus it was invalid
            print("Enter a valid option")
            #ask the user to chose a service
            inputChoice()
        
    elif user_choice == 4:
        # User wishes to use the circulation services
        # Circulation services code goes here ---
        print("1) View the circulation table")
        print("2) Enter a into table")
        print("3) Remove from table")
        # Ask the user to chose a service
        inputChoice()
        # User has chosen and confirmed a choice
        if user_choice == 1:
            # User wishes to view the circulation table
            print(df4)
        elif user_choice == 2:
            # User wishes to add a book to the table
            a = int(input("Enter index: "))
            b = input("Enter book id: ")
            c = input("Enter member id: ")
            df4.at[a,:] = [b,c]
            df4.to_sql('circulation', delta , if_exists='replace')
        elif user_choice == 3:
            # User wishes to remove a book
            dt=int(input("Enter the index of book you want to remove:"))
            df4.drop([dt])
            print(df4)
        else:
            # User choise wasn't 1 or 2 or 3. Thus, it was invalid
            print("Please enter a valid option")
            # Ask the user to chose a service
            inputChoice()
        
    else:
        # User choise wasn't 1 or 2 or 3 or 4. Thus, it was invalid
        print("Please enter a valid option.")
        # Ask the user to chose a service
        inputChoice()
