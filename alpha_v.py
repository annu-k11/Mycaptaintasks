def  most_frequent(str):
    letter = lambda str :dict([(i,str.count(i)) for i in str])
    [print( k, " = ", v ) for k,v in dict(sorted(letter(str.lower()).items(), key = lambda kv : kv[1], reverse = True)).items()]

word = input("Enter a word :")
most_frequent(word)
