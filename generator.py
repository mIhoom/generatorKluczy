import random
import string
import sys


while True:
        print('GENERATOR KLUCZY" \n'
        'Generuje losowe klucze i umożliwia ich zapis do pliku.\n')
                
        length = 20
        password = ''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=length,))
        print("Twój niepowtarzalny klucz to: ",password,' \n' "*Klucz zostanie zapisany do pliku .txt w miejscu lokalizacji programu"' \n')

        if input('Chcesz kontunuować? \n' 't - Tak, generuj i zapisz kolejny klucz / dowolny klawisz - Nie, zakończ program.\n' 'Wybór zatwierdź ENTEREM ') != 't':
                file_path = 'twojKlucz.txt'
                sys.stdout = open(file_path, "w")
                print("Twój niepowtarzalny klucz to: ",password)
                break