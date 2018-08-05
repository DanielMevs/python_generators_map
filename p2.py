def running_max(seq):
    temp = seq[0]
    yield seq[0]
    for i in seq:
        if seq[i] > seq[i-1]:
            yield seq[i]
            temp = seq[i]
        else:
            yield temp
def running_mapped_max(seq, fun):
    temp = seq[0]
    yield seq[0]
    for i in seq:
        if fun(i) > fun(temp):
            yield i
            temp = i
        else:
            yield temp


for x in running_max([1,3,2,4,0,2]):
    print(x, end=", ")

teamdata = [(2010, 15), (2011, 12), (2012, 20), (2013, 23), (2014, 19), (2015, 21)]
for year_wins in running_mapped_max(teamdata, lambda yw: yw[1]):
    print(year_wins, end=", ")
