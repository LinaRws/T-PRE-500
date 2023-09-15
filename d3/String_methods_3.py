#Can you predict the result of the following snippet of code?
p = "abcdefghij"
print(p[:: -2][:5][:: -1][3:])

#A chaque crochet, une sous-chaîne est créée. Le crochet suivant est appliqué au croquet précédent.
#Le crochet 2 s'applique sur la chaîne créée par le crochet 1

#Crochet 1 : jhfdb
#Crochet 2 : jhfdb
#Crochet 3 : bdfhj
#Crochet 4 : hj