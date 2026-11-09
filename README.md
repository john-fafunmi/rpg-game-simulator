# Python RPG Battle Simulator

A lightweight, text-based command-line RPG built in Python. This project demonstrates core Object-Oriented Programming (OOP) principles, data encapsulation, and robust command-line input handling.

## Why I Built This

I built this project to transition from writing basic Python scripts to practicing Object-Oriented Programming (OOP). As a beginner, I wanted a hands-on project to solidify my understanding of:
- Structuring code with classes (`Hero`, `Monster`).
- Using `@property` and setters to handle data encapsulation and safety.
- Writing reliable command-line input loops using `try-except` to prevent crashes.

## Key Features

- **Object-Oriented Design:** Clean separation of game entities utilizing `Hero` and `Monster` classes.
- **Data Encapsulation:** Uses Python properties (`@property` and setters) to safely manage and constrain health values between `0` and `100`.
- **Turn-Based Combat:** Interactive combat loop featuring weapon selections and randomized monster damage using Python's `random` module.
- **Input Validation:** Implements `try-except` blocks and `while` loops to handle invalid user selections gracefully without crashing.

## How to Run

1. Clone the repository and navigate into the directory:
   ```bash
   git clone [https://github.com/john-fafunmi/rpg-game-simulator.git](https://github.com/john-fafunmi/rpg-game-simulator.git)
   cd rpg-game-simulator
