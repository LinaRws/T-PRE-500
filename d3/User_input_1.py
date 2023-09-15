#Ask the user his/her name and then greet him/her with “Hello Username”, with the user’s name
#always printed with its first (and only the first) letter capitalized

print("Veuillez saisir votre prénom :")
name=str(input())
a=name.upper()[0]+name.lower()[1:]
print("Hello",a)

#ou print(name.title)