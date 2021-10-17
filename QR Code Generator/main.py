from qrcode import *
from adress import *
from table import *


scale = 70

header('Welcome to QR Code Generator', '=', scale)
print('Type an adress to generate a QR Code'.center(scale))
print(line('=', scale))

while True:
    adress = str(input('\033[33m>\033[m '))
    
    if verify(adress) == False:
        while True:
            header(f'\033[31m"{adress}" is not accessible right now. Are you sure that? (y/n)\033[m', '-', scale)

            choice = str(input('\033[33m>\033[m '))
            
            if choice.lower() == 'y' or 'n':
                break
    else:
        choice = 'y'
    
    if choice == 'y':
        header("Type file name and I'll create a file .png for you.", '-', scale)

        file_name = str(input('\033[33m>\033[m '))

        try:
            img = make(adress)
            img.save(f'{file_name}.png')
        except:
            header('\033[31mSorry I failed to create your QR Code.\033[m')
            break
        else:
            header("\033[32mYour QR Code is ready! Let's it...\033[m")
        
        try:
            img.show()
        except:
            header("\033[31mSorry I wanted to show you your QR Code but I can't open it.\033[m")