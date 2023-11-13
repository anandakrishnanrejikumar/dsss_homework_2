import random
<<<<<<< HEAD


def function_A(min, max):
    """
    Random integer.
    """

    return random.randint(min, max)


def function_B():
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 - n2
    elif o == '-': a = n1 + n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3.14159265359
=======
#import unittest


def generate_random_integer(min_value, max_value):
    """
    Generating random integer within the specified range
    """

    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generating random arithmetic operator
    """
    return random.choice(['+', '-', '*'])


def generate_math_problem_and_answer(num1, num2, operator):
    """
    Generate a math problem and its correct answer based on provided numbers and operator.
    """
    problem = f"{num1} {operator} {num2}"

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2  # Fix: Correct the subtraction calculation
    else:
        answer = num1 * num2

    return problem, answer

def math_quiz():
    """
    conducting math quiz with user
    """
    score = 0
    total_questions = 3
>>>>>>> code_cleanup

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

<<<<<<< HEAD
    for _ in range(t_q):
        n1 = function_A(1, 10); n2 = function_A(1, 5.5); o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")
=======
    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10); num2 = generate_random_integer(1, 5.5); operator = generate_random_operator()

        problem, answer = generate_math_problem_and_answer(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid Input. Please enter a valid integer")
            continue
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")
>>>>>>> code_cleanup

if __name__ == "__main__":
    math_quiz()
