
# 1. Pentru primul exercițiu se cere calcularea ariei unui triunghi folosind forma de mai jos,
# cerand parametrii de la utilizator.
# A=1/2bh , unde b = bază și h = înălțimea.
# a. Cereți input de la utilizator cu baza triunghiului și înălțimea acestuia. Asigurati-va
# ca utilizatorul știe ce trebuie sa introduca, și stocati valorile cerute într-o variabila.
# b. Creați o variabila care sa reprezinte rezultatul calculului.
# c. Afișați tipul de data a variabilei rezultate
# d. Afișați rezultatul funcției pe ecran.

    # b = float(input("Enter base: "))
    # h = float(input("Enter height: "))
    #
    # a = 1/2 *b*h
    # print(type(a))
    # print(f'Aria este: {a}')


# 2. Parola unui calculator este 7710. Se cere input de la utilizator cu un număr. Afișați
# comparatia intre aceste doua numere. Daca este True, înseamnă ca utilizatorul a ghicit
# parola.

#     pc_password = 7710
#     input_password = int(input("Enter password: "))
#     if pc_password == input_password:
#         print("Correct password")
#     else:
#         print("Incorrect password")




# 3. Se va cere input de la utilizator cu 2 numere. Se calculeaza:
# a. Media numerelor
# b. Impartirea numerelor in ordinea introdusa de catre utilizator (rezultatul trebuie sa
# fie număr întreg)
# c. Primul număr la puterea celui de-al doilea număr.
# ** Cand afisati rezultatele pe ecran, afișați-le dintr-o singura funcție print și folosiți
# escape character pentru a delimita output-ul. Exemplu output:
# Media numerelor este: 8.5
# Impartirea numerelor este: 2
# A la puterea b: 248832

    # number1 = int(input("Enter first number: "))
    # number2 = int(input("Enter second number: "))
    #
    # medie = (number1 + number2)/2
    # impartire = number1//number2
    # poww = number2**number1
    #
    # print(f"Media numerelor: {medie}\n Impartirea numerelor: {impartire}\n Power: {poww}")



# 4. Se cere input de la utilizator cu venit net pe luna. Din acesta, calculati regula 50/30/20:
# - 50% din venit acordat necesităților (cumparaturi, intretinere, chirie, etc)
# - 30% din venit acordat scopurilor recreative
# - 20% din venit acordat datoriilor și economiilor
# Venit: 2875
# Recomandarile noastre:
# Cheltuieli uzuale: 1437.5
# Recreere: 862.5
# Economii si datorii: 575.0

venit_net = float(input("Venit net: "))

fifty = 50/100 * venit_net
thirty = 30/100 * venit_net
twenty = 20/100 * venit_net

print(f"Venit: {venit_net}\n Recomandarile noastre:\n Cheltuieli uzuale: {fifty}\n Recreere: {thirty}\n Economii si datorii: {twenty}")