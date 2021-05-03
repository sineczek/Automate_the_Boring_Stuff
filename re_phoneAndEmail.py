#! python 3

import re
import pyperclip  # do obsługi schowka

# Create a regex fore phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d))?       #area code (optional)
(\s|-)                          #first seperator
\d\d\d                          # first 3 digits
-                               # seperator
\d\d\d\d                        # last 4 digits
(((ext(\.)?\s|x)                # extension (optional)
 (\d{2,5})))?                    # extension number (optional)
)
''', re.VERBOSE)

# Create a regex for emails
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+        # name part
@                      # @
[a-zA-Z0-9_.+]+        # domain name part
''', re.VERBOSE)

# Get text off the clipboard
text = pyperclip.paste() #skleja to co w schowku

# Extract the emails/phones form this text
extractedPhone = phoneRegex.findall(text)
extractedEmails = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted emails/phones to the clipboard
results = '\n'.join((allPhoneNumbers)) + '\n'.join(extractedEmails)
pyperclip.copy(results) #kopiuje wyniki do schowka