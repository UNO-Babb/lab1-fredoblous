#MadLib.py
#Name: Joshua
#Date: 8/28/24
#Assignment: Lab1
#Purpose: To create a story using the user's inputs

def main():
  print("Madlib")
  #Ask user for words
  noun_one = input("Enter a food item: ")
  print(noun_one)

  noun_two = input("Enter a person: ")
  print(noun_two)

  noun_three = input("Enter a place: ")
  print(noun_three)

  adjective_one = input("Enter a adjective that relates to size: ")
  print(adjective_one)

  adjective_two = input("Enter a adjective that relates to age: ")
  print(adjective_two)

  adjective_three = input("Enter a adjective that relates to smell: ")
  print(adjective_three)

  verb_one = input("Enter a verb: ")
  print(verb_one)


  #Print the story with the user supplied words.
  print(f"{adjective_three} {noun_two} likes to {verb_one} {adjective_two} {noun_one} at {adjective_one} {noun_three}.")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
