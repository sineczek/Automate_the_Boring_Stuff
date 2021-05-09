import webbrowser, sys, pyperclip

sys.argv # gdy przekaemy argumenty ['mapit.py', 'ul.', 'Nazwa', 'numer']

# check if commandline arguments ware passed
if len(sys.argv) > 1: # jeśli tak to
    # ['mapit.py', 'ul.', 'Nazwa', '123'] --> 'ul. Nazwa 123'
    address = ' '.join(sys.argv[1:]) # pomija mapit.py
else: # jeśli nie było to wklej to co w schowku
    address = pyperclip.paste()

#przejście na strone https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)









