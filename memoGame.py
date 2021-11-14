from GuessGame import generate_num
import time


def generate_sequence(level_select):
    seq_lst = []
    for i in range(int(level_select) ):
        seq_lst.append(generate_num(101))
    return seq_lst


def get_list_from_user(level_select):
    user_lst = []
    for i in range(level_select ):
        user_lst.append(int(input(f"pls insert your {i + 1} place seq ")))
    return user_lst


def is_list_equal(seq_lst, user_lst):
    len_of_lst = len(seq_lst)
    for i in range(len_of_lst):
        if seq_lst[i] != user_lst[i]:
            return False
    return True


def play(level_select):
    make_seq = generate_sequence(level_select)
    print(make_seq, end='')
    time.sleep(1)
    print('\r        ')
    print("time is up")
    user_seq = get_list_from_user(level_select)
    score = is_list_equal(make_seq, user_seq)
    return score

def getHTML(level_select):
    make_seq = generate_sequence(level_select)
    return make_seq

def playHTML(user_guess,make_seq):
    score =is_list_equal(user_guess,make_seq)
    return score