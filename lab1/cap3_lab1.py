# 1. Luați input de la utilizator primele 7 cifre ale CNP-ului. Găsiți o metoda sa calculați și sa
# afisati dacă utilizatorul are peste 18 ani, folosind if/else.
# Introduceti primele 7 cifre din CNP: 2981021
# Aveti peste 18 ani.

cnp = int(input("Enter your cnp: "))

first_letter = cnp[0]
ultimele_doua_cifre_alea_anului_nasterii = cnp[1:2]
luna_nasterii = cnp[3:4]
ziua_nasterii = cnp[5:6]
