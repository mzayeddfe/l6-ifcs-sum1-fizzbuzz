# FizzBuzz Project

## User Documentation

### What is this? 

This program implements the classic FizzBuzz problem. To use it, run the `fizzbuzz.py` script. The function lists numbers from 1 to the number you provide, but for multiples of 3, it prints "Fizz" instead of the number, for multiples of 5, it prints "Buzz", and for multiples of both 3 and 5, it prints "FizzBuzz".

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

You can import the `fizzbuzz` function from `fizzbuzz.py` and use it in your own Python scripts or in the Python interactive shell.

#### Example Usage

1. Open a Python shell or create a new Python script in the same directory.
2. Import the function:
   ```python
   from fizzbuzz import fizzbuzz
   ```
3. Call the function with your desired range (e.g., 1 to 100):
   ```python
   fizzbuzz(100)
   ```

This will print the FizzBuzz sequence from 1 to 100.



## Technical Documentation

- **fizzbuzz.py**: Contains the main logic for the FizzBuzz problem.
- **test_fizzbuzz.py**: Contains tests for the FizzBuzz implementation using pytest.
- **.github/workflows/fizzbuzz-tests.yml**: GitHub Actions workflow file that automatically runs the test suite on every push and pull request. It sets up a Python environment, installs dependencies, and runs pytest to ensure code quality and correctness.

The main function iterates from 1 to the number provided to the function and prints the appropriate output based on divisibility by 3 and/or 5.

## Developer Documentation


### Project Structure
- `fizzbuzz.py`: Main script.
- `test_fizzbuzz.py`: Test script.
- `.github/workflows/fizzbuzz-tests.yml`: Continuous Integration (CI) workflow for automated testing with GitHub Actions.

### Continuous Integration
All tests are automatically run on GitHub Actions for every push and pull request using the workflow defined in `.github/workflows/fizzbuzz-tests.yml`. This ensures that all code changes are tested before being merged.


### How to Run Tests Locally
To run the tests locally, make sure you are in the project root directory. Run the following command:
```
pytest
```
Pytest will automatically discover and run all test files named `test_*.py`.

### Contribution Guidelines
- Follow PEP8 style guidelines.
- Write tests for new features or bug fixes.
- Document your code with comments where necessary.
