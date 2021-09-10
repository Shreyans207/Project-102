import csv
from collections import Counter

start_up = print('This program will easily  give out the details about any element present in currect periodic table')
print('')

with open('chem_elements.csv' , newline = '') as f : 
    reader = csv.reader(f)
    list_data = list(reader)

new_data = []
result = True
while(result) : 
    element_name = input('Enter the element name : ')
    for i in range(len(list_data)) : 
        Element_No = list_data[i][0]
        Element_Symbol = list_data[i][2]
        Element = list_data[i][1]
        if (Element == element_name or Element_No == element_name or Element_Symbol == element_name) : 
            position = list_data[i]

    print('')
    print(f'    Atomic Number : {position[0]}')
    print(f'    Element : {position[1]}')
    print(f'    Symbol : {position[2]}')
    print(f'    Atomic Mass : {position[3]}')
    print(f'    Discoverer : {position[23]}')
    print(f'    Year : {position[24]}')
    print(f'    Type : {position[15]}')
    print('')
    print(f'    No. Of Neutrons : {position[4]}')
    print(f'    No. Of Protons : {position[5]}')
    print(f'    No. Of Electrons : {position[6]}')
    print(f'    No. Of Shells : {position[26]}')
    print(f'    No. of Valence Electrons: {position[27]}')
    print('')
    print(f'    Period : {position[7]}')
    print(f'    Group : {position[8]}')
    print(f'    Phase : {position[9]}')
    print(f'    Density : {position[19]}')
    print(f'    Melting Point : {position[20]}')
    print(f'    Boiling Point : {position[21]}')
    print('')
    print(f'    Atomic Radius : {position[16]}')
    print(f'    Electronegativity : {position[17]}')
    print(f'    No. Of Isotopes : {position[22]}')
    print('')
    mood = input('Wanna Continue (y/n) : ')
    print('')

    if(mood == 'n' or mood == 'N') : 
        result = False
    else : 
        result = True
        position = None

print('Thanks for using this application :)')
