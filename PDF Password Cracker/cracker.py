# Modules Needed:
# i. pikepdf
# ii. tqdm

# command to install modules:
# => pip install pikepdf
# => pip install tqdm

# AlSO WE NEED wordlist.txt

# A WORDLIST IS A LIST OF PASSWORDS THAT ARE COLLECTED IN PLAIN TEXT

import pikepdf  
from tqdm import tqdm  

passwords = [line.strip() for line in open("wordlist.txt")]

for password in tqdm(passwords, "Decrypting PDF"):
    try:
        with pikepdf.open("PDF_HERE.pdf", password=password) as pdf:
            print("\n[+] Password found:", password)
            break
    except pikepdf._pqdf.PasswordError as e:
        # WRONG PASSWORD,JUST CONTINUE IN THE LOOP
        continue
