def analyis_text(txt):
    print("Length of txt is = ",len(txt))
    print("Text in uppercasse = ", txt.upper())
    print("First letter of text is = ", txt[0])
    print("Last letter of text is = ", txt[-1])
sentence = input("Enter the sentence = ")  
analyis_text(sentence)
    
def make_story(name, place, object, feeling):
    story = "One day, " + name + " went to " + place + ". " \
            + name + " found a " + object + " there and felt very " + feeling + "."
    print("\nHere’s your story:")
    print(story)

name = input("Enter a name: ")
place = input("Enter a place: ")
object = input("Enter an object: ")
feeling = input("Enter a feeling: ")        
    
    
    
def format_word(word):
    print("Title case = ", word.title())
    print("Reversed = ", word[::-1])

    vowel_replaced = word.replace('a', '*')
    vowel_replaced = vowel_replaced.replace('e', '*')
    vowel_replaced = vowel_replaced.replace('i', '*')
    vowel_replaced = vowel_replaced.replace('o', '*')
    vowel_replaced = vowel_replaced.replace('u', '*')

    print("Vowel Replaced:", vowel_replaced)


sentence = input("Enter sentence: ")
format_word(sentence)

    

 