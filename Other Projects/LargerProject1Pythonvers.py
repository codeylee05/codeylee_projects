
sentences = {
    "Me llamo Lefa y yo tengo un gato bonito que se llama Ily":"My name is Lefa and I have a beautiful cat called Ily",
    "Yo vivo en una casa muy grande con mi mama, mi tia, y su perro":"I live in a very big house with my mom, my aunt, and her dog",
    "Hoy es una dia muy interesante porque mi companero de intercambio que viene de Francia nos visita":"Today will be a very interesting day because my exchange partner who comes from France is visiting us"
}
correct_transl = 0
incorrect_transl = 0

def userTranslation():
    
    user_transl = input("Translation: ")

    return user_transl


def checkTranslation(user_value, actual_value):

    if user_value == actual_value:
        print("Correct!")
        global correct_transl
        correct_transl += 1
    else:
        print("Incorrect")
        global incorrect_transl
        incorrect_transl += 1


def outputSentence():

    i = 0
    for key, value in sentences.items():
        i += 1
        print("")
        print(f"The Spanish sentence {i} is: ")
        print(f"{key}")

        user_transl_return = userTranslation()
        checkTranslation(user_transl_return, value)

outputSentence()

print("")
print(f"Completed! You have gotten {correct_transl}/{incorrect_transl}questions correct")
print("")

def outputAll():

    for key, value in sentences.items():
        print(f"{key} | {value}")

outputAll()