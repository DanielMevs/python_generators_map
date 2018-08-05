def mapflatlst(lst, fun):
    if len(lst) == 0:
        return []
    else:
        return [fun(lst[0])] + mapflatlst(lst[1:], fun)

def times2(x):
    return x*2

ls = [1,2,3,4]
print(mapflatlst(ls, times2))



