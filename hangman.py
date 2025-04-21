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
    
    word_length = len(selected_word)
    number_of_remaining_attempts= word_length 
    print(f'\nGuess the letters in the word!!! Its a {word_length} letter word \n'  )
    print(f'Number of attempts to guess the word: {number_of_remaining_attempts} \n')
    hyphen = "_"
    user_guessed_letters = list(hyphen * word_length)
    selected_word_to_letters = list(selected_word)
    while number_of_remaining_attempts > 0:
        user_input = input('Enter a letter: ').lower()
        if not user_input.isalpha() or len(user_input) !=1:
            print('\nInvalid character !! Only one alphabetical character is allowed. Invalid inputs are not taken as an attempt. Try with a valid character'  )
        else:
            number_of_remaining_attempts -=1
            if user_input in selected_word_to_letters:
                for l in range(word_length):
                    if selected_word_to_letters[l]== user_input:
                        user_guessed_letters[l]= user_input                      
            else:
                         print('\nWrong letter!! The letter doesnt exists in the word')
        
             

        print(f'{' '.join(user_guessed_letters)}')  

        if hyphen not in user_guessed_letters:
           print('\nYou guessed the correct word' )
           break
    else:
         print('\nGame Over !!! You Lost, Number of attempt to guess the word is over')
    continue_playing = input('\nDo you want to continue playing ? \n(y/n): ').lower() 
    if continue_playing == 'y':
        hangman()      
    else:
        print('\nThanks for playing!')       

        
        

    

if  __name__ == '__main__':
    hangman()
