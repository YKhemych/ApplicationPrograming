import re
f = open('text1.txt', mode='r', encoding='utf-8')
content = f.readlines()
pattern = re.compile('\w+')
words = 0
for line in content:
    for word in re.findall(pattern, line):
        words += 1

print("Number of words: %2.0f" %words)