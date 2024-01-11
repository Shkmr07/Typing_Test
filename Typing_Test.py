import random

def sentence_generator():
    # This functions is to generate random sentences through random library
    test_string =  [
        "The quick brown fox jumps over the lazy dog","My name is Amit","Hello, world!","I love to play football",
        "Python is a great programming language","The weather is really nice today","Health is wealth",
        "Artificial intelligence is fascinating","Reading books is a good habit","Music can change the mood"]
        
    Random_test = random.choice(test_string)
    return Random_test