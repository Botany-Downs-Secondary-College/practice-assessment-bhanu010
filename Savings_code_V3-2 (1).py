#Bhanu's code.py
#Neha, Ali, Jessica and Bhanu, March 2020


global user_income
#Function 1
def get_word(question):
 while True:
  word = input(question)
  if not(word.isalpha()):
   print("Word must contain all alphabetic characters")   
  else:
    return word
   
#Function 2   
def get_yes_or_no(question):
 while True:
    word = get_word(question)
    if word[0].lower() == 'y':
       return True
    elif word[0].lower() == 'n':
       return False
    else:
         print("Please enter Yes or No")
   
#Function 3
def get_interger(question):
 while True:
  word = input(question)
  if(word.isdigit()):
   return int(word)
  else:
   print('Please enter a valid integer!')

def info():
    while True:
        try: 
            time_income = int(input("How soon do you want to buy the product. Enter in weeks: "))
            break
        except ValueError:
            print("Sorry, Enter a valid number.")
    
    while True:
        try:
            
            w_expenses = float(input("How much is your weekly expenses? :$"))
            if w_expenses > user_income:
                print("You are spending more than you earn, try again and decrease the weekly expenses!")

            else:
                break
                
        except ValueError:
            print("That is not a valid entry, please try again!")
            

global user_income
#first_tax = "user_income * 0.13"
#second_tax = user_income * 0.23
#third_tax = user_income * 0.30
        
#Function that calculates your tax.           
#def w_tax():
 #  if user_income <= 269:
  #    print("You have to pay {} tax".format (first_tax))
      #10.5% tax
   #elif user_income <= 923:
    #  print("You have to pay {} tax".format(second_tax))
     # #17.5% tax
   #elif user_income <= 1346:
    #  print("You have to pay {} tax".format(third_tax))
     # #30% tax
   #elif w_income > 1346:
    #  print("You have to pay {} tax".format(fourth_tax))   
   #else:
    #  print("You don't have to pay tax!")


# Main loop

print("Kia ora")
print("Welcome to 'Savings calculator', this programme will aid you in planning to purchase the item you desire.")
#Greet user   
#Asks user for name
name = get_word("What is your name? ")
#Compliments user
print( "{}, It is nice to meet you. You have a wonderful name!".format(name.capitalize())) 

satisfied = False
while not satisfied:
 #Ask user what they want to purchase
 purchase = get_word("What would you like to buy? ")
 cost = get_interger("How much does {} cost ? :$ ".format(purchase.capitalize()))
 print("Okay")
 while True:
     try:
         user_income = int(input("How much are you earning per week?: $"))
         break
     except ValueError:
         print("Sorry, Enter a valid number: ")
 print(info())
 
 #print(w_tax())

 
 #Asks user if they are satisfied with the end result. 
 satisfied = get_yes_or_no("Are you satisfied with the end result? yes -- finish programme, no -- restart programme: ")
 if satisfied:
  print("That's great {}, thank you for using savings calculator!".format(name.capitalize()))
 else:
  print("That's okay")


 
 






