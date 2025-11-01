# 🐍 Python Snake Game

A classic implementation of the Snake game built from scratch using Python and the built-in `turtle` module.

This project is written using object-oriented programming (OOP), splitting the game's logic into separate classes for the `Snake`, the `Food`, and the `Scorecard`.

<img width="302" height="313" alt="image" src="https://github.com/user-attachments/assets/7ff64c2f-d171-4535-88fa-29aebac13b14" />


## ✨ Features

* **Classic Gameplay:** Control the snake to eat the food and grow longer.
* **OOP Design:** The code is cleanly organized into four classes:
    * `Snake`: Manages the snake's body, movement, and controls.
    * `Food`: Manages the food's appearance and random placement.
    * `Scorecard`: Manages score tracking and displays the "Game Over" message.
    * `main`: Handles the main game loop, screen setup, and collision detection.
* **Collision Detection:** The game ends if the snake hits a wall or its own tail.
* **Responsive Controls:** The controls are designed to prevent the snake from turning 180 degrees back onto itself in a single move.
* **Clean UI:** Features a simple, dark-themed background.

## 💻 Tech Stack

* **Language:** Python
* **Core Libraries:** `turtle` (for graphics), `random` (for food), `time` (for game speed)

## 🚀 How to Run


If you have Python installed on your computer and want to run the code yourself:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Spargerx/Snake_Game.git](https://github.com/Spargerx/Snake_Game.git)
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd Snake_Game
    ```
3.  **Run the game!**
    ```sh
    python main.py
    ```
    *(Note: You may need to use `python3 main.py` on macOS or Linux)*

## ⌨️ Controls

* **Up:** `Up Arrow`
* **Down:** `Down Arrow`
* **Left:** `Left Arrow`
* **Right:** `Right Arrow`

## 📁 File Structure

* **main.py**: Handles the main game loop, screen setup, and collision detection.
* **snake.py**: Defines the `Snake` class (movement, body, controls).
* **food.py**: Defines the `Food` class (placement).
* **scorecard.py**: Defines the `Scorecard` class (tracking score, game over).
