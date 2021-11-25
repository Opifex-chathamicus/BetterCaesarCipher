import divisor_util as divutil
from fragmentation_cipher import FragmentationCipher

def show_divisors(divisor_list):
        print(*divisor_list, sep= ", ")

cipher = FragmentationCipher()
cipher.show_info()
command = int(input("Enter a command:\n[1] Encrypt\n[2] Decrypt\n[3] Show info\n[0] Exit\n-> "))

while command != 0:

    message = input("Enter your message:\n")
    message_length = len(message)

    divisors = divutil.find_divisors(message_length)
    print("Possible divisors: ")
    show_divisors(divisors)

    fragments_num = int(input("Enter the number of fragments (must be one of the divisors):\n"))
    key_series = input("Enter a series of keys, one for each fragment:\n")

    if command == 1:
        print(cipher.encode(message, fragments_num, key_series))
    elif command == 2:
        print(cipher.decode(message, fragments_num, key_series))
    elif command == 3:
        print((cipher.show_info()))
    else:
        print("Invalid command!\n")

    cipher.show_info()
    command = int(input("Enter a command:\n[1] Encrypt\n[2] Decrypt\n[3] Show info\n-> "))