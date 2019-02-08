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
    # Intialize returned variable

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

    ans1 = input("Answer: ").lower()

    while ans1 != "A) Yellow".lower():
        print("Yowch! Incorrect answer!")
        print("Try Again!")

        ans1 = input("Answer: ").lower()

        if ans1 == "A) Yellow".lower():
            print("Good Job!")
            print("Correct answer!")
            break

        if ans1 == "Skip".lower():
            print("What a shame. You're skipping the question?")
            print("Skip granted!")
            break

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

    ans2 = input("Answer: ").lower()

    while ans2 != "C) Violet".lower():
        print("Yowch! Incorrect answer!")
        print("Try Again!")

        ans2 = input("Answer: ").lower()

        if ans2 == "C) Violet".lower():
            print("Good Job!")
            print("Correct answer!")
            break

        if ans2 == "Skip".lower():
            print("What a shame. You're skipping the question?")
            print("Skip granted!")
            break

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

    ans3 = input("Answer: ").lower()

    # If loop condition for skip option
    # If loop condition for correct answer
    # While loop condition to repeat question if answered incorrectly

    while ans3 != "B) Red".lower():
        print("Yowch! Incorrect answer!")
        print("Try Again!")

        ans3 = input("Answer: ").lower()

        if ans3 == "B) Red".lower():
            print("Good Job!")
            print("Correct answer!")
            break

        if ans3 == "Skip".lower():
            print("What a shame. You're skipping the question?")
            print("Skip granted!")
            break

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

    ans4 = input("Answer: ").lower()

    # If loop condition for skip option
    # If loop condition for correct answer
    # While loop condition to repeat question if answered incorrectly

    while ans4 != "D) Green".lower():
        print("Yowch! Incorrect answer!")
        print("Try Again!")

        ans4 = input("Answer: ").lower()

        if ans4 == "D) Green".lower():
            print("Good Job!")
            print("Correct answer!")
            break

        if ans4 == "Skip".lower():
            print("What a shame. You're skipping the question?")
            print("Skip granted!")
            break

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

    ans5 = input("Answer: ").lower()

    # If loop condition for skip option
    # If loop condition for correct answer
    # While loop condition to repeat question if answered incorrectly

    while ans5 != "D) Blue".lower():
        print("Yowch! Incorrect answer!")
        print("Try Again!")

        ans5 = input("Answer: ").lower()

        if ans5 == "D) Green".lower():
            print("Good Job!")
            print("Correct answer!")
            break

        if ans5 == "Skip".lower():
            print("What a shame. You're skipping the question?")
            print("Skip granted!")
            break

    # End of questions

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