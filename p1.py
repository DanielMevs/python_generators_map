def mapflatlst(lst, fun):
    if len(lst) == 0:
        return []
    else:
        return [fun(lst[0])] + mapflatlst(lst[1:], fun)

def times2(x):
    return x*2

def maplst(lst, fun):
    if len(lst) == 0:
        return []
    elif type(lst[0]) == list:
        return maplst(lst[0] + lst[1:], fun)
    else:
        return [fun(lst[0])] + maplst(lst[1:], fun)

ls = [1,2,3,4,5]
ls2 = [[[1]], [2, [3, 4], 5], 6]
print(mapflatlst(ls, times2))
print(maplst(ls2, times2))

