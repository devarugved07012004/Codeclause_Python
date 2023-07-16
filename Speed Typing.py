import time
def speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)
    input("Press Enter when you are ready.")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    words_per_minute = calculate_words_per_minute(user_input, elapsed_time)
    print("Time taken: {:.2f} seconds".format(elapsed_time))
    print("Words per minute: {:.2f}".format(words_per_minute))
def calculate_words_per_minute(user_input, elapsed_time):
    words = user_input.split()
    word_count = len(words)
    minutes = elapsed_time / 60
    words_per_minute = word_count // minutes
    return words_per_minute
speed_typing_test()