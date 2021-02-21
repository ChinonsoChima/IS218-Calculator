import csv
import unittest
import os

# the .py file name is Calculator and the class name is also Calculator
from src.calculator import Calculator

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# test data file path, the fills is a csv file.
test_data_file_path = (os.path.join(THIS_DIR, os.pardir, 'testCases/Unit_Test_Addition.csv'),
                       os.path.join(THIS_DIR, os.pardir, 'testCases/Unit_Test_Subtraction.csv'),
                       os.path.join(THIS_DIR, os.pardir, 'testCases/Unit_Test_Multiplication.csv'),
                       os.path.join(THIS_DIR, os.pardir, 'testCases/Unit_Test_Division.csv'),
                       os.path.join(THIS_DIR, os.pardir, 'testCases/Unit_Test_Square_Root.csv'),
                       os.path.join(THIS_DIR, os.pardir, 'testCases/Unit_Test_Square.csv'))

# test data file object
test_data_file_object = list()

# test data row list.
test_data_row_list = list()


# load test data from ./test_data.csv file.
def load_test_data():
    # NOTE TO SELF: Make these lists of lists. So each index will be a file and each object will be that file, and each data row index will be a file
    global test_data_file_object, test_data_row_list
    # open test data csv file.
    num = 0
    for i in test_data_file_path:
        test_data_row_list.append(list())
        test_data_file_object.append(open(i, 'r'))
        # read the csv file and return the text line list.
        csv_reader = csv.reader(test_data_file_object[num], delimiter=',')

        for row in csv_reader:
            test_data_row_list[num].append(row)
        num += 1

        print('open and load data from ' + i + ' complete.')


# close and release the test data file object.
def close_test_data_file():
    global test_data_file_object, test_data_file_path
    num = 0
    for i in test_data_file_object:
        if i is not None:
            i.close()
            print('close file ' + test_data_file_path[num] + ' complete.')
        num += 1


'''
This is the TestCase class that test Calculator class functions.
'''


class TestCalculator(unittest.TestCase):
    # this is the Calculator class instance.
    calculator = None

    # class level setup function, execute once only before any test function.
    @classmethod
    def setUpClass(cls):
        load_test_data()
        print('')
        print('setUpClass')

    # class level setup function, execute once only after all test function's execution.
    @classmethod
    def tearDownClass(cls):
        close_test_data_file()
        print('')
        print('tearDownClass')

    # execute before every test case function run.
    def setUp(self):
        self.calculator = Calculator()
        print('')
        print('setUp')

    # execute after every test case function run.
    def tearDown(self):
        # release the Calculator object.
        if self.calculator is not None:
            self.calculator = None
        print('')
        print('tearDown')

    # below are function that test Calculator class's plus, minus, multiple and divide functions.
    def test_addition(self):
        print('')
        print('******test_addition******')
        # get each row text from the csv file.
        for row in test_data_row_list[0]:
            # the first column in the text line is x value.
            x = row[0]
            # the second column in the text line is y value.
            y = row[1]
            # the third column in the text line is (x + y) value.
            expect_result = row[2]
            result = self.calculator.sum(x, y)

            print(str(x) + ' + ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))

    def test_subtraction(self):
        print('')
        print('******test_subtraction******')
        for row in test_data_row_list[1]:
            x = row[0]
            y = row[1]
            expect_result = row[2]
            result = self.calculator.subtract(x, y)

            print(str(x) + ' - ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertAlmostEqual(float(result), float(expect_result))

    def test_multiplication(self):
        print('')
        print('******test_multiplication******')
        for row in test_data_row_list[2]:
            x = row[0]
            y = row[1]
            # the fifth column in the text line is (x * y) value.
            expect_result = row[2]
            result = self.calculator.multiply(x, y)

            print(str(x) + ' * ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))

    def test_division(self):
        print('')
        print('******test_division******')
        for row in test_data_row_list[3]:
            x = row[0]
            y = row[1]
            # the sixth column in the text line is (x / y) value.
            expect_result = row[2]
            result = self.calculator.divide(x, y)

            print(str(x) + ' / ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))

    def test_squareRoot(self):
        print('')
        print('******test_squareRoot******')
        for row in test_data_row_list[4]:
            x = row[0]
            expect_result = row[1]
            result = self.calculator.root(x, 2)

            print(' √ ' + str(x) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))

    def test_squared(self):
        print('')
        print('******test_squared******')
        for row in test_data_row_list[5]:
            x = row[0]
            # the sixth column in the text line is (x / y) value.
            expect_result = row[1]
            result = self.calculator.power(x, 2)

            print(str(x) + '² ' + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))


if __name__ == '__main__':
    unittest.main()


def build_test_suite():
    # create unittest.TestSuite object.
    test_suite = unittest.TestSuite()
    # add each test function to the test suite object.
    test_suite.addTest(TestCalculator('test_addition'))
    test_suite.addTest(TestCalculator('test_subtraction'))
    test_suite.addTest(TestCalculator('test_multiplication'))
    test_suite.addTest(TestCalculator('test_division'))
    test_suite.addTest(TestCalculator('test_squareRoot'))
    test_suite.addTest(TestCalculator('test_squared'))
    return test_suite
