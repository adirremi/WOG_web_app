from DctToTxt import dct_r_txt, dct_w_txt


def add_score(level_select, nickname):
    POINTS_OF_WINNING = (level_select * 3) + 5
    Score_dct = dct_r_txt()
    if Score_dct == False:
        return None
    Score_dct[nickname] = Score_dct.get(nickname, 0) + POINTS_OF_WINNING
    dct_w_txt(Score_dct)


    return None
