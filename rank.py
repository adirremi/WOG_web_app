def top3rank(dct):
    nameLIST = sorted(dct, key=dct.get)[-3:]
    return top3points(nameLIST[-1::-1], dct)


def top3points(list, dct):
    newList = []
    for name in list:
        newList.append([name, dct.get(name)])
    return newList
