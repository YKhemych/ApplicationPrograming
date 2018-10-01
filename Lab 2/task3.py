import re
import xml.etree.cElementTree as ET
from collections import Counter

pattern = re.compile('\w+\'\w+|\w+')
words = []
with open('../Lab 2/a.txt', mode='r', encoding='utf-8') as a:
    for line in a:
        for word in re.findall(pattern, line):
            words.append(word)

print(words)

counter = Counter()
for word in words:
    counter[word] += 1

print(counter)

root = ET.Element("root")
for word in counter:
    ET.SubElement(root, "word", number=str(counter[word])).text = word
tree = ET.ElementTree(root)
tree.write("../Lab 2/unique.xml", encoding='utf-8')