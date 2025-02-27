# Hangman Game

This is a simple Hangman game implemented in Python. The game randomly selects a word, and the player must guess the word by suggesting letters within a limited number of attempts.

## Features
- Random word selection from the system dictionary or fallback list
- ASCII art to visualize hangman stages
- Tracks guessed letters to prevent repetition
- Input validation for single-letter guesses
- Encourages user interaction with clear feedback

## How to Play
1. Run the script in a Python environment.
2. The game will randomly choose a word.
3. You will see the word displayed as underscores (e.g., `_ _ _ _`).
4. Guess one letter at a time.
5. If the letter is in the word, it will be revealed in its correct position.
6. If the letter is incorrect, you lose an attempt.
7. The game continues until you either guess the word or run out of attempts.

## Installation & Execution
### Prerequisites
- Python 3.x installed on your system

### Steps to Run
1. Clone this repository or download the script.
2. Open a terminal or command prompt and navigate to the script location.
3. Run the script using:
   ```sh
   python hangman.py
   ```

## File Structure
```
/your_project_directory
│── hangman.py
│── README.md
```

## Potential Enhancements
- Add a graphical user interface (GUI) version.
- Implement multiplayer mode.
- Integrate an API for word selection.

## License
This project is open-source and free to use.

