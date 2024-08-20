import csv
import os
import random

FILEPATH = "H:/Random Coding Practice/Random-Coding-Practices/quiz.csv"


def createQuestionBankFromCSV(file_path):
    with open(file=file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        questionBank = [line for line in csv_reader]
    return questionBank


def clear_screen():
    os.system("cls||clear")


def ask_question(question, answer):
    response = input(question + " ").lower()
    if response == answer:
        print("That is the correct answer")
        return 1
    else:
        print("That was an incorrect answer")
        return 0


def play_round(questionBank, no_of_question):
    scores = []
    for _ in range(no_of_question):
        random.shuffle(questionBank)
        temp = questionBank.pop()
        question = temp["Question"]
        answer = temp["Answer"].lower()
        scores.append(ask_question(question, answer))
    return scores


def display_score(scores, no_of_question):
    final_score = sum(scores)
    print("Final Score: ")
    print(f"You got {final_score} out of {no_of_question}")
    print(f"The percentage is {(final_score / no_of_question) * 100}%")


def game():
    playing = True
    questionBank = createQuestionBankFromCSV(FILEPATH)
    while playing:
        clear_screen()
        no_of_question = int(
            input("How many questions do you want? (MAX IS 10) "))
        scores = play_round(questionBank, no_of_question)
        display_score(scores, no_of_question)
        if input("Still wanna play? ").lower() != "yes":
            playing = False


game()
