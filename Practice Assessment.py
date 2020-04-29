#Practice Assessment
#Bhanu Raveenthiran, April 2020


#Function 1
def get_a_or_b(question):
 while True:
    need = get_a_or_b(question)
    if word[0].lower() == 'a':
       return True
    elif word[0].lower() == 'b':
       return False
    else:
         print("Please enter a or b")
#Greet User
print("******************************")
print("                               ")
print(" Welcome to Password Manager!")
print("                               ")
print("*****************************")

#Brief Description of Programme
#Provides Menu for creating new account or login to existing password manager

need = get_a_or_b("Type 'a' to create new account or type 'b' to login to existing password mananger")
