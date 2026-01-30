print("""
   ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗ 
  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
  ██║     ███████║█████╗  █████╗  ███████║██████╔╝
  ██║     ██╔══██║██╔══╝  ██╔══╝  ██╔══██║██╔══██╗
  ╚██████╗██║  ██║███████╗███████╗██║  ██║██║  ██║
   ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

        ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
       ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
       ██║     ██║██████╔╝███████║█████╗  ██████╔╝
       ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
       ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
        ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(text, shift_amount, encode_or_decode):
    result_text = ""

    if encode_or_decode == "encode":
        for alpha in text:
            if alpha in alphabet:
                position = alphabet.index(alpha)
                new_position = (position + shift_amount) % 26
                result_text += alphabet[new_position]
            else:
                result_text += alpha

        print("Encrypted text:", result_text)

    elif encode_or_decode == "decode":
        for alpha in text:
            if alpha in alphabet:
                position = alphabet.index(alpha)
                new_position = (position - shift_amount) % 26
                result_text += alphabet[new_position]
            else:
                result_text += alpha

        print("Original text:", result_text)
        



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
ceaser(text,shift,direction)
