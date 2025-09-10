# Tip Calculator 💰

A simple Python command-line application that calculates tips and splits bills among multiple people.

## Features

- ✅ Calculate tip amount based on percentage
- ✅ Add tip to original bill total
- ✅ Split the total amount among multiple people
- ✅ Round final amounts to 2 decimal places
- ✅ User-friendly interactive prompts

## How to Use

1. Run the program
2. Enter the total bill amount (accepts decimal values)
3. Choose tip percentage (10, 12, 15, or any other percentage)
4. Enter the number of people splitting the bill
5. Get the amount each person should pay

## Example

```
Welcome to the tip calculator!
What was the total bill? $100.50
What percentage tip would you like to give? 18
How many people to split the bill? 4
Each person should pay: $29.64
```

**Calculation breakdown:**
- Original bill: $100.50
- 18% tip: $18.09
- Total with tip: $118.59
- Split 4 ways: $29.64 per person

## Requirements

- Python 3.x
- No external dependencies required

## Installation & Running

1. Clone this repository:
```bash
git clone https://github.com/yourusername/tip-calculator.git
cd tip-calculator
```

2. Run the program:
```bash
python tip_calculator.py
```

## Code Structure

The program follows these steps:
1. Prompts user for bill amount
2. Gets tip percentage from user
3. Asks for number of people
4. Calculates tip amount: `bill × (tip_percentage ÷ 100)`
5. Adds tip to original bill
6. Divides total by number of people
7. Rounds to 2 decimal places and displays result

## Future Enhancements

- [ ] Add input validation for negative numbers
- [ ] Support for different currencies
- [ ] Option to round up to nearest dollar
- [ ] Save calculation history
- [ ] GUI interface

## Contributing

Feel free to fork this repository and submit pull requests for any improvements!
