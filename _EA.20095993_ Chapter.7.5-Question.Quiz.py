'''
Name: Erin Alvarico
Date: October 23, 2018
Lab: Chapter 7 5-Question Quiz
Create a simple quiz program that asks the user to answer 5 questions, keeps track of the number of
questions answered and prints the appropriate message corresponding to how many answered correctly.
'''

# Main class starts here

def main():

    # Intro text

    print("Welcome to the Color Theory Quiz!")
    print("")

    # First [enter] prompt initiated: to give users time to read before proceeding

    input("< Press [Enter] to continue >")

    # Explains what the quiz is about

    print("")
    print("This quiz is designed to test your knowledge on colors and their")
    print("corresponding meaning and mood.")
    print("")
    print("Are you ready?")
    print("")

    input("< Press [Enter] to continue >")

    # Question 1:

    print("")
    print("Question 1:")
    print("")
    print("What color represents happiness and optimism?")
    print("")
    print("A) Yellow")
    print("B) Blue")
    print("C) Red")
    print("D) Orange")
    print("")

    # Prompt user for answer

    q1ans = input("Answer: ").lower()

    # Count for how many questions correctly answered

    qcorrect = 0

    # If loop to create counter for correctly answered questions

    if q1ans == "A) Yellow".lower():
        qcorrect = qcorrect + 1
        print("Wow! Good job!")
    else:
        print("Yowch! Incorrect answer, better luck next time!")

    print("")
    input("<Press [Enter] to continue >")
    print("")

    # Question 2:

    print("")
    print("Question 2:")
    print("")
    print("What color represents mystery and royalty?")
    print("")
    print("A) Green")
    print("B) Pink")
    print("C) Violet")
    print("D) Red")
    print("")

    # Prompts user for answer

    q2ans = input("Answer: ").lower()

    # If loop to create counter for correctly answered questions

    if q2ans == "C) Violet".lower():
        qcorrect = qcorrect + 1
        print("Wow! Good job!")
    else:
        print("Yowch! Incorrect answer, better luck next time!")

    print("")
    input("<Press [Enter] to continue >")
    print("")

    # Question 3:

    print("")
    print("Question 3:")
    print("")
    print("What color represents passion and aggressiveness?")
    print("")
    print("A) Black")
    print("B) Red")
    print("C) White")
    print("D) Orange")
    print("")

    # Prompts user for answer

    q3ans = input("Answer: ").lower()

    # If loop to create counter for correctly answered questions

    if q3ans == "B) Red".lower():
        qcorrect = qcorrect + 1
        print("Wow! Good job!")
    else:
        print("Yowch! Incorrect answer, better luck next time!")

    print("")
    input("<Press [Enter] to continue >")
    print("")

    # Question 4:

    print("")
    print("Question 4:")
    print("")
    print("What color represents safety and money?")
    print("")
    print("A) Yellow")
    print("B) Black")
    print("C) Blue")
    print("D) Green")
    print("")

    # Prompts user for answer

    q4ans = input("Answer: ").lower()

    # If loop to create counter for correctly answered questions

    if q4ans == "D) Green".lower():
        qcorrect = qcorrect + 1
        print("Wow! Good job!")
    else:
        print("Yowch! Incorrect answer, better luck next time!")

    print("")
    input("<Press [Enter] to continue >")
    print("")

    # Question 5:

    print("")
    print("Question 5:")
    print("")
    print("What color represents loyalty and trust?")
    print("")
    print("A) Orange")
    print("B) Green")
    print("C) Red")
    print("D) Blue")
    print("")

    # Prompts user for answer

    q5ans = input("Answer: ").lower()

    # If loop to create counter for correctly answered questions

    if q5ans == "D) Blue".lower():
        qcorrect = qcorrect + 1
        print("Wow! Good job!")
    else:
        print("Yowch! Incorrect answer, better luck next time!")

    # End of questions

    print("")
    input("<Press [Enter] to continue >")
    print("")

    print("")
    print("Thank you for your input! Now we will assess your results!")
    print("Loading...")

    print("")
    input("<Press [Enter] to continue >")
    print("")

    # Results: number correctly answered displayed

    print("You have answered ", qcorrect, " out of 5 questions correct!")

    # Print a personalized message depending on how well the player did

    if qcorrect == 5:
        print("Awesome! You Rock!")
    elif qcorrect == 4:
        print("Not bad. Try again soon!")
    elif qcorrect == 3:
        print("Not bad. Try again soon!")
    else:
        print("Better luck next time!")

    print("")
    input("<Press [Enter] to continue >")
    print("")

    # Terminate program

    print("Thank you for playing the Color Theory Quiz!")
    print("The program will now terminate.")

    print("")
    input("<Press [Enter] to continue >")

    print("")
main()