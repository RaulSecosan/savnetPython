# 1. Se cere afișarea următoarelor șiruri pe ecran:
# a. Astăzi mă duc la “facultate”.
# b. /*\/*\*/*\/*\
# Python
# \./\./\./\./
# c. P y t h o n


# print("Astazi ma duc la \" facultate \" ")
# print("/*\\/*\\*/*\\/*\\ \n  Python \n \\./\\./\\./\\./ ")
# print("P\ty\tt\th\to\tn")

# 2. Se cere input de la utilizator:
# a. Numele utilizatorului
# b. Varsta
# Creati un script care sa aibe output similar cu exemplul urmator:
# Cum te numesti? Ana
# Ce varsta ai? 22
# Ceau Ana! Deci te-ai nascut in 1999.
#
# name = input("Name: ")
# age = int(input("Age: "))
#
# print(f"Cum te numesti? {name}\n Ce varsta ai? {age}\n Ceau {name}! Deci te-ai nascut in {2024-age}.")



# 3. Cereți input de la utilizator cu un șir și afișați lungimea șirului in 4 moduri:
# - Cu metoda format()
# - Prin metoda f” ”
# - Concatenare (+)
# - Cu virgula
# Introduceti un sir: Ana are mere.
# Lungimea sirului este: 13

# sir = input('Introdu un sir: ')
# lungime_sir = len(sir)
# # print(lungime_sir)
# # sa fiu atent sa pui {} la format
# print('Cu format {}'.format(lungime_sir))
# print(f'Lungimea sirului  {lungime_sir}')
# print('Lungimea sirului ' + str(lungime_sir))
# print('Lungimea sirului ', lungime_sir)


# 4. Afișați următoarele forme geometrice folosind metoda center().
#asa am scris eu dar mai jos e de prof mai bine
# print("/-\\".center(20))
# #primul center e pentru a-mi adauga \ iar al doilea pentru al pozitiona bine
# print("//_".center(6,'\\')[1:].center(20))
# print("".center(7,'-').center(20))
# print("\\_//".center(6,'\\')[0:-1].center(20))
# print('\\-/'.center(20))
#
# print("----".center(20))
# print("/    \\".center(19))
# print("/______\\".center(20))

#de prof
# print("/-\\".center(20))
# print("//_\\\\".center(20))
# print("-------".center(20))
# print("\\\\_//".center(20))
# print('\\-/'.center(20))

# print("*".center(20))
# print("***".center(19))
# print("*****".center(20))
# print("*******".center(20))



# 5. Cereți input de la utilizator cu un cuvânt. Afișați dacă acest cuvant este palindrom.
# Introduceti un cuvant: ana
# Palindrom: True
# Introduceti un cuvant: Ananas
# Palindrom: False


# cuvant = input('Introdu un cuvant: ')
# # Daca nu punem lower atunci Ana este diferit de ana si va da false ceea ce nu e bine
# palindrom = cuvant.lower() == cuvant[::-1].lower()
# print(palindrom)



# 6. Afișați următoarele șiruri: “Hello Python”, “Ana are mere”, “Pizza Party” în următoarele
# formate:
# - Fiecare cuvant separat cu _
# - Punct la final de sir
# - Primul cuvânt din șir multiplicat de 4 ori

str1 = "Hello Python"
str2 = "Ana are mere"
str3 = "Pizza Party"

print(str1.replace(" ", "_"))
print(str2.replace(" ", "_"))
print(str3.replace(" ", "_"))

print(str1 + '.')
print(str2 + '.')
print(str3 + '.')

print((str1.split()[0] + ' ')  * 4)
print((str2.split()[0] + ' ') * 4)
print((str3.split()[0] + ' ')  * 4)





# 7. Creati 3 variabile: a = 5., b = 5, c = “ana”
# - Afisati locatia in memorie a fiecarei variabile in hexadecimal
# Locatia lui a este: 0x14951d37b70
# - Afișați tipul variabilei
# Tipul variabilei a este: <class 'float'>

a = 5
b = 5
c = "ana"
print(f"Locatia lui c este: {hex(id(c))}")
print(f"Locatia lui a este: {hex(id(a))}")
print(f"Locatia lui b este: {hex(id(b))}")

print(f"Tipul variabilei  a este {type(a)}")
print(f"Tipul variabilei  b este {type(b)}")
print(f"Tipul variabilei  c este {type(c)}")
