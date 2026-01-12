# U.S. States Guessing Game (Python)

An educational Python game designed to help users learn and practice all 50 U.S. states.  
Players type in state names, and correct guesses are displayed on a blank U.S. map.

---

## How the Game Works

- A blank U.S. map is displayed using **turtle graphics**.
- The player is prompted to guess state names.
- For each correct guess:
  - The state name appears on the map at the correct location.
  - The guess counter increases.
- The game continues until:
  - All 50 states are guessed, **or**
  - The user clicks “Cancel”.
- Any states not guessed are saved to **`states_to_learn.csv`** for further practice.

---

## Technical Concepts & Skills Practiced

- Python programming
- **turtle** graphics for visual output
- **pandas** for reading and writing CSV files
- File handling
- User input and validation
- Basic game logic and iteration

---

## Game Preview

![Game Output](game-preview.jpg)

---

## Project Files

- `main.py` – main game script  
- `50_states.csv` – state names and x/y coordinates  
- `blank_states_img.gif` – map background image  
- `states_to_learn.csv` – generated after the game ends  
- `game-preview.jpg` – example screenshot of game output  

---

## How to Run the Game

1. Ensure **Python 3** is installed.

2. Install dependencies:
```bash
pip install pandas
```

3. Clone the repository:
```bash
git clone https://github.com/MichelleRunning/states-guessing-game.git
cd states-guessing-game
```

3. Make sure all project files remain in the same directory.

4. Run the game:
```bash
python main.py
```


