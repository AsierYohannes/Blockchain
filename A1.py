from urllib.request import urlopen, hashlib
sha1hash= input("Type in the hash you wish to crack.\n")
List_of_passwords = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(), 'utf-8')
for guess in List_of_passwords.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess,'utf-8')).hexdigest()
    if hashedGuess == sha1hash:
        print("The password is ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print("Password guess ",str(guess)," does not match, attempting next effort")
print("Password not in database.")
