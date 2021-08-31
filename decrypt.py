import time
import codecs
import random
import sys
import nacl.secret
import nacl.utils

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


def unshuffle(data):
    data = list(data)
    random.seed(SEED)
    i = len(data)
    idx = []
    while i > 1:
        i = i-1
        num = random.randint(0, i)
        idx.append(num)
        idx.append(i)
    j = len(idx) - 1
    while j > 0:
        c = data[idx[j-1]]
        data[idx[j-1]] = data[idx[j]]
        data[idx[j]] = c
        j = j-2

    return ''.join(data)


def base69_decode(data):
    data = data.replace('$อีซี่คริปต์$.', '')
    list(data).reverse()
    ''.join(data)
    charset = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮⴰⴱⴳⴷⴹⴻⴼⴽⵀⵃⵄⵅⵇⵉⵊⵍⵎⵏⵓⵔⵕⵖⵙⵚⵛⵜⵟⵡⵢⵣⵥ" #Thai & Tifinagh alphabets
    charset = shuffle(charset)
    big_int = 0
    for i in range(len(data)):
        idx = charset.index(data[i])
        big_int = big_int + (idx * pow(69, i))
    data = big_int.to_bytes((big_int.bit_length() + 7)//8, "big")
    return data


def decrypt(data):
    data = base69_decode(data)
    data = data[-20:] + data[:4][::-1] + data[4:-20]
    box = nacl.secret.SecretBox(KEY)
    return unshuffle(box.decrypt(data).decode())


def main():
    print(banner)
    try:
        dropped_file = sys.argv[1]
        data = read_file(dropped_file)
        if len(data) >= 32:
            print(SUCCESS_PREFIX + f'cipher text: \n {data}\n')
            start = time.time()
            plaintext = decrypt(data)
            end = time.time()
            print(SUCCESS_PREFIX + f'plain text: \n {plaintext}\n')
            write_file(plaintext)

            print('\n' + SUCCESS_PREFIX + f'Successfully decrypted cipher text with {len(data)} characters/{sys.getsizeof(data)} bytes in {end - start}s.')
        else:
            print(ERROR_PREFIX + 'Invalid input, string length must reach to 32 chars.')

        input("\nPress any key to exit..\n")

    except IndexError:
        try:
            print("Input cipher text below [Ctrl+D(Unix)] or [Ctrl+Z and Enter(Windows)] to send data.")
            data = sys.stdin.read().rstrip("\n")
            if len(data) >= 32:
                print(SUCCESS_PREFIX + f'cipher text: \n{data}\n')
                start = time.time()
                plaintext = decrypt(data)
                end = time.time()
                print(SUCCESS_PREFIX + f'plain text: \n{plaintext}\n')
                write_file(plaintext)

                print('\n' + SUCCESS_PREFIX + f'Successfully decrypted cipher text with {len(data)} characters/{sys.getsizeof(data)} bytes in {end - start}s.')
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
