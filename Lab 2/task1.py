import re
f = open('../Lab 2/text1.txt', mode='r', encoding='utf-8')
content = f.readlines()
pattern = re.compile('\w+\'\w+|\w+')
words = 0
for line in content:
    for word in re.findall(pattern, line):
        words += 1

print("Number of words: %2.0f" %words)