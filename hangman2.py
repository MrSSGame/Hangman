import random


def read_file(file_name):
    ask_file_name()
    file = open(file_name,'r')
    return file.readlines()


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index]
    return word


def select_random_letter_from(word):
    random_index = random.randint(0, len(word) - 2)
    letter = word[random_index]
    print('Guess the word: ' + word[:random_index] + "_" + word[random_index+1:])
    return letter, random_index


def get_user_input():
    return input('Guess the missing letter: ')


def show_answer(answer, selected_word, missing_letter_index):
    """
    TODO Step 1 - Show better results messages
    """

    if answer == selected_word[missing_letter_index]:
     print("Well Done! You are awesome")
    else:
         print("Wrong Do better next time")
         



# TODO: Step 2
def ask_file_name():
    """
    TODO Step 2 - Update to prompt user for filename to use for words
    """
    print("Please select a file from these options:Immediate_words.txt,Kids_words.txt,Python_words.txt")
    file_choose = input("Please choose a file from the above: ")
    
    if file_choose == "Immediate_words.txt":
        file_choose = '/home/c5r5s6/problems/submission_001-hangman-conditional/Immediate_words.txt'
    elif file_choose == "Kids_words.txt":
        file_choose = '/home/c5r5s6/problems/submission_001-hangman-conditional/Kids_words.txt'
    elif file_choose == "Python_words.txt":
        file_choose = '/home/c5r5s6/problems/submission_001-hangman-conditional/Python_Words.txt'
    else:
         file_choose = '/home/c5r5s6/problems/submission_001-hangman-conditional/short_words.txt'

                        
    return file_choose




def run_game(file_name): 
    """
    You can leave this code as is, and only implemented above where the code comments prompt you.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    missing_letter, letter_index = select_random_letter_from(word)
    answer = get_user_input()
    show_answer(answer, word, letter_index)


if __name__ == "__main__":
    words_file = ask_file_name()
    run_game(words_file)

