import random
import string

while True:
    print('GENERATOR KLUCZY" \n'
            'Generuje losowe klucze i umożliwia ich zapis do pliku.\n' 'Twój niepowtarzalny klucz to:  ')
    
#     list = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h','I', 'i', 'J', 'j', 'K', 'k',
#             'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v',
#             'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '!', '@', '#', '$', '%', '^', '&', '*', '?',]
#     array = []
    length = 20
    password = ''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=length,))
    print(password)

    if input('Chcesz kontunuować? t - Tak, generuj kolejny klucz / dowolny klawisz - Nie, zakończ program.\n' 'Wybór zatwierdź ENTEREM ') != 't':
        break