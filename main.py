import random
import os
import word_list

wl = word_list.words

# Variables

word_1 = random.choice(wl)
word_2 = random.choice(wl)
word_3 = random.choice(wl)
word_4 = random.choice(wl)
nums = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
]

# Function
pass_1 = word_1.capitalize() + word_2.capitalize() + word_3.capitalize() + word_4.capitalize()

pass_2 = pass_1 + random.choice(nums) + random.choice(nums) + random.choice(nums) + random.choice(nums)

print(pass_2)