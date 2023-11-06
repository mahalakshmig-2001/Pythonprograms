# Giraffe Language
#vowels--g
#----------eg:

#dog-dgg
#cat--cgt

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation  + "g"
        else:
            translation = translation + letter
    return translation

#print(translate("Cat"))
print(translate(input("Enter phrase:")))
