import random
import string
import sys
import tkinter

def generator():
    while True:
        length = 20
        password = ''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=length,))
        print(password)
        l3.config(text = password)
        file_path = 'twojKlucz.txt'
        sys.stdout = open(file_path, "w")
        print("Klucz to: ",password)
        break

root = tkinter.Tk()
root.title("Generator kluczy")
root.geometry('350x120')

l = tkinter.Label(root, text = "Generuje losowe klucze i zapisuje je do pliku", font = ('Calibri', 12,), width = '40',)
l.place(x = 12, y = 5)
l2 = tkinter.Label(root, text = "Twój klucz: ", font = ('Calibri', 12), width = '10', fg = 'red')
l2.place(x = 42, y = 30)
l3 = tkinter.Label(root, text = generator, font = ('Calibri', 12), fg = 'green', width = '21')
l3.place(x = 142, y = 30)
l4 = tkinter.Label(root, text = "Klucz zostanie zapisany jako .txt w miejscu lokalizacji programu", font = ('Calibri', 8))
l4.place(x = 22, y = 60)
l5 = tkinter.Button(root, text = "generuj kolejny", command = generator, font = ('Calibri', 10), bg = 'grey', fg = 'white')
l5.place(x = 132, y = 83)
generator()
root.mainloop()