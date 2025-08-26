import random

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def main():
    user_input = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    if user_input.lower() in ["e", "encrypt"]:
        encrypt()
    elif user_input.lower() in ["d", "decrypt"]:
        decrypt()
    else:
        return


def encrypt():
    s = get_seed_a()
    message = input("Please enter the sentence you want to cypher. ")
    words = message.casefold().split()
    encrypted_words = []
    current_seed = s

    for word in words:
        encrypted_word = ""
        random.seed(current_seed)
        cypher = alphabet.copy()
        random.shuffle(cypher)
        for letter in word:
            if letter in alphabet:
                position = alphabet.index(letter)
                l = cypher[position]
                encrypted_word = encrypted_word + l
            else:
                encrypted_word = encrypted_word + letter
        encrypted_words.append(encrypted_word)
        current_seed = current_seed + 1
    
    result = ' '.join(encrypted_words)
    print(f"Your cyphered text is {result}. Your seed is {s}.")

def decrypt():
    current_seed = int(input("Please enter your seed "))
    ctext = input("Please enter your cyphered text ")
    words = ctext.split()
    decrypted_words = []
    
    for word in words:
        decrypted_word = ""
        random.seed(current_seed)
        cypher = alphabet.copy()
        random.shuffle(cypher)
        for letter in word:
            if letter in cypher:
                position = cypher.index(letter)
                l = alphabet[position]
                decrypted_word = decrypted_word + l
            else:
                decrypted_word = decrypted_word + letter
        decrypted_words.append(decrypted_word)
        current_seed = current_seed + 1
    
    result = ' '.join(decrypted_words)
    print (f"Your uncyphered text is {result}")


def get_seed_a():
    s = random.randrange(0, 10000)
    return s



main()