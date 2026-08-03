# 2048 Game (Academic Project & Evolution)

## Project Overview
This project is a fully functional version of the popular **2048 puzzle game**, built from scratch using Python and the Tkinter GUI library. 

It was originally developed in **May 2025** as the **Final Project** for the academic course:  
**Programming Techniques and Applications**.

*Note: This repository serves as a lightweight architectural overview, showcasing the structural configuration, interface design, and method signatures of the application rather than the complete source implementation. In order to protect the intellectual property and personal effort invested in developing this system, the comprehensive execution logic has been kept private. If you would like to explore the full, integrated codebase, please reach out to me directly using the contact email provided on my CV.*

### Continuous Improvement (Refactoring)
While the core functional game was successfully completed and graded in May 2025, I am committed to clean code and continuous learning. I have since **refactored and optimized** the entire codebase to:
- Transition from highly hardcoded logic to a streamlined, dynamic mathematical grid system.
- Eliminate massive code duplication across movement methods into a unified pipeline.
- Implement strict modularity by completely separating the core puzzle mechanics from the rendering framework.

---

## Architectural Highlights
Designed entirely using **Object-Oriented Programming (OOP)** principles, the project strictly isolates responsibilities to keep components loosely coupled:
- **`game.py` (Controller/Entry)**: Initializes the main window, computes the mathematical layout grid, paints static structural frames, and maps global keyboard listeners.
- **`Board.py` (State Management)**: Evaluates grid states, handles multi-directional flow, filters empty positions, logs move milestones, and monitors win/loss conditions.
- **`tile.py` (UI Presentation)**: Translates raw tracking integers into dynamic canvas shapes, controls coloring maps based on numeric sizes, and intercepts empty slots to keep tiles visually blank.
- **`utility.py` (Core Engine)**: Centralizes cross-functional drawing commands and executes the recursive sorting physics for sliding and merging tile operations.

---

## Technical Prerequisites

To run this application locally, you only need a standard installation of Python 3. 

### Verify Python Installation
Open your terminal (macOS/Linux) or Command Prompt (Windows) and type:
```bash
python --version
```
*(Any version of Python 3.x will work seamlessly. Tkinter comes bundled natively with standard Python installations, meaning no third-party package installs like `pip` are required).*

---

## How to Run the Game

Follow these simple steps to launch the game manually:

1. **Download the Source Code**: Ensure that all four core files (`game.py`, `Board.py`, `tile.py`, and `utility.py`) are downloaded and placed into the **exact same folder/directory**.
2. **Open your Terminal/Command Prompt**: Navigate to the directory containing your project files:
   ```bash
   cd path/to/your/project-folder
   ```
3. **Execute the Application**: Launch the entry point script by running:
   ```bash
   python game.py
   ```

---

## How to Play & Game Controls

The goal of the game is to slide numbered tiles across a grid, combining matching tiles to create a tile with the number 2048.

- **Move Tiles**: Use the **Arrow Keys** (`Up`, `Down`, `Left`, `Right`) on your keyboard to slide tiles in the corresponding direction. 
- **Start Over**: Click the **New Game** button in the top interface section to reset your current score and clear the grid.
- **Exit Safely**: Click the **Quit** button to gracefully shut down the application window. Your highest score is automatically preserved inside a local `record.txt` file and will load up the next time you launch the game!
