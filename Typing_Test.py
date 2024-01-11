from termcolor import colored
import random
import msvcrt
import time

leaderboard = {}

def sentence_generator():
    # This functions is to generate random sentences through random library
    test_string =  [
        "The quick brown fox jumps over the lazy dog","My name is Amit","Hello, world!","I love to play football",
        "Python is a great programming language","The weather is really nice today","Health is wealth",
        "Artificial intelligence is fascinating","Reading books is a good habit","Music can change the mood"]
        
    Random_test = random.choice(test_string)
    return Random_test

def typing_test(test_string,username):
    # In this function we check the user type correct character or not. if not we coun the mistakes
    # And along with finding the (Words per minutes and how much time taken by user to write sentence)
    mistakes,word_count = 0,len(test_string.split())
    print("Type this sentence :" , test_string)
    print("Start Typing in next line ->")

    start_time = time.time()
    
    for char in test_string:
        while True:
            user_input = msvcrt.getch().decode('utf-8')
            if user_input == char:
                print(user_input, end='', flush=True)
                break
            else: mistakes += 1

    end_time = time.time()

    elapsed_time = end_time - start_time
    wpm = (word_count / elapsed_time) * 60

    leaderboard[username] = wpm

    print(colored("\nCongratulations! You have completed the typing test.","green"))
    print(colored(f"You made {mistakes} mistakes.","red"))
    print("Number of words typed: ", word_count)
    print("Time taken for the test: ", round(elapsed_time, 2), "seconds.")
    print("Your typing speed is", round(wpm), "words per minute.")
