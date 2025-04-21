# Hangman-Exercise
Hangman game using python
## Create virtual environment by following the below steps
- install python version 3.13
- Create virtual environment by running 'python3 -m venv venv'
- Activate the virtual environment by running 
  - For windows 'venv\Scripts\activate'
  - For mac 'source venv/bin/activate'
## To run the program
- Run 'Python3 hangman.py'

## Instructions to play the game
- A word will be selected from the predefined list.
- User will be informed about how many letters the word has and will be asked to guess the letters.
- Number of attempts to guess the word will be informed to the user.
- Number of attempts is equal to number of letters in the word.
- User can guess one letter at a time.
- If the user guess the correct letter it is populated at the correct position in the word.
- If the user guess the wrong word, then a message 'Wrong letter!! The letter doesn't exists in the word' is displayed.
- Non alphabetical characters and more than one alphabet are considered as invalid input.
- Invalid inputs are not considered as an attempt.
- If the user guess the correct word within the attempts a sucesss mesage 'You guessed the correct word' is displayed.
- If the user couldn't guess the word within the attempts given, then 'Game over!!! You Lost, Number of attempts to guess the word is over' message will be displayed.
- The user is given a chance to continue playing if they want to.
  