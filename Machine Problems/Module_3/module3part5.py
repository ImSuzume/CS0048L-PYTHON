"""
Create a program that calculates the average grade for a student based
on their scores in different subjects. The program should display a menu
with options to add scores and calculate the average. The program should
continue to run until the user chooses to exit.
"""

studentScores = {}

def menu():
    print("==============================")
    print("1. Add Score")
    print("2. Calculate Average")
    print("3. Exit")
    print("==============================")

def addScore():
    global studentScores
    subjectName = input("Enter the subject: ").lower()
    scoreInput = input("Enter the score: ")

    if scoreInput.replace('.', '', 1).isdigit():
        score = eval(scoreInput)
        if score >= 0 and score <= 100:
            if subjectName in studentScores:
                studentScores[subjectName].append(score)
            else:
                studentScores[subjectName] = [score]
            print("Score added.")
        else:
            print("Score must be between 0 and 100.")
    else:
        print("Invalid input. Please enter a number.")

def calculateAverage():
    if studentScores == {}:
        print("")
        print("No scores added.")
    else:
        print("\nAverage Scores by Subject:")
        for subjectName, scores in studentScores.items():
            total = 0
            for score in scores:
                total += score
            average = total / len(scores)
            print(f"{subjectName}: {average:.2f}")

def main():
    choice = ""
    while choice != "3":
        menu()
        choice = input("Enter your choice (1-3): ").lower()
        if choice == "1":
            addScore()
        elif choice == "2":
            calculateAverage()
        elif choice == "3":
            print("See you soon...")
        else:
            print("")
            print("Invalid input. Try again.")

main()
