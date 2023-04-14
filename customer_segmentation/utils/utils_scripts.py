import numpy as np
import random
import string


def random_word(length):
    # create a list of all letters
    letters = string.ascii_letters + string.digits
    # generate a random word of the specified length
    word = ''.join(random.choice(letters) for i in range(length))
    return word