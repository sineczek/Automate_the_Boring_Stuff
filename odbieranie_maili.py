import imapclient, pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('login@gmail.com', 'password')

conn.select_folder('INBOX', readonly=True)  # aby przypadkiem nie pokasować maili

uids = conn.search(['SINCE 20-Aug-2020'])  # maile od 20 sierpnia 2020, zwraca UIDs maili

rawmsg = conn.fetch(['uid'], ['BODY[]', 'FLAGS'])
msg = pyzmail.PyzMessage.factory(rawmsg[uid][b'BODY[]']) # parsowanie maile, trzeba przekazać uid oraz b'BODY[]'

msg.get_subject() # pobranie tematu
msg.get_address('from') # od kogo
msg.get_address('to') # do kogo | można przekazć też np. bcc, cc etc.
msg.text_part # czy była część w plaintexście, jak None to brak textu
msg.html_part # czy ma część html

msg.text_part.get_payload().decode('UTF-8') # i to daje dopiero treść maila

conn.logout() # zamknięcie połączenia