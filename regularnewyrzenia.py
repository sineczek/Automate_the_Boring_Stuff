
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
    re.IGNORECASE lub re.I i nie trzeba pisać dużymi i małymi (jako 2 argument)
^ - carrot ;] tak sie po ang nazywa

r'^Hello' - poszukuje ale tylko na początku
r'hello$' - poszukuje ale tylko na końcu

. - pojedynczy znak, prócz nowej linii
    re.DOTALL pozwoli również nowe linie (jako 2 argument)
.* - każdy ciąg, ('First Name: (.*) Last Name: (.*)')  -> tupa z imieniem i nazwiskiem
.*? - minimalna ilośc zgadzająca się

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
sub() - zamienia (co, w czym), ale też można np. \1 czyli z grupy 1, \2 z gdupy 2 etc.


re.VERBOSE - można wówczas podzielić txt na linie i dodawać komentarze
np. re.compile(r'''
(\d\d\d)|       # kierunkowy np. 012 lub
(\d\d)          # samo 12
\s              # spacja/przerwa
(\d\d\d)        # pierwsze 3 cyfry
(\s)|           # przerwa
-               # - między
(\d\d)          # 1 blok 2 cyfr
(\s)|           # przerwa
-               # - między
(\d\d)          # 2 blok 2 cyfr
''', re.VERBOSE | re.DOTALL | re.I) # | pozwala użyć więcej argumentów


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