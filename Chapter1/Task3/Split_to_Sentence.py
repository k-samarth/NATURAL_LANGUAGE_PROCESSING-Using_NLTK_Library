import re

paragraph = "Hello there, I am Samarth. How are doing? I love coding in python and hope you will love it as well. Keep learning, we will rock it together! Why don't you try something new with this"

sentence = re.split(r"[.?!]",paragraph)
print(sentence)
