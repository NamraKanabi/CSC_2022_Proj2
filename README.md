This program is essentially a lite version of commonly known game called wordle. Player is initially asked to enter a 5 letter word. On entering the said word, it will be checked whether the word is a recognized word inside the database, if yes then it will sort its letter into three categories. GREEN means letter is in the word and at correct position. ORANGE means letter is in the word but at incorrect position. RED means letter is not in the word. Player is given 6 chances to deduce the correct word. 
Game is played by running main.py
Wordle175.py contains classes used in main.py
clean.py reads the word5Dict.txt file and sorts the data in it and writes it into scrabble5.txt.
Data in scrabble5.txt is used to generate words for the game. 