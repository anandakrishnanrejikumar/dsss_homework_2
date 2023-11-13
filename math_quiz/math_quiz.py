import random
import unittest

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within the specified range.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generate a random arithmetic operator (+, -, or *).
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
    Conduct a math quiz game with the user.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = generate_math_problem_and_answer(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()

class TestMathGame(unittest.TestCase):
    """
    Unit tests for the math quiz game functions.
    """

    def test_generate_random_integer(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        """
        Test the generation of a random arithmetic operator.
        """
        operators = set()
        for _ in range(1000):  # Test a large number of random values
            operators.add(generate_random_operator())
        self.assertSetEqual(operators, {'+', '-', '*'})

    def test_generate_math_problem_and_answer(self):
        """
        Test the generation of a math problem and its correct answer.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            # Add more test cases here
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_math_problem_and_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
