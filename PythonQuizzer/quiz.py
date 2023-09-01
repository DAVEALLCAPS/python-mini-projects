import json
import time
import random

def load_questions():
    with open("questions.json", "r") as file:
        questions = json.load(file)
    return questions

def quiz():
    questions = load_questions()
    random.shuffle(questions)  # shuffle the questions

    total_questions = len(questions)
    correct_answers = 0

    for index, q in enumerate(questions, 1):
        print(f"Question {index}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"{idx}. {option}")

        start_time = time.time()
        answer = input("\nEnter your answer (time limit: 10s): ")
        end_time = time.time()

        if end_time - start_time > 10:
            print("Time's up!")
            continue

        if q['options'][int(answer)-1] == q['answer']:
            correct_answers += 1
            print("Correct!\n")
        else:
            print(f"Wrong! Correct answer is {q['answer']}\n")

    print(f"You scored {correct_answers}/{total_questions}!")

if __name__ == "__main__":
    quiz()
