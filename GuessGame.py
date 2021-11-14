import random
import sys


def generate_num(level_select):
    num = random.randint(1, level_select)
    return num


def get_guess_from_user(secret_number):
    getguess = input(f"pls select number betwin 1 to {secret_number}")
    getguess = int(getguess)
    if getguess > secret_number and getguess < 1:
        raise ValueError('No way')
    return getguess


def compare_results(num, secret_number):
    if num == secret_number:
        return True
    return False


def play(level_select):
    num = get_guess_from_user(level_select)
    secret_number = generate_num(level_select)
    return (compare_results(num, secret_number))
def playHTML(level_select,num):
    num=int(num)
    secret_number = generate_num(level_select)
    return (compare_results(num, secret_number))