

def encode(message, security_num, key_str):
    encoded_message = ''
    key_index = 0
    message_length = len(message)
    keys_num = message_length // security_num

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

def decode(message, security_num, key_str):
    decoded_message = ''
    key_index = 0
    message_length = len(message)
    keys_num = message_length // security_num

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


mess = "Hello my dear friend"
mess2 = "Lippq oa ghds gsjfoe"
print(encode(mess,5,"42311"))
print(decode(mess2,5,"42311"))
