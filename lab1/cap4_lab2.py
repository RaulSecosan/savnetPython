# 1. Se cere un script care sa calculeze media de varsta a unor participanți la un sondaj de
# opinie. Cerinte:
# a. Se cere input de la utilizator numărul de participanți. Dacă utilizatorul introduce
# un răspuns invalid, se va trata eroarea cu ajutorul excepțiilor și i se va cere în
# mod repetat numărul de participanți pana cand acesta este unul valid.
# b. Pentru fiecare participant, se va cere varsta. Dacă varsta nu a fost introdusă
# corect, i se va cere din nou varsta pentru același participant.
# c. Media varstelor se va face printr-o funcția dedicată acestui lucru, prin pasarea
# unei liste care contine toate varstele ca parametru.
# Exemplu output:
# Cati participanti avem la sondaj? 4
# Introduceti varsta participantului 1: 22
# Introduceti varsta participantului 2: t
# Nu ati introdus un format valid la participantul 2.
# Introduceti varsta participantului 2: 34
# Introduceti varsta participantului 3: 45
# Introduceti varsta participantului 4: 22t
# Nu ati introdus un format valid la participantul 4.
# Introduceti varsta participantului 4: 45
# Media de varsta a participantilor la sondajul de opinie este: 36.5

# age_list = []
# while True:
#     try:
#         participants_number = int(input("Enter number of participants: "))
#         if participants_number > 0:
#             break
#         else:
#             print("Please enter a positive integer")
#     except ValueError:
#         print("Please enter a correct number")
#
# for i in range(1, participants_number + 1):
#     try:
#         age = int(input(f"Enter age for {i}: "))
#
#         if age >= 0:
#             age_list.append(age)
#         else:
#             print("Please enter a valid age")
#
#
#     except ValueError:
#         print(f"Nu ați introdus un format valid la participantul {i}.")
#
# media_varstelor = sum(age_list) / len(age_list)
# print(f'Media varstelor este {media_varstelor: }')





# 2. Se da urmatorul schelet de cod:
# def suma(lista: list):
# pass
# def medie(lista: list):
# passdef putere(lista: list):
# pass
# meniu = {
# "1": medie,
# "2": suma,
# "3": putere
# }
# Se cere:
# a. Input de la utilizator cu numere, care se vor aduna într-o listă cu elemente de tip
# float. Numerele trebuie sa fie valide. Cand utilizatorul nu mai are numere de
# introdus, va scrie x.
# Introduceti numere. Cand sunteti gata, introduceti x.
# Numar: 3
# Numar: 5
# Numar: 18.8
# Numar: 2
# Numar: 4
# Numar: x
# b. După introducerea numerelor, se va afișa un meniu cu 4 opțiuni: medie, suma,
# puterea numerelor din lista, iesire. În funcție de ce introduce utilizatorul, se va
# calcula rezultatul cu ajutorul funcțiilor din scheletul de mai sus și se va afișa.
# Meniu:
# 1. Media numerelor
# 2. Suma numerelor
# 3. Puterea numerelor din lista de numere
# 4. Iesire
# Introduceti optiunea dvs: 1
# Rezultatul: 6.56


#
# def suma(lista: list):
#     return sum(lista)
# def medie(lista: list):
#     if len(lista) == 0:
#         return 0
#     return sum(lista) / len(lista)
#
# def putere(lista: list):
#     # nu am inteles exact ce trebuie sa fac
#     if len(lista) == 0:
#         return 0
#     power = 1
#     for number in lista:
#         power += number
#     return power
# meniu = {
#     "1": medie,
#     "2": suma,
#     "3": putere
#   }
#
#
# numbers_list = []
# print('Introduceti numere. Cand sunteti gata, introduceti x.')
# while True:
#
#     number_or_done = input('Numar: ')
#
#     if (number_or_done.lower() == 'x'):
#         print("It's over")
#         break
#
#     try:
#         numbers_list.append(float(number_or_done))
#
#     except ValueError:
#         print("It's not a number")
#
# while True:
#     print("\nMeniu:")
#     print("1. Media numerelor")
#     print("2. Suma numerelor")
#     print("3. Puterea numerelor din lista de numere")
#     print("4. Ieșire")
#
#     optiune = input("Introduceți opțiunea dvs: ")
#
#     if optiune == "4":
#         print("La revedere!")
#         break
#     elif optiune in meniu:
#         rezultat = meniu[optiune](numbers_list)
#         print(f"Rezultatul: {rezultat:}")
#     else:
#         print("Opțiune invalidă. Încercați din nou.")
# print(numbers_list)




