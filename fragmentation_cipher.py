import sys

class FragmentationCipher:
    
    def help(self):
        print("Help")

    def show_info(self):

        print("This is a Fragmentation Cipher tool.\n")
        print("Every message will be divided into equal fragments (substings).\n")
        print("The number <F> of fragments (substrings) must be a divisor of the message's length.\n")
        print("Example: 'Hello my dear friend' has a length of 20 and can thus be divided into 1, 2, 4, 5, 10 and 20 Fragments.\n")
        print("A string of keys must then be inputed for every character in each fragment to be shifted by.\n")
        print("Example: If 'Hello my dear friend' has been divided into 5 fragments and the key string is '12345',")
        print("every character in the first fragment will be shifted by 1, every character in the second fragment by 2 and so on.\n")
        print("'Hello my dear friend' becomes 'Ifmmq oa ghdv jvnjsi' after the encryption process ends.")
        print("In order for a decryption to be performed, the person decrypting must know the number of fragments and the key string.\n")
        print("This makes Fragmentation Cipher a bit harder to brute-force than Caesar's Shift")
        print("as it has 24^k possible encryption combinations (where k is the number of keys which must be a divisor of the length of the message).")
        print("Since the algorithm uses a string of integers as keys, which means that unlike the Vigenere algorithm,")
        print("there is no passphrase that can be guessed.")
        print("The Fragmentation aspect of the algorithm adds another element of difficulty both for encrypting and decrypting messages.\n")
        
    def cli_interface(self):
        arguments = sys.argv

        if len(arguments) != 5:
            self.show_info()
        else:
            if arguments[1] == '-e':
                encoded_message = self.encode(arguments[2], arguments[3], arguments[4])
                return encoded_message
            elif arguments[1] == '-d':
                decoded_message = self.decode(arguments[2], arguments[3], arguments[4])
                return decoded_message
                

    def encode(self, message, fragments_num, key_str):
        encoded_message = ''
        key_index = 0
        message_length = len(message)
        keys_num = message_length // int(fragments_num)


        for i in range(0, message_length + 1, keys_num):
            encoded_sub_message = ''
            sub_message = message[i:keys_num+i]
            
            for j in range(len(sub_message)):
                character_to_shift = sub_message[j]

                if(ord(character_to_shift) != 32):
                    if(character_to_shift.isupper()):
                        encoded_sub_message += chr((ord(character_to_shift) + int(key_str[key_index]) - 65) % 26 + 65)
                    else:
                        encoded_sub_message += chr((ord(character_to_shift) + int(key_str[key_index]) - 97) % 26 + 97)
                else:
                    encoded_sub_message += ' '
                
            encoded_message += encoded_sub_message
            key_index += 1

        return encoded_message

    def decode(self, message, fragments_num, key_str):
        decoded_message = ''
        key_index = 0
        message_length = len(message)
        keys_num = message_length // int(fragments_num)

        for i in range(0, message_length + 1, keys_num):
            decoded_sub_message = ''
            sub_message = message[i:keys_num+i]

            for j in range(len(sub_message)):
                character_to_shift = sub_message[j]

                if(ord(character_to_shift) != 32):
                    if(character_to_shift.isupper()):
                        decoded_sub_message += chr((ord(character_to_shift) - int(key_str[key_index]) - 65) % 26 + 65)
                    else:
                        decoded_sub_message += chr((ord(character_to_shift) - int(key_str[key_index]) - 97) % 26 + 97)
                else:
                    decoded_sub_message += ' '
                
            decoded_message += decoded_sub_message
            key_index += 1
        
        return decoded_message


if __name__ == "__main__":
    cipher = FragmentationCipher()
    print(cipher.cli_interface())
    #print(cipher.encode("Hello my dear friend",5,"12345"))
    #print(cipher.decode("Ifmmq oa ghdv jvnjsi", 5, "12345"))
