import random

imie = input('Jak się zowiesz ?\n')
print(f'Witaj {imie}! Wymyśliłem sobie jakąś liczbę pomiędzy 1 a 20. \n'
      f'Czy uda Ci się ją odgadnąć w 5 próbach?')
magicznaLiczba = random.randint(1, 20)

for l in range(1, 6):
    print('Gotów?')
    strzal = int(input(f'Strzelaj ! '))
    if strzal > magicznaLiczba:
        print('Za wysoko przyjacielu!')
    elif strzal < magicznaLiczba:
        print('Za nisko przyjacielu!')
    else:
        break

if strzal == magicznaLiczba:
    print(f'Nieźle {imie}! Bullseye!\n'
          f'Faktycznie myślałem o {magicznaLiczba}!\n'
          f'Trafiłeś za {l} razem!')
else:
    print(f'Słabo, słabo {imie} :( \n'
          f'Myślałem o {magicznaLiczba}!\n'
          f'Zagrajmy raz jescze !')
