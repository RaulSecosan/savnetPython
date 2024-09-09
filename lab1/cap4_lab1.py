# 1. Cereți input de la utilizator cu username și parola dorită. Se cere o funcție care sa
# verifice dacă are lungimea de minim 7 caractere, conține o cifra și una din următoarele
# caractere: !,@,%.
# Exemplu:
# Introduceti o parola: hcjdfhks
# Parola trebuie sa contina una din urmatoarele caractere: %, !, @.
# Parola trebuie sa contina o cifra.
# Introduceti o parola: Iosido
# Parola trebuie sa contina una din urmatoarele caractere: %, !, @.
# Parola trebuie sa contina o cifra.
# Parola trebuie sa aiba lungimea mai mare de 7 caractere.
# Introduceti o parola: Iosdis5
# Parola trebuie sa contina una din urmatoarele caractere: %, !, @.
# Introduceti o parola: Isidjsdaj%3
# Parola este in regula.
# Process finished with exit code 0
# Challenge: În scriptul anterior se mai adaugă o condiție la parola: Parola trebuie să
# înceapă cu litera mare. Verificati daca parola introdusă de către utilizator începe cu o
# litera mare.

#
# username = input("Enter your username: ")
# password = input("Enter your password: ")
#
# specials_characters = ['%','!','@']
# if(len(password) < 7):
#     print("Parola trebuie sa aiba lungimea mai mare de 7 caractere.")
#
# if not password[0].isupper():
#     print("Parola trebuie să înceapă cu o literă mare.")
#
# if not any(cifra.isdigit() for cifra in password):
#         print("Parola trebuie să conțină o cifră.")
#
# if not any(special_character in '!@%' for special_character in password):
#         print("Parola trebuie să conțină una din următoarele caractere: %, !, @.")
#
# if(len(password) >= 7 and password[0].isupper() and any(cifra.isdigit() for cifra in password) and  any(special_character in '!@%' for special_character in password)):
#     print("Parola este în regulă.")



#
# 2. Creați o aplicație care sa ceara input de la utilizator cu un număr. Creați o funcție care
# sa ia ca parametru numărul introdus de către utilizator si sa calculeze puterea acestuia.
# Cereți input de la utilizator în interiorul unei bucle infinite. Dacă utilizatorul dorește sa
# iasa, trebuie sa scrie q.

# def power_run(number):
#     return number ** 2
#
# def infiniteLoop():
#     while True:
#        out_or_number = input('For out press Q or press a number: ')
#        if out_or_number.lower() == 'q':
#            print('Bye')
#            break
#        try:
#            number = float(out_or_number)
#            putere = power_run(number)
#            print(f"Puterea numărului {number} este: {putere}")
#        except ValueError:
#            print('Please enter a number valid')
#
# infiniteLoop()



# 3. Într-un birou se afla 3 PC-uri. Creați un script care sa ceara admin si user pentru fiecare
# din cele 3 PC-uri si sa mapeze user-ul fiecărui PC cu parola acestuia într-un dictionar.
# Afișați credentialele în formatul următor:
# Introduceti utilizatorul PC-ului 1:
# admin1
# Introduceti parola PC-ului 1:
# passme1
# Introduceti utilizatorul PC-ului 2:
# admin2
# Introduceti parola PC-ului 2:
# passme2
# Introduceti utilizatorul PC-ului 3:
# admin3
# Introduceti parola PC-ului 3:
# passme3
# admin1 -> passme1
# admin2 -> passme2
# admin3 -> passme3
# Process finished with exit code 0

# # Inițializăm un dicționar pentru a stoca utilizatorii și parolele
# credențiale = {}
#
# # Parcurgem fiecare PC și cerem utilizatorul și parola
# for i in range(1, 4):
#     utilizator = input(f"Introduceți utilizatorul PC-ului {i}: ")
#     parola = input(f"Introduceți parola PC-ului {i}: ")
#
#     # Mapăm utilizatorul cu parola în dicționar
#     credențiale[utilizator] = parola
#
# # Afișăm credențialele în formatul dorit
# print("\nCredențialele sunt:")
# for utilizator, parola in credențiale.items():
#     print(f"{utilizator} -> {parola}")





#
# 4. Se dau următoarele dictionare.
# angajat1 = {
# 'nume': 'Ana-Maria Popescu',
# 'departament': 'IT',
# 'ID': 3409,
# 'Salar': 4560,
# }
# angajat2 = {
# 'nume': 'Marian Muntean',
# 'departament': 'IT',
# 'ID': 2235,
# 'Salar': 4556,
# }
# angajat3 = {
# 'nume': 'Maria Manea',
# 'departament': 'HR',
# 'ID': 1908,
# 'Salar': 6755,
# }
# angajat4 = {
# 'nume': 'Oana Popa','departament': 'HR',
# 'ID': 1977,
# 'Salar': 5400,
# }
# angajat5 = {
# 'nume': 'David Codru',
# 'departament': 'Management',
# 'ID': 1988,
# 'Salar': 12900,
# }
# lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]
# Se cere:
# a. Afisati numele, departamentul si ID-ul angajatilor cu salar mai mare decat 5000.
# Ion Doe -> HR1000
# b. Creați o lista cu numele angajatilor, mai puțin a managerului, si afisati-o.
# c. Faceti media salariala pe departamentul HR si afisati-o.


angajat1 = {
'nume': 'Ana-Maria Popescu',
'departament': 'IT',
'ID': 3409,
'Salar': 4560,
}
angajat2 = {
'nume': 'Marian Muntean',
'departament': 'IT',
'ID': 2235,
'Salar': 4556,
}
angajat3 = {
'nume': 'Maria Manea',
'departament': 'HR',
'ID': 1908,
'Salar': 6755,
}
angajat4 = {
'nume': 'Oana Popa','departament': 'HR',
'ID': 1977,
'Salar': 5400,
}
angajat5 = {
'nume': 'David Codru',
'departament': 'Management',
'ID': 1988,
'Salar': 12900,
}
lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]
lista = []
salarii_hr = []

for angajat in lista_dict:
    if angajat['Salar'] >= 5000:
        print(angajat['nume'] + angajat['departament'], angajat['Salar'])

    if angajat['departament'] != 'Management':
        lista.append(angajat['nume'])

    if angajat['departament'] == 'HR':
        salarii_hr.append(angajat['Salar'])

print("\nLista angajaților (fără manager):", lista)
if salarii_hr:
    media_salariala_hr = sum(salarii_hr) / len(salarii_hr)
    print(f"\nMedia salarială în departamentul HR este: {media_salariala_hr:}")
