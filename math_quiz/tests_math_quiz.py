import unittest
from math_quiz import generate_random_integer, generate_random_operator, generate_math_problem_and_answer

class TestMathQuizFunctions(unittest.TestCase):
    """
    Unit tests for the functions in math_quiz.py.
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
            (8, 3, '-', '8 - 3', 5),  # Fix: Update the expected answer to 5
            (4, 6, '*', '4 * 6', 24),
            # Add more test cases here
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            with self.subTest(num1=num1, num2=num2, operator=operator):
                problem, answer = generate_math_problem_and_answer(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
