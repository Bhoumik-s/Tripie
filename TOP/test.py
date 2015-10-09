from collections import OrderedDict

alist = []
for x in range(100):
    adict = {}
    adict["1"]=x
    adict["2"]=x+1
    alist.append(adict.copy())
print(alist)