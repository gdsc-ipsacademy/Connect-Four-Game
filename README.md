# Connect four
A game of connect four against AI.

![image](https://github.com/gdsc-ipsacademy/Connect-Four-Game/assets/81830617/9ffb20cd-9c8e-40fd-9fb6-8942ffdb02a1)


![image](https://github.com/gdsc-ipsacademy/Connect-Four-Game/assets/81830617/469ed5b2-7d2f-4d5f-93b9-31bc19134d24)


# Directory structure
- [variables.py](https://github.com/gdsc-ipsacademy/Connect-Four-Game/blob/main/src/variables.py) contains all the GLOBAL variables for the project so that they are easy to find and change if ever needed. Helps in writing clean code.
- [functions.py](https://github.com/gdsc-ipsacademy/Connect-Four-Game/blob/main/src/functions.py) contains all the functions used in the game loop. This helps in bundling the functions together so that they are easy to find, edit and are easily accessible throughout the project. Keeps the main file clean as well.
- [ui_components.py](https://github.com/gdsc-ipsacademy/Connect-Four-Game/blob/main/src/ui_components.py) conatins all the UI elements for the game. Helps in keeping UI methods and other methods separate.
- [score_ai.py](https://github.com/gdsc-ipsacademy/Connect-Four-Game/blob/main/src/score_ai.py) contains the functions for the score based AI version.
- [minmax_ai.py](https://github.com/gdsc-ipsacademy/Connect-Four-Game/blob/main/src/minmax_ai.py) contains the functions for the minmax algorithm based AI version.
- [game.py](https://github.com/gdsc-ipsacademy/Connect-Four-Game/blob/main/src/game.py) contains the game loop and executes the software.

# Version information
- [v0.1.0](https://github.com/gdsc-ipsacademy/Connect-Four-Game/releases/tag/v0.1.0) contains the base game without AI. It just has human vs human mode where turns switch between both until the game is over.
- [v1.0.1](https://github.com/gdsc-ipsacademy/Connect-Four-Game/releases/tag/v1.0.1) contains the game with an AI that uses scoring method to try and beat the human player. This version contains just human vs AI mode where turns switch between both until the game is over.
- [v1.3.0](https://github.com/gdsc-ipsacademy/Connect-Four-Game/releases/tag/v1.3.0) contains the game with an AI that uses minmax algorithm with alpha-beta pruning, calculating upto depth 7, which makes it impossible to beat. This version contains just human vs AI mode where turns switch between both until the game is over. This version also includes sound effects for the game.
- [v1.3.1](https://github.com/gdsc-ipsacademy/Connect-Four-Game/releases/tag/v1.3.1) contains the game with different difficulty levels from easy to god mode for the user to choose from at the start of the game. This version contains just human vs AI mode where turns switch between both until the game is over.

# How to run the game?
1. Clone the repository to your machine following [how to clone a repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) documentation.
2. Create a virtual environment by using the command `python<version> -m venv <virtual-environment-name>` in your terminal.

(If you don't have venv installed, you can install it by running `pip install virtualenv` in your terminal.)

3. Activate the virtual environment by running either `<virtual-environment-name>/Scripts/activate.bat` in CMD or `<virtual-environment-name>/Scripts/Activate.ps1` in PowerShell.

(To deactivate the virtual environment run the command `deactivate`.)

4. Install the requirements in the virtual environment by running `pip install -r requirements.txt`.
5. Run the game by running `python -u <directory path>\Connect-Four-Game\src\game.py`

If you don't want to go through the hassle of creating a virtual environment, just run the commands in steps 4 and 5.
