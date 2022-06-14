message = input()
keytext = input()


letters = 'abcdefghijklmnopqrstuvwxyz'
d = {letter: ind for ind,letter in enumerate(letters)}

def vigenere_cipher(message,key_):
    keylen = len(key_)
    other_symbols = ['.',',',':',';','!','@','#','$','%','^','&','*','(',')','_',
                     '-','+','/','"','?',' ','1','2','3','4','5','6','7','8','9','0']
    
    output_text = ''
    for index,character in enumerate(message):
        if character in other_symbols:
            output_text += character
              
            
        else:
            i = (d[character.lower()] + d[key_[index % keylen].lower()])% 26
            output_text += letters[i].upper() if character.isupper() else letters[i]
            
    return output_text


print(vigenere_cipher(message,keytext))




