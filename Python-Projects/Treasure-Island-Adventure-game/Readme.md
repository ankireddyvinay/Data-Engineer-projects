# 🏴‍☠️ Treasure Island Adventure Game

A text-based adventure game where you navigate through choices to find the hidden treasure! Make the right decisions to avoid danger and claim your prize.

## 🎮 Game Overview

Navigate through a series of choices in this interactive story:
- **Mission**: Find the treasure and win the game
- **Format**: Text-based with multiple choice decisions  
- **Outcome**: One winning path, multiple ways to lose

## 🗺️ Game Flow

### Level 1: The Crossroad
- **Choice**: Go "left" or "right"
- **Consequence**: Going right leads to immediate game over

### Level 2: The Lake  
- **Choice**: "Wait" for boat or "swim" across
- **Consequence**: Swimming leads to trout attack

### Level 3: The House of Doors
- **Choice**: Enter "red", "yellow", or "blue" door
- **Consequences**: 
  - Red = Fire room (Game Over)
  - **Yellow = Treasure room (You Win!)** 🏆
  - Blue = Beast room (Game Over)

## 🏆 How to Win

Follow this exact path to find the treasure:
1. Choose **"left"** at the crossroad
2. Choose **"wait"** at the lake  
3. Choose **"yellow"** door at the house

## 🎯 Features

- ✅ ASCII art treasure map display
- ✅ Interactive story with user input
- ✅ Multiple branching paths and endings
- ✅ Case-insensitive input handling
- ✅ Immediate feedback for all choices
- ✅ Clear win/lose conditions

## 🚀 How to Run

1. Make sure you have Python 3.x installed
2. Save the code as `treasure_island.py`
3. Run the game:
```bash
python treasure_island.py
```

## 📋 Example Gameplay

```
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
[ASCII art continues...]
*******************************************************************************

Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a crossroad, where do you want to go? Type "left" or "right.
> left
You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.
> wait  
You arrive at the island unharmed. There is house with 3 doors. One red, one yellow and one blue. Which colour do you choose?
> yellow
You found the treasure. You Win!
```

## 🎲 All Possible Endings

| Path | Ending |
|------|--------|
| Right | Fall into hole → Game Over |
| Left → Swim | Trout attack → Game Over |
| Left → Wait → Red | Fire room → Game Over |
| Left → Wait → Blue | Beast room → Game Over |
| Left → Wait → Yellow | **Found treasure → You Win!** |
| Left → Wait → Other | Non-existent door → Game Over |

## 🔧 Requirements

- Python 3.x
- No external libraries required

## 🎨 Future Enhancements

- [ ] Add more decision levels
- [ ] Include inventory system
- [ ] Add character stats (health, items)
- [ ] Multiple treasure locations
- [ ] Save/load game progress
- [ ] Sound effects for different scenarios

## 🤝 Contributing

Feel free to fork this repository and submit pull requests to add new storylines, choices, or features!
