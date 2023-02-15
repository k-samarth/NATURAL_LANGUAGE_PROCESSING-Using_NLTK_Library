import re

sentence = "Hello there, I am Samarth. How are doing? I love coding in python and hope you will love it as well. Keep learning, we will rock it together! Why don't you try something new with this"

comma_seperated = re.split(r"[,]",sentence)
print(comma_seperated)
