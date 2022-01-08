# Unit Testing with Python

## Running the unit tests
You can run the unit tests with the following command
```
python3 unit_tests.py
```

`unit_tests.py` imports the calculator that we created and the `unittest` module needed to set up and run the tests.

## Add more unit tests
You should add more test cases to the `unit_tests.py` file. The general structure is to have a class that takes in the unittest module: `class TestCalculator(unittest.TestCase)`. Then, add functions that test a specific part of the code written in calculator.py

## setUp()
Method called to prepare the test fixture. This is called immediately before calling the test method; any exception raised by this method will be considered an error rather than a test failure. The default implementation does nothing.

## tearDown()
Method called immediately after the test method has been called and the result recorded. This is called even if the test method raised an exception, so the implementation in subclasses may need to be particularly careful about checking internal state. Any exception raised by this method will be considered an error rather than a test failure. This method will only be called if the setUp() succeeds, regardless of the outcome of the test method. The default implementation does nothing.

## More information
[unittest](https://docs.python.org/3/library/unittest.html#basic-example) \
[Python_unittest_Assertions](https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index) \
[library-project](https://replit.com/@appbrewery/library-project-end)