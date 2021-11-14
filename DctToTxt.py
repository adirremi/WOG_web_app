import json


def dct_w_txt(dct):
    f = open('Scores.txt', 'w+')
    f.write(json.dumps(dct))
    f.close()
    return dct


def dct_r_txt():
    try:
        f = open("Scores.txt", 'r')
    except IOError as e:
        print(e.errno)
        return False
    dct = json.loads(f.read())
    f.close()

    return dct
