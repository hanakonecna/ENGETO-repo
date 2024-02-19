'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Hana Konecna
email: h.konecna16@seznam.cz
discord: hana.konecna

'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
"bob": "123", 
"ann": "pass123",
"mike": "password123",
"liz": "pass123"
}

separator = "-" * 30

username = input("username: ")
password = input("password: ")

if users.get(username) == password:
    print(separator, f"Welcome to the app, {username}", sep="\n")
    print(f"We have {len(TEXTS)} texts to be analyzed.", separator, sep="\n")
else:
    print("unregistered user, terminating the program..")
    quit()

number = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

if number.isdigit():
    number_input = int(number)  

    if 1 <= number_input <= len(TEXTS):
        
        words = [word.strip(",.:;'") for word in TEXTS[number_input - 1].split()]
        
        words_count = len(words)
        print(f"There are {words_count} words in the selected text.")

        titlecase_count = sum(1 for word in words if word.istitle())
        print(f"There are {titlecase_count} titlecase words.")

        uppercase_count = sum(1 for word in words if word.isupper())
        print(f"There are {uppercase_count} uppercase words.")

        lowercase_count = sum(1 for word in words if word.islower())
        print(f"There are {lowercase_count} lowercase words.")

        numeric_string = sum(1 for word in words if word.isnumeric())
        print(f"There are {numeric_string} numeric strings.")

        numbers = [int(word) for word in words if word.isdigit()]
        sum_numbers = sum(numbers)
        print(f"The sum of all the numbers {sum_numbers}")
        print(separator)

        word_length = []
        for word in words:
            word_length.append(len(word))

        occurence = {}
        for length in word_length:
            if length not in occurence:
                occurence[length] = 1
            else:
                occurence[length] += 1

        print(" LEN | OCCURENCES | NR.")
        print(separator)
       
        for length, frequency in sorted(occurence.items()):
            print(f"{length:2} | {'*' * frequency:<{max(occurence.values())}} | {frequency:2}")

    else:
        print("Wrong input, terminating the program...")

else:
    print("Wrong input, terminating the program...")