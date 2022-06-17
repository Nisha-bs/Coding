#!/usr/bin/python3
import re
import json
import os.path
from os import path 
import random


user_details={}
user=[]
if not path.exists('user_1.json'):
  with open('user_1.json','w') as o_file:
    json.dump(user,o_file)

def init():
  print("Welcome to bank")
  
  haveaccount = int(input('''You are New_User or Old_user:
  1 Old User
  2 New User
  '''))
  if(haveaccount == 1):
    login()
  elif(haveaccount == 2):
    register()
  else:
    print("You have selected invalid option")
    init()


def login():
  
  print("Login to your account")

  account_Number = (input("what is your account number?"))
  acc_no = re.fullmatch("[0-9]{10}",account_Number)
  if acc_no:
    ph_no = input("Enter the mobile_no")
 
    for account_number,userdetails in user_details.items():
      if(account_number == account_Number):
        if(user_details["client_mobile_no"] == ph_no):
          bankoperation() 

   
    else:
      print("Invalid account or ph_no")


 
def register():
  print("Register")
  email = input("what is your email address")
  c_name = input("Enter the name")
  client_name="[A-Z]{1}[a-z]{1,20}\s+[A-Z]{1}"
  mobile_no = input("Enter the mobile_no")
  client_mobile_no="[6-9]{1}[0-9]{9}"
  name=re.fullmatch(client_name,c_name)
  ph_no=re.fullmatch(client_mobile_no,mobile_no)
  account_number = generate_account_number()
 
  if name:
    if ph_no:
      user_details["client_name"]=c_name
      user_details["client_mail_id"]=email
      user_details["client_mobile_no"]=mobile_no
      user_details["account_number"]=account_number
      print(user_details)
      with open('user_1.json','r') as r_file:
        a=json.load(r_file)
        a.append(user_details)
      with open('user_1.json','w') as w_file:
        json.dump(a,w_file)
    else:
      print("Enter the valid number")
      register()
  else:
    print("Enter the valid name")
    register()

  
  #user_details[account_number] = [ c_name, mobile_no, email ]
  
  print("Your Account has been created")
  print(generate_account_number())
  bankoperation()


def bankoperation():
  #print("Welcome %s %s" % (user[0],user[1]))
  
  selected_option = int(input('''What would you like to do?
  1 deposit
  2 withdrawal
  3 current_balance
  4 exit
  '''))
  
  if(selected_option == 1):
    deposit()
  elif(selected_option == 2):
    withdrawal()
  elif(selected_option == 3):
    current_balance()
  elif(selected_option == 4):
    exit()
  else:
    #bankoperation(user)
    print("Invalid option selected")

def withdrawal():
  initial_balance=int(input("enter initial amount"))
  amount=int(input("Enter the withdraw amount:"))
  if initial_balance>=amount:
    initial_balance-=amount
    print("\n You withdraw the amount",amount)
    print("Your balance is:",initial_balance)
  else:
    print("\n Insufficient balance")


def deposit():
  initial_balance=int(input("enter initial amount"))
  amount=int(input("Enter the deposit amount:"))
  initial_balance+=amount
  print("deposit amount:",amount)
  print("Your balance:",initial_balance)


def current_balance():
  initial_balance=int(input("enter initial amount"))
  print("\n The current balance:",initial_balance)


def generate_account_number():
  
  print("Generating account number")
  return random.randrange(1111111111,9999999999)

init()



