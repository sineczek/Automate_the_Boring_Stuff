
"""
RE - wyrażenia regularne

\d - cyfra

? oznacza że coś jest opcjonalne czyli może 0 lub 1 raz wystąpić
aby wyszukać ? używamy \?

* oznacza że coś jest opcjonalne czyli może 0 lub wiele razy wystąpić
aby wyszukać * używamy \*

+ oznacza że musi wystąpić 1 lub więcej razy
aby wyszukać + używamy \+

dokłdnie ileś razy {x}
{x,} - x lub więcej
{x,y} - pomiędzy x a y - szuka maksymalnej możliwej ilości
{x,y}? - pomiędzy x a y -  szuka minimalnej możliwej ilości
"""




import re # RegularExpressions
batRegex = re.compile(r'Bat(wo)?man')
print(batRegex.search("Adventures of Batman"))
print(batRegex.search("Adventures of Batwoman"))
print(batRegex.search("Adventures of Batwowowowoman"))




batRegex = re.compile(r'Bat(wo)*man')
print(batRegex.search("Adventures of Batman"))
print(batRegex.search("Adventures of Batwoman"))
print(batRegex.search("Adventures of Batwowowowoman"))



batRegex = re.compile(r'Bat(wo)+man')
print(batRegex.search("Adventures of Batman"))
print(batRegex.search("Adventures of Batwoman"))
print(batRegex.search("Adventures of Batwowowowoman"))




ha = re.compile(r'ha{3}') # dokłdnie 3x ha
print(ha.search('powiedział hahaha'))