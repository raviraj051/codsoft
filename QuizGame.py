# Define a list of quiz questions as dictionaries
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "correct_answer": "C"
    },
    {
        "question": "Who was the first President of the United States?",
        "options": ["A. Thomas Jefferson", "B.John Adams ", "C. George Washington", "D. Benjamin Franklin"],
        "correct_answer": "C"
    },
    {
        "question": "In which year did Christopher Columbus first arrive in the Americas?",
        "options": ["A. 1492", "B. 1521", "C. 1607", "D. 1776"],
        "correct_answer": "A"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Go", "B. Au", "C. Ag", "D. Ge"],
        "correct_answer": "B"
    },
    {
        "question": "Who is the founder of Google?",
        "options": ["A. Otto von Bismarck", "B. Larry Page", "C. Christopher Latham", "D. Sundar Pichai"],
        "correct_answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "correct_answer": "C"
    },
    {
        "question": "What is 7 x 8?",
        "options": [],
        "correct_answer": "56"
    }
]

# Initialize the user's score
score = 0

# Display the welcome message and rules
print("Welcome to the Quiz Game!")
print("You will be asked multiple-choice and fill-in-the-blank questions.")
print("Let's get started!\n")

# Iterate through the quiz questions
for index, question in enumerate(quiz_questions, start=1):
    print(f"Question {index}: {question['question']}")

    if question['options']:
        for option in question['options']:
            print(option)
        user_answer = input("Your answer (A, B, C, D): ").upper()
    else:
        user_answer = input("Your answer: ")

    # Evaluate the user's answer
    if user_answer == question['correct_answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer is: {question['correct_answer']}\n")

# Calculate the final score
total_questions = len(quiz_questions)
percentage_score = (score / total_questions) * 100

# Display the final result
print(f"Quiz completed!\nYour final score is: {score}/{total_questions}")
print(f"Your performance: {percentage_score}%")

# Provide a performance message
if percentage_score >= 70:
    print("Congratulations! You did great!")
else:
    print("Keep practicing to improve your knowledge.")
