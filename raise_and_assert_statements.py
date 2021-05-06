#raise Exception ('Na dziś mam dość. 12h pracy...')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception ('Only one symbol')
    if (width < 2) or (height < 2):
        raise Exception ('Width and height must be greater than 2.')


    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)


boxPrint('x', 15, 5)


market_2nd = {'NS': 'green', 'EW' : 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow'
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'

        assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)




switchLights(market_2nd)