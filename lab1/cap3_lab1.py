# 1. Luați input de la utilizator primele 7 cifre ale CNP-ului. Găsiți o metoda sa calculați și sa
# afisati dacă utilizatorul are peste 18 ani, folosind if/else.
# Introduceti primele 7 cifre din CNP: 2981021
# Aveti peste 18 ani.


#L-am scris incomplet, lipseste ceva, posibil verificarea daca  a implinit deja 18 ani
# from datetime import datetime
#
# cnp = input("Enter your cnp: ")
#
# first_letter = int(cnp[0])
# ultimele_doua_cifre_alea_anului_nasterii = int(cnp[1:3])
# luna_nasterii = cnp[3:5]
# ziua_nasterii = cnp[5:7]
#
# secol = 0
# if first_letter in [1,2]:
#     secol = 1900
# elif first_letter in [5,6]:
#     secol = 2000
#
# anul_nasterii = secol + ultimele_doua_cifre_alea_anului_nasterii
#
# if(datetime.now().year - anul_nasterii >= 18):
#     print('Aveti peste 18 ani! ')
# else:
#     print('Aveti sub 18 ani')

# print(datetime.now().year)




#
# 2. Luați input de la utilizator un număr și parcurgeți intervalul de la 0 pana la numărul
# introdus de către utilizator, afisand toate numerele pare.

# number = input("Enter a number: ")
# for i in range(int(number)):
#     if i % 2 == 0:
#         print(i)






# 3. Un automat de cafea are următoarele opțiuni: Cappuccino, Espresso. Cappuccino
# costa 4 lei, iar Espresso costa 3,5 lei. Aparatul de cafea accepta doar bancnote de 5 si
# 10 lei.
# Utilizatorului îi este afișat meniul, după care i se cere o opțiune. Dacă utilizatorul a
# introdus o opțiune validă, i se cere o bancnota. Dacă utilizatorul a introdus o bancnotă
# validă, acesta va primi restul și i se va livra produsul.
# Creați un script care sa simuleze acest automat de cafea în mod similar cu exemplul
# următor:
# 1. Cappuccino ... 4 lei
# 2. Espresso ...3.5 lei
# Ce optiune alegeti? [1,2]: 1
# Introduceti o bacnota [5,10]: 5
# Veti primi restul de 1 lei.
# Produsul se livreaza...

# print('1.Cappuccino     ..4 lei')
# print('2.Espresso       ..3.5 lei')
# optiune = int(input('Ce optiune alegeti? [1,2] '))
#
# if optiune == 1:
#     bacnota = float(input('Introduceti o bacnota [5,10] '))
#     print(f'Veti primi restul de {bacnota-4} lei')
#     print('Produsul se livreaza')
# elif optiune == 2:
#     bacnota = float(input('Introduceti o bacnota [5,10] '))
#     print(f'Veti primi restul de {bacnota - 3.5} lei')
#     print('Produsul se livreaza')
# else:
#     print('Nu ati introdus o optiune valida')

##Rezolvare mai complexa
# # Meniul
# print('1. Cappuccino     ..4 lei')
# print('2. Espresso       ..3.5 lei')
#
# # Solicităm opțiunea utilizatorului
# optiune = int(input('Ce opțiune alegeți? [1,2] '))
#
# # Variabile pentru prețuri
# pret_cappuccino = 4
# pret_espresso = 3.5
#
# if optiune == 1:
#     # Dacă utilizatorul alege Cappuccino
#     bacnota = float(input('Introduceți o bancnotă [5, 10]: '))
#
#     if bacnota in [5, 10]:
#         if bacnota >= pret_cappuccino:
#             rest = bacnota - pret_cappuccino
#             print(f'Veți primi restul de {rest:.2f} lei.')
#             print('Produsul se livrează...')
#         else:
#             print('Nu ați introdus o sumă suficientă.')
#     else:
#         print('Bancnota introdusă nu este validă.')
#
# elif optiune == 2:
#     # Dacă utilizatorul alege Espresso
#     bacnota = float(input('Introduceți o bancnotă [5, 10]: '))
#
#     if bacnota in [5, 10]:
#         if bacnota >= pret_espresso:
#             rest = bacnota - pret_espresso
#             print(f'Veți primi restul de {rest:.2f} lei.')
#             print('Produsul se livrează...')
#         else:
#             print('Nu ați introdus o sumă suficientă.')
#     else:
#         print('Bancnota introdusă nu este validă.')
#
# else:
#     print('Nu ați introdus o opțiune validă.')








# 4.Parola unui PC este 7788. Creați un script care sa simuleze accesul la PC.
# Introduceti parola: 7677
# Parola gresita. Mai incercati.
# Introduceti parola: 3432
# Parola gresita. Mai incercati.
# Introduceti parola: 7788
# Acces permis.
# Process finished with exit code 0

# pc_password = 7677
# input_password = int(input("Enter your password: "))
# while input_password != pc_password:
#     print("Wrong password!, try again.")
#     input_password = int(input("Enter your password: "))
# print('Access permis')




#
# 5. Creați o lista obiecte = [“Masa”, 5, “Scaun”, 4.5, [5,6,7],8]. Parcurgeți lista de obiecte și
# afișați tipul fiecăruia. Challenge: Afișați tipul obiectelor în felul următor:
# Tipul obiectului Masa este str
# Tipul obiectului 5 este int

#
# list  = ["Masa", 5, "Scaun", 4.5, [5,6,7],8]
# # type(obiect).__name__: Returnează doar numele tipului obiectului, precum str, int, float, list
# for element in list:
#     print(f'Tipul obiectului {element} este {type(element).__name__}')
#




# 6. Luați ca input de la utilizator un cuvant si afisati numarul ocurentei primei litere din
# cuvant. Exemplu:
# Introduceti un cuvant (fara majuscule): rabdare
# r apare de 2 ori.

# word = input("Enter a word: ")
# first_letter = word[0]
# letter_apparition = 0
# for letter in word:
#     if first_letter == letter:
#         letter_apparition +=1
#
# print(f"{first_letter} apare de {letter_apparition} ori")




# 7. Pentru acest exercițiu aveți începutul codului care cere input de la utilizator cu un șir
# separat prin virgula și îl împarte într-o listă.
# lista = input("Introduceti lista de taskuri: ")
# lista_taskuri = lista.split(",")
# print(lista_taskuri)
# Parcurgeti lista generata din input-ul utilizatorului si eliminati dublurile din aceasta


###nu e bine, mai jos e rezolvarea corecta
# lista = input("Introduceti lista de taskuri: ")
# lista_taskuri = lista.split(",")
# # print(lista_taskuri)
# first_task = lista_taskuri[0]
# for task in lista_taskuri:
#     if task == first_task:
#         lista_taskuri.remove(task)
#     else:
#         first_task = task
#
# print(lista_taskuri)
# print(first_task)

lista = input("Introduceți lista de taskuri, separate prin virgulă: ")
lista_taskuri = lista.split(",")

# Folosim o listă pentru a stoca task-urile fără dubluri
taskuri_fara_dubluri = []

# Parcurgem lista și adăugăm taskurile care nu sunt deja în lista fără dubluri
for task in lista_taskuri:
    #task.strip(): Această metodă elimină eventualele spații suplimentare de la începutul și sfârșitul fiecărui task, deoarece în lista originală pot exista spații după virgulă.
    task = task.strip()  # Eliminăm spațiile extra de la început și final
    if task not in taskuri_fara_dubluri:
        taskuri_fara_dubluri.append(task)

print("Lista de taskuri fără dubluri:", taskuri_fara_dubluri)