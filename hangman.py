import random


predefined_hangman_words = [
    'machine',
    'automatic',
    'sunset',
    'volcano',
    'mystery'
]

def hangman():
    selected_word = random.choice(predefined_hangman_words)
    print(selected_word)
    word_length = len(selected_word)
    number_of_remaining_attempts= word_length 
    print( f'Guess the letters in the word!!! Its a {word_length} letter word'  )
    print(f'Number of attempts to guess the word: {number_of_remaining_attempts}')
    hyphen = "_"
    user_guessed_letters = list(hyphen * word_length)
    selected_word_to_letters = list(selected_word)
    while number_of_remaining_attempts > 0:
        user_input = input('Enter a letter: ')
        if user_input.isalpha():
            number_of_remaining_attempts -=1
            if user_input in selected_word_to_letters:
                for l in range(word_length):
                    if selected_word_to_letters[l]== user_input:
                        user_guessed_letters[l]= user_input                      
            else:
                         print('Wrong letter!! The letter doesnt exists in the word')
        else:
            print('Invalid character !! Only alphabetical choise is allowed') 

        print(f'Guessed Word: {' '.join(user_guessed_letters)}')  

        if hyphen not in user_guessed_letters:
           print('You guessed the correct word' )
           break
    else:
         print('Game Over you Lost, Number of attempt to guess the word was over')
    continue_playing = input('DO you want to continue playing ? (y/n)') 
    if continue_playing == 'y':
        hangman()      
    else:
        print('Thanks for playing!')       

        
        

    

if  __name__ == '__main__':
    hangman()
