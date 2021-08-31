############################################################################
############################# Dear attacker(s) #############################
############### 'EzTextCrypt' is designed for easy reversing ###############
########### just check my algorithm and read variable names LOL ############
#################### I hope you enjoy to reversing :) ######################
############################################################################

import time
import codecs
import random
import sys
import nacl.secret
import nacl.utils
import os

banner = ''' 
███████ ███████ ████████ ███████ ██   ██ ████████  ██████ ██████  ██    ██ ██████  ████████ 
██         ███     ██    ██       ██ ██     ██    ██      ██   ██  ██  ██  ██   ██    ██    
█████     ███      ██    █████     ███      ██    ██      ██████    ████   ██████     ██    
██       ███       ██    ██       ██ ██     ██    ██      ██   ██    ██    ██         ██    
███████ ███████    ██    ███████ ██   ██    ██     ██████ ██   ██    ██    ██         ██    
                    CREATED BY WACHIRAWITCH Y. (DISCORD: Custard#2161)                   
'''
SUCCESS_PREFIX = '[+] '
ERROR_PREFIX = '[-] '
KEY = b'900d 1vCk H@V3 FvN MY F213Nd ^_^'
SEED = int.from_bytes(KEY, "little")


def read_file(filename):
    with open(file=filename, mode='r', encoding='utf8') as file:
        text = file.read()
    return text


def write_file(data):
    with open(file='output.txt', mode="w", encoding='utf8') as file:
        file.write(data)
        file.close()
    print(SUCCESS_PREFIX + 'Output file exported.')


def shuffle(data):
    data = list(data)
    random.seed(SEED)
    i = len(data)
    while i > 1:
        i = i-1
        num = random.randint(0, i)
        c = data[num]
        data[num] = data[i]
        data[i] = c
    return ''.join(data)


def base69_encode(data):
    big_int = int.from_bytes(data, "big")
    charset = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮⴰⴱⴳⴷⴹⴻⴼⴽⵀⵃⵄⵅⵇⵉⵊⵍⵎⵏⵓⵔⵕⵖⵙⵚⵛⵜⵟⵡⵢⵣⵥ" #Thai & Tifinagh alphabets
    charset = shuffle(charset)
    temp = "$อีซี่คริปต์$."
    while big_int > 0:
        value = big_int % 69
        temp = temp + charset[value]
        big_int = big_int // 69
    list(temp).reverse()
    return ''.join(temp)


def encrypt(data):
    _data = shuffle(data) #TIPS; if you want to reversing, please don't use this original function, just reverse it ;)
    cryptz = nacl.secret.SecretBox(KEY)
    nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
    ciphertxt = cryptz.encrypt(_data.encode(), nonce=nonce)
    if len(ciphertxt) == len(_data.encode()) + cryptz.NONCE_SIZE + cryptz.MACBYTES:
        h, t = nonce[:20], ciphertxt[20:24]
        return base69_encode(t[::-1]+ciphertxt.ciphertext+h)
    else:
        print(ERROR_PREFIX + 'Authentication Failed.')
        exit(1)
        return 0


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    try:
        dropped_file = sys.argv[1]
        data = read_file(dropped_file)
        if len(data) >= 32:
            print(SUCCESS_PREFIX + f'plain text: \n {data}\n')
            start = time.time()
            ciphertext = encrypt(data)
            end = time.time()
            print(SUCCESS_PREFIX + f'cipher text: \n {ciphertext}\n')
            write_file(ciphertext)

            print('\n' + SUCCESS_PREFIX + f'Successfully encrypted plain text with {len(data)} characters/{sys.getsizeof(data)} bytes in {end-start}s.')
        else:
            print(ERROR_PREFIX + 'Invalid input, string length must reach to 32 chars.')

        input("\nPress any key to exit..\n")

    except IndexError:
        try:
            print("Input plain text below [Ctrl+D(Unix)] or [Ctrl+Z and Enter(Windows)] to send data.")
            data = sys.stdin.read().rstrip("\n")
            if len(data) >= 32:
                print(SUCCESS_PREFIX + f'plain text: \n{data}\n')
                start = time.time()
                ciphertext = encrypt(data)
                end = time.time()
                print(SUCCESS_PREFIX + f'cipher text: \n{ciphertext}\n')
                write_file(ciphertext)

                print('\n' + SUCCESS_PREFIX + f'Successfully encrypted plain text with {len(data)} characters/{sys.getsizeof(data)} bytes in {end-start}s.')
            else:
                print(ERROR_PREFIX + 'Invalid input, string length must reach to 32 chars.')

            input("\nPress any key to exit..\n")

        except EOFError:
            input("\nPress any key to exit..\n")

    except UnicodeError:
        print(ERROR_PREFIX + "Invalid file input, EzTextCrypt support only 'UTF-8' text file.")
        input("\nPress any key to exit..\n")

    except Exception as e:
        input("\nPress any key to exit..\n")


if __name__ == '__main__':
    main()