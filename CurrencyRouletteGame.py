from forex_python.converter import CurrencyRates
from GuessGame import generate_num


def get_money_interval(Money_Value, level_select):
    c = CurrencyRates()
    Currency = (c.get_rate("ILS", "USD")) / 0.1  # convertUSDtoEURO
    Money_After_ex = Currency * Money_Value
    AnswerRange = [int(Money_After_ex - (5 - level_select)), int(Money_After_ex + (5 - level_select))]
    return AnswerRange


def get_guess_from_user(Money_Value):
    get_guess = input(f"The Value in USD is {Money_Value} please insert your guess in ILS!   ")
    return get_guess


def play(level_select):
    Money_Value = generate_num(100)
    Answer_rang = get_money_interval(Money_Value, level_select)
    guess_user = int(get_guess_from_user(Money_Value))
    if guess_user >= Answer_rang[0] and guess_user <= Answer_rang[1]:
        return True
    else:
        return False

def playHTML(level_select):
    Money_Value = generate_num(100)
    level_select = int(level_select)
    Answer_rang = get_money_interval(Money_Value, level_select)
    return [Answer_rang,Money_Value]

def PlayHTML2(Answer_rang,user_guess):
    guess_user = int(user_guess)
    if guess_user >= Answer_rang[0] and guess_user <= Answer_rang[1]:
        return True
    else:
        return False