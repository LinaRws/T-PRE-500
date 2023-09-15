#Write a snippet of code that counts the number of occurrences of the strings “Cat”, “Garden” and
#“Mice” in any string.
#The substring can be read left to right or right to left
#Matches must be case insensitive.
#The string “thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN” should return 4.

ch="thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
l=ch.lower()+ch.lower()[::-1]
a=l.count("cat")
b=l.count("garden")
c=l.count("mice")
print(a+b+c)
