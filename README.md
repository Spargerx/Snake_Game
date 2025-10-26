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

There are two ways to play this game:

### 1. For Players (Easy Method)
You can download the ready-to-play game for Windows directly from the releases page.

1.  Go to the **[Releases Page](https://github.com/Spargerx/Snake_Game/releases)**.
2.  Under the latest release, click on `snake_game_v1.0.exe` or `snake_game_v1.0.zip` to download it.
3.  Double-click the downloaded file to play!

---

## ⚠️ Antivirus / Windows Defender Warning

Some users may see a message like "Virus detected" or "Unrecognized app" when downloading the `.exe` file from the Releases page.

**Don’t worry — this is a false positive and a common issue with Python games built using PyInstaller.**

### 🧠 Why this happens

* The game’s `.exe` file is not digitally signed (it’s made by an independent developer (me!!), not a verified company).
* Windows Defender and some antivirus tools flag new, unsigned executables as “suspicious” simply because they haven’t seen them before — not because they contain malware.

You can verify the source code here on GitHub — it’s 100% open-source and safe to run.

### 🪄 How to safely run the game

If you downloaded the `.exe` and Windows blocks it:

1.  Right-click the file → **Properties** → check “**Unblock**” (if the option appears).
2.  Double-click to open it.
3.  If you see “Windows protected your PC”:
    * Click **More info**
    * Then click **Run anyway**

Or, if you prefer, you can always build your own `.exe` directly from the source using:

```sh
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
```
---
### 2. For Developers (Running from Source)
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
