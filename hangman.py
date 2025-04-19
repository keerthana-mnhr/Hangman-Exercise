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
    print( f'Guess the letters in the word \n Its a {word_length} letter word'  )
    user_guessed_letters = list('_' * word_length)
    print(user_guessed_letters)
    selected_word_letters = list(selected_word)
    while number_of_remaining_attempts > 0:

        user_input = input('Enter the guessed letter: ')
        if user_input.isalpha():
            number_of_remaining_attempts -=1
            if user_input in selected_word_letters:
                for l in range(word_length):
                    if selected_word_letters[l]== user_input:
                        user_guessed_letters[l]= user_input         
            else:
                print('Wrong letter!! The letter doesnt exists in the word')


        else:
            print('Invalid letter !! Only alphabetical choise is allowed') 

        print(f'{user_guessed_letters}')   
    

if  __name__ == '__main__':
    hangman()