# 3. Se da urmatorul text:
# “In primavara anului 1894, toata Londra a fost interesata, iar lumea la moda a fost consternata de
# uciderea onorabilului Ronald Adair in circumstante cele mai neobisnuite si inexplicabile. Publicul
# a aflat deja acele detalii ale crimei care au iesit la iveala in ancheta politiei; dar multe au fost
# suprimate cu acea ocazie, deoarece cazul acuzarii era atat de coplesitor de puternic, incat nu era
# necesar sa se prezinte toate faptele. Abia acum, la sfarsitul a aproape zece ani, imi este permis sa
# aprovizionez acele verigi lipsa care alcatuiesc intregul lant remarcabil. Crima era interesanta in
# sine, dar acel interes nu era nimic pentru mine in comparatie cu continuarea de neconceput, care
# mi-a oferit cel mai mare soc si surpriza din orice eveniment din vitța mea aventuroasa. Chiar si
# acum, dupa acest interval lung, mă trezesc emotionat cand ma gandesc la asta si simt din nou acel
# potop brusc de bucurie, uimire si neincredere care mi-a cufundat cu totul mintea.”
# Se cere:
# a. Numărarea literei introduse de către utilizator în textul de mai sus, indiferent daca
# aceasta este o majuscula sau nu.
# b. Crearea unei liste cu toate cuvintele din textul de mai sus cu ajutorul funcțiilor
# split().
# Documentatie: https://docs.python.org/3/library/stdtypes.html#str.split
# c. Selectarea cuvintelor care incep cu litera s din lista creata anterior si afisarea
# acestora.

# Textul dat
text = """
In primavara anului 1894, toata Londra a fost interesata, iar lumea la moda a fost consternata de
uciderea onorabilului Ronald Adair in circumstante cele mai neobisnuite si inexplicabile. Publicul
a aflat deja acele detalii ale crimei care au iesit la iveala in ancheta politiei; dar multe au fost
suprimate cu acea ocazie, deoarece cazul acuzarii era atat de coplesitor de puternic, incat nu era
necesar sa se prezinte toate faptele. Abia acum, la sfarsitul a aproape zece ani, imi este permis sa
aprovizionez acele verigi lipsa care alcatuiesc intregul lant remarcabil. Crima era interesanta insine, dar acel interes nu era nimic pentru mine in comparatie cu continuarea de neconceput, care
mi-a oferit cel mai mare soc si surpriza din orice eveniment din vitța mea aventuroasa. Chiar si
acum, dupa acest interval lung, mă trezesc emotionat cand ma gandesc la asta si simt din nou acel
potop brusc de bucurie, uimire si neincredere care mi-a cufundat cu totul mintea.
"""

# a. Numărarea unei litere introduse de utilizator (majuscule și minuscule tratate la fel)
litera = input("Introduceți o literă pentru a număra aparițiile ei: ").lower()
count_litera = text.lower().count(litera)
print(f"Litera '{litera}' apare de {count_litera} ori în text.")

# b. Crearea unei liste cu toate cuvintele din text
lista_cuvinte = text.split()
print("\nLista cuvintelor din text este creată.")
print(lista_cuvinte)

# c. Selectarea cuvintelor care încep cu litera 's'
print("\nLista cuvintelor din text care incep cu 's'.")
words_starts_with_s = []
for cuvant in lista_cuvinte:
    if cuvant[0].lower() == 's':
        words_starts_with_s.append(cuvant)
        # print(cuvant)

print(words_starts_with_s)