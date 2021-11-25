import sys

class FragmentationCipher:
    
    def help(self):
        print("Help")

    def show_info(self):
        print("Info")

    def cli_interface(self):
        arguments = sys.argv

        if len(arguments) != 5:
            print("error")
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
