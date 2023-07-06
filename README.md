# chess
Game development with pygame. Playing around with chess

### Structure
* Project Name
  - README.md
  - main.py
  - core/
      + __init__.py
      + board.py
      + piece.py
      + player.py
      + utils.py
  - assets/
      + images
      + sounds
  - tests/
      + __init__.py
      + test_board.py
      + test_piece.py
      + test_player.py

## root folder
The root folder contains main.py which is where the game is run. It also contains core folder where all game logic and python files are written, Assets is a folder for images sounds and media files. Tests is a separate folder for unit tests which will keep the project more tidy

## core
The game will be object oriented most of the files in core will contain classes for the given object. For instance piece will have a parent class with subclasses, queen pawn etc.
utils.py is a file for general purpose functions that does not belong to a class. For instance conversion of data structs.

## assets

## tests
