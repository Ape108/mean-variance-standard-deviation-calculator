# Mean-Variance-Standard Deviation Calculator

A Python project that calculates various statistical measures (mean, variance, standard deviation, max, min, and sum) for a 3x3 matrix of numbers. This project is part of the freeCodeCamp Data Analysis with Python certification.

## Project Description

This calculator takes a list of 9 numbers and performs statistical calculations on them after reshaping them into a 3x3 matrix. The calculations are performed:
- Along each axis (rows and columns)
- For the flattened matrix
- For each individual axis

## Features

- Calculates the following statistical measures:
  - Mean
  - Variance
  - Standard Deviation
  - Maximum
  - Minimum
  - Sum
- Handles input validation
- Returns results in a structured dictionary format

## Requirements

- Python 3.x
- NumPy

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from mean_var_std import calculate

# Example input
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Calculate statistics
result = calculate(numbers)

# Access results
print(result['mean'])  # Get mean values
print(result['variance'])  # Get variance values
print(result['standard deviation'])  # Get standard deviation values
```

## Input Format

The function expects a list of exactly 9 numbers. The numbers will be reshaped into a 3x3 matrix for calculations.

## Output Format

The function returns a dictionary containing the following keys:
- 'mean'
- 'variance'
- 'standard deviation'
- 'max'
- 'min'
- 'sum'

Each key contains a list of three values:
1. Calculations along axis 0 (columns)
2. Calculations along axis 1 (rows)
3. Calculations for the flattened matrix

## Error Handling

The function will raise a ValueError if:
- The input list does not contain exactly 9 numbers

## Testing

The project includes a test suite to verify the functionality. Run the tests using:
```bash
python test_module.py
```

## Project Structure

- `mean_var_std.py`: Main implementation file
- `test_module.py`: Test suite
- `requirements.txt`: Project dependencies
- `main.py`: Example usage

## License

This project is part of the freeCodeCamp curriculum and is available for educational purposes.

