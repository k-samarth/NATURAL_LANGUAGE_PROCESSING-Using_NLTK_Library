from nltk.tokenize import TreebankWordTokenizer

s = '''Hello there, I am Samarth. How are doing? I love coding in python and hope you will love it as well. Keep learning, we will rock it together! Why don't you try something new with this. Good muffins cost $3.88\nin New York.  Please buy me two of them.\n\nThanks.'''

tok1 = TreebankWordTokenizer()
print(tok1.tokenize(s))
