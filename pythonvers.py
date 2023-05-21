
sentences = {
    "Me llamo Lefa y yo tengo un gato bonito que se llama Ily":"My name is Lefa and I have a beautiful cat called Ily",
    "Yo vivo en una casa muy grande con mi mama, mi tia, y su perro":"I live in a very big house with my mom, my aunt, and her dog",
    "Hoy es una dia muy interesante porque mi companero de intercambio que viene de Francia nos visita":"Today will be a very interesting day because my exchange partner who comes from France is visiting us"
}

correct_transl = 0
incorrec_transl = 0

def userTranslation():
        
    user_translate = input("Translation: ")
        
    return user_translate


def checkTranslation(user_translation, actual_translation):

    if user_translation == actual_translation:
        print("Correct!")
        global correct_transl
        correct_transl += 1
    else:
        print("Incorrect!")
        global incorrec_transl
        incorrec_transl += 1

#main function#
def outputSentence():

    i = 0
    for key, value in sentences.items():
        i += 1
        print(f"The Spanish sentence {i} is:")
        print(f"{key}")

        user_translated = userTranslation()
        checkTranslation(user_translated, value)

outputSentence()


print(f"Well done! You have gotten {correct_transl}/{len(sentences)} sentences correct")

def outputAll():
    
    for key, value in sentences.items():
        print(key, "|", value)

print(f"The sentences are: ")
outputAll()

