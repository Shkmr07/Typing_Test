from termcolor import colored
import random
import msvcrt
import time

# Here, I intiallze one empty dictionary
leaderboard = {}

def Leaderboard():
    # This function is showing ranking with their Name and WPM 
    if leaderboard:
        print("Here is a Leaderboard ->")
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda item: (-item[1], item[0]))
        rank = 0
        last_wpm = None
        for name, wpm in sorted_leaderboard:
            if wpm != last_wpm:
                rank += 1
            print(str(rank) + ".", name, ":", round(wpm), "WPM")
            last_wpm = wpm
    
    else: 
        print("No users have completed the typing test yet. The leaderboard is empty.")


def sentence_generator():
    # This functions is to generate random sentences through random library
    test_string =  [
    "The quick brown fox jumps over the lazy dog. This sentence contains all the letters of the English alphabet.",
    "My name is Amit. I'm a software engineer by profession and I have a deep interest in artificial intelligence.",
    "Hello, world! This is often the first program written by people learning to code.",
    "I love to play football. It's a sport that requires both physical prowess and strategic thinking.",
    "Python is a great programming language. It's simple, yet powerful and used in a variety of fields.",
    "The weather is really nice today. It's sunny with a slight breeze, perfect for outdoor activities.",
    "Health is wealth. It's important to take care of our health as it's our most valuable asset.",
    "Artificial intelligence is fascinating. It's a field that's constantly evolving and pushing the boundaries of what's possible.",
    "Reading books is a good habit. It can broaden your horizons and deepen your understanding of the world.",
    "Music can change the mood. A good song can lift your spirits and make you feel better."
]
        
    Random_test = random.choice(test_string)
    return Random_test

def typing_test(test_string,username):
    # In this function we check the user type correct character or not. if not we coun the mistakes
    # And along with finding the (Words per minutes and how much time taken by user to write sentence)
    mistakes,word_count = 0,len(test_string.split())
    print( "Type this sentence: " + "\033[1m"  + test_string + "\033[0m")
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

def main():
    # This are the instructions the user can see in terminal 
    print(colored("########## Typing Test ##########","blue"))
    print(colored("1. Start Typing Test","yellow"))
    print(colored("2. Show Leaderboard","yellow"))
    print(colored("3. Exit","yellow"))
    # Here i take user choice what it want
    choices = int(input("Enter your choices (1/2/3): "))
    print()

    # this while loop runs until user not press 3
    while choices != 3:
        if choices == 1:
            username = input(colored("Enter the username: ","green"))
            print()
            ans = sentence_generator()
            typing_test(ans,username)

        elif choices == 2:
            print()
            Leaderboard()

        else:
            print()
            print(colored("Invaild Input","red"))

        print()
        print(colored("1. Start Typing Test","yellow"))
        print(colored("2. Show Leaderboard","yellow"))
        print(colored("3. Exit","yellow"))
        choices = int(input("Enter your choices (1/2/3): "))
        
main()