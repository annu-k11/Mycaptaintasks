print("List of positive numbers\n\t: "+str([x for x in [int(x) for x in input("input integers saprated by ','(coma)\n\t: ").split(",")] if x > 0]).strip("[]"))
