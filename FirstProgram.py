#FirstProgram.py
#Name: Joshua
#Date: 8/28/24
#Assignment: Lab 1
#Purpose: Asks for the user's name and age and uses the provided information to formulate the birth year of the user

def main():
  print("First Program")
  #Say hello
  print("Hello User")
  
  #Ask for the user's name
  name = input("What is your name? ")

  #Use the user's name in the program.
  print("Nice to meet you,", name + ".")

  #Ask the user for their age.
  age = int(input("How old are you? "))
  #Tell the user what year they were born in.
  print("Based on your given input you were born in", 2024 - age)

  #Assume that they have not had their birthday yet this year.
  birth_year = int(input("What year were you born in? "))
  
  if birth_year != (2024 - age):
     print("You have not had your birthday yet.")
  else:
     print("You have had your birthday this year")



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
