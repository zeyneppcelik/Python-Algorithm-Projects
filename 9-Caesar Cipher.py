alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direct, p_text, s_amount):
    end_text=''
    if direct=='decode':
        s_amount*=-1

    for char in p_text:
        if char not in alphabet:
            end_text+=char
        else:
            position = alphabet.index(char)
            if (position+s_amount)>=len(alphabet):
                end_text+= alphabet[(position+s_amount)%len(alphabet)]
            else:
                end_text+= alphabet[position+s_amount]
    print(f"The {direct}d text is {end_text}")

cont='yes'

while cont=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))%26

    caesar(direct=direction, p_text=text, s_amount=shift)

    cont=input("Type 'yes' to restart the chiper or type 'exit' to exit:\n").lower()
    if cont=='exit':
        print('GOODBYE :)')