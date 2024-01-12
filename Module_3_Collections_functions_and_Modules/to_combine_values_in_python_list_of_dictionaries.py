# import module Counter from the collections
from collections import Counter
mylist = [{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
data = Counter()
#print(data)
# use for loop in mylist
for i in mylist:
    data[i['item']]+=i['amount']
print(data)    
