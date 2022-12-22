# since all wifi paswords are stord in an encrypted library called hashlib(also known as md5)


import hashlib

flag = 0
counter = 0

pass_hash = input("Enter md5 hash: ")

wordlist = input("File name: ")

try:
    pass_file = open(wordlist, "r")
except:
    print("Sorry :( the file does not exist")
    quit()

for word in pass_file:

    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    print(word)
    print(digest)
    print(pass_hash)
    counter += 1

    if digest == pass_hash:
        print("Password located")
        print("Password: " + word)
        break

# incase the wifi password is not found
if flag == 0:
    print("Password has not been found please update the network. ")
