print(" ------Introduce Youself------")

name = input(" Enter your name : ")
age = (input("Enter your age : "))

print(" Hello my name is "+ name +  " and my age is " +age)




print("-----Your Favourit Hobby-----")


fav_hobby = input("' Enter your favourit hobby : ")

print(" Upper case : " , fav_hobby.upper())


print(" Lower case : " , fav_hobby.lower())


print( " Length of Hobby = ", len(fav_hobby))



print("-----simple functins-----")

def greet_user(name):
    
    print(" Hey " + name + " python is waiting for you")
user_input =input(" Enter name : ")    
greet_user(user_input)
sen = str(input("Enter any santance: "))
print(sen.title())
print(sen.replace(" ","-")



adjective = input("Enter adjective = ")
noun = input("Enter the noun  = ")
verb = input("Enter the verb = ")

print("The adjective is = " +adjective + " The verb is = " + verb + " The noun is = "+ noun)


def full_name(first,last):
    return first+" "+ last
first = input("Enter your first name: ")
last = input("Enter your last name: ")
print("Your full name is:", full_name(first, last))


    
    
    

