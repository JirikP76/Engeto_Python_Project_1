# Projekt 1 - Textový analyzátor
#           - první projekt do Engeto Online Python Akademie

# author: Jiří Požár
# email: pozar@volny.cz
#

texts = ['''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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
    garpike and stingray are also present.''']

# přihlášení do programu
users = {"bob":"123",
         "ann":"pass123",
         "mike":"password123",
          "liz":"pass123"
}
user = input("username:")
password = input ("password:")
if users.get(user) == password:
    print("-" * 40)
    print("Welcome to the app,", user)
else:
    print("Unregistered user, terminating the program...")
    exit()

# analyzátor textů - volba textu
print(f"We have {len(texts)} texts to be analyzed.")
print("-" * 40)  
choice = input(f"Enter a number btw 1 and {len(texts)} to select: ")
print("-" * 40)
choice = int(choice) - 1
if 0 <= choice < len(texts):
    choice_text = texts[choice]
else:
    print("Invalid choice, program terminated.")
    exit()

# ANALÝZA TEXTU - 1.část
# součet slov   
word_count = len(choice_text.split())
# součet slov začínajících velkým písmenem 
word_titlecase_count = 0
for word in choice_text.split():
    if word[0].isupper() and any(char.isdigit() == False for char in word):
        word_titlecase_count += 1
# součet slov psaných velkými písmeny        
word_uppercase_count = 0
for word in choice_text.split():
    if word.isupper() and any(char.isdigit() == False for char in word):
        word_uppercase_count += 1
# součet slov psaných malými písmeny
word_lowercase_count = 0
for word in choice_text.split():
    if word.islower() and any(char.isdigit() == False for char in word):
        word_lowercase_count += 1
# součet číselných řetězců
numeric_string_count = 0        
for word in choice_text.split():
    if word.isdigit() and any(char.isdigit() == True for char in word):
        numeric_string_count += 1 
# součet hodnot číselných řetězců        
numbers = [int(word) for word in choice_text.split() if word.isdigit()]
numbers_sum = sum(numbers)

# VÝPIS ANALÝZY - 1.část
print(f"There are {word_count} words in the selected text.")
print(f"There are {word_titlecase_count} titlecase words.")
print(f"There are {word_uppercase_count} uppercase words.")
print(f"There are {word_lowercase_count} lowercase words.")
print(f"There are {numeric_string_count} numeric string.")
print(f"The sum of all the numbers is {numbers_sum}")
print("-" * 40)

# ANALÝZA TEXTU s výpisem - 2.část
# délka jednotlivých slov
len_words = [len(word.strip(",.")) for word in choice_text.split()]
# výpis délky slov
print("LEN |    OCCURRENCES     |NR.")
print("-" * 40)
for length in sorted(set(len_words)):
    count = len_words.count(length)
    stars = '*' * count
    print(f"{length:>3} | {stars:<18} | {count}")

