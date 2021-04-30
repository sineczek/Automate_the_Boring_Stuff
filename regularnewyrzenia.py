
"""
RE - wyrażenia regularne

klasy znaków - character classes
\d - cyfra 0 - 9
\D - wszystkie inne znaki
\w - każda litera, cyfra lub "podkreślony znak"
\W - każdy znak który nie jest literą, cyfrą lub "podkreślonym znakiem"
\s - każda spacja, tab czy znak końca linii
\S - każdy znak niebędący spacją, tab, czy końcem linii

('[aeiouAEIOU]') - tworzenie własnej klasy samych samogłosek
('^[aeiouAEIOU]') - ^ oznacza wszystko inne

^ - carrot ;] tak sie po ang nazywa

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

search() wyrażenia regularnego szuka pierwszego zgodnego
findall() wyrażenia regularnego szuka wszystkich trafień, np. wszystkie nr na stronie

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