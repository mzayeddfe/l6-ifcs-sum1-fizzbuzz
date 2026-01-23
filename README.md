# FizzBuzz Project

## User Documentation

### What is this? 

This program implements the classic FizzBuzz problem. The main logic is in `fizzbuzz.py`, and tests are in `test_fizzbuzz.py`. The function takes a single integer and returns:
- "Fizzbuzz" if the number is divisible by both 3 and 5
- "Fizz" if divisible by 3
- "Buzz" if divisible by 5
- The number as a string otherwise.

### How do I use it?
1. [Install dependencies](#installing-dependencies) if you do not already have them.
2. [Use the guide for the FizzBuzz function](#using-the-fizzbuzz-function-in-your-code)


## Installing Dependencies

- You need Python 3.x installed. To install Python, visit: https://www.python.org/downloads/

- If you want to run tests, you need to install `pytest`:

    ```
    pip install pytest
    ```

### Using the fizzbuzz Function in Your Code

You can import the `fizzbuzz` function from `fizzbuzz.py` and use it in your own Python scripts or in the Python interactive shell. The function returns a string for a single number.

#### Example Usage

1. Open a Python shell or create a new Python script in the same directory.
2. Import the function:
   ```python
   from fizzbuzz import fizzbuzz
   ```
3. Call the function with your desired range (e.g., 1 to 100):
   ```python

   print(fizzbuzz(15))  # Output: Fizzbuzz
   print(fizzbuzz(9))   # Output: Fizz
   print(fizzbuzz(10))  # Output: Buzz
   print(fizzbuzz(7))   # Output: 7
   ```

This will print the FizzBuzz result for a single number.



## Technical Documentation

- **fizzbuzz.py**: Contains the main logic for the FizzBuzz problem.
- **test_fizzbuzz.py**: Contains tests for the FizzBuzz implementation using pytest. (Note: The test file must be named with underscores, not dashes, for pytest to discover it.)
- **.github/workflows/fizzbuzz-tests.yml**: GitHub Actions workflow file that automatically runs the test suite on every push and pull request. It sets up a Python environment, installs dependencies, and runs pytest to ensure code quality and correctness.

The main function takes a single integer and returns the appropriate FizzBuzz string based on divisibility by 3 and/or 5.

## Developer Documentation


### Project Structure
- `fizzbuzz.py`: Main script.
- `test_fizzbuzz.py`: Test script (ensure the file is named with underscores, not dashes).
- `.github/workflows/fizzbuzz-tests.yml`: Continuous Integration (CI) workflow for automated testing with GitHub Actions.

### Continuous Integration
All tests are automatically run on GitHub Actions for every push and pull request using the workflow defined in `.github/workflows/fizzbuzz-tests.yml`. This ensures that all code changes are tested before being merged.


### How to Run Tests Locally
To run the tests locally, make sure you are in the project root directory. Run the following command:
```
pytest
```
Pytest will automatically discover and run all test files named `test_*.py` (with underscores).

### Contribution Guidelines
- Follow PEP8 style guidelines.
- Write tests for new features or bug fixes.
- Document your code with comments where necessary.
