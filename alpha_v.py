letter = lambda str :dict([(i,str.count(i)) for i in str])
[print( k, " = ", v ) for k,v in dict(sorted(letter(input("Enter a word :").lower()).items(), key = lambda kv : kv[1], reverse = True)).items()]




#[print( k, " = ", v ) for k,v in dict(sorted(dict([(i,str.count(i)) for i in input("Enter :").lower()]).items(), key = lambda kv : kv[1], reverse = True)).items()]
