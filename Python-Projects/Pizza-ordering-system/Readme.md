# 🍕 Python Pizza Delivery System

A simple command-line pizza ordering application that calculates the total bill based on pizza size and toppings.

## 🍕 Menu & Pricing

### Pizza Sizes
| Size | Price |
|------|-------|
| Small (S) | $15 |
| Medium (M) | $20 |
| Large (L) | $25 |

### Toppings
| Topping | Small | Medium | Large |
|---------|-------|--------|-------|
| Pepperoni | +$2 | +$3 | +$4 |
| Extra Cheese | +$3 | +$3 | +$3 |

## 🎯 Features

- ✅ Interactive pizza size selection
- ✅ Pepperoni topping with size-based pricing
- ✅ Extra cheese option
- ✅ Case-insensitive input handling
- ✅ Real-time bill calculation
- ✅ Input validation for pizza sizes

## 🚀 How to Use

1. Run the program
2. Select pizza size (S, M, or L)
3. Choose whether you want pepperoni (Y or N)
4. Choose whether you want extra cheese (Y or N)
5. Get your final bill total

## 📋 Example Order

```
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: Y
your final_bill is $:32
```

**Order breakdown:**
- Large pizza: $25
- Pepperoni (Large): +$4
- Extra cheese: +$3
- **Total: $32**

## 🔧 Requirements

- Python 3.x
- No external libraries required

## 💻 Installation & Running

1. Clone or download the repository
2. Save the code as `pizza_ordering.py`
3. Run the program:
```bash
python pizza_ordering.py
```

## 🧮 Pricing Examples

| Size | Base | +Pepperoni | +Extra Cheese | Total |
|------|------|------------|---------------|-------|
| Small | $15 | +$2 | +$3 | $20 |
| Medium | $20 | +$3 | +$3 | $26 |
| Large | $25 | +$4 | +$3 | $32 |

## 🐛 Known Issues

- Final bill displays even when invalid pizza size is entered
- No validation for pepperoni/cheese inputs beyond Y/N

## 🚀 Future Enhancements

- [ ] Add more topping options
- [ ] Implement multiple pizza ordering
- [ ] Add delivery fee calculation
- [ ] Include tax calculation
- [ ] Add order summary before final bill
- [ ] Implement discount codes
- [ ] Add GUI interface
- [ ] Save order history

## 🏗️ Code Structure

The program follows this flow:
1. Get pizza size and set base price
2. Check for pepperoni and add size-appropriate cost  
3. Check for extra cheese and add $3 if selected
4. Display final calculated bill

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements, bug fixes, or new features!