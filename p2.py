
def running_max(seq):
    temp = seq[0]
    yield seq[0]
    for i in seq:
        if seq[i] > seq[i-1]:
            yield seq[i]
            temp = seq[i]
        else:
            yield temp
        
     
for x in running_max([1,3,2,4,0,2]):
    print(x, end=", ")
