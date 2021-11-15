from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import User,Note
from . import db
import json
from time import sleep
from rank import top3rank
from DctToTxt import dct_r_txt
from GuessGame import playHTML
from CurrencyRouletteGame import playHTML as Play1
from CurrencyRouletteGame import PlayHTML2 as play2
from Score import add_score
from memoGame import getHTML,playHTML as playmemo
views = Blueprint('views', __name__)

lst = []
bugfix = []
scorelst = []
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == 'GET':
        render_template('home.html', user=current_user)
    if request.method == 'POST':
        game = request.form.get('game_select')
        level = request.form.get('level_select') or 0  # if user not push level it well automaticlly be error
        # print(level)
        # print(game)
        if int(level) < 1 or int(level) > 5:
            flash('level is must be between 1-5!', category='error')
        elif game == '0':
            flash('must pick up a game !', category='error')

        global bugfix
        global scorelst
        bugfix.append(level)
        scorelst.append(level)

        if game == '1':
            flash('lets play!', category='success')
            # response = requests.post(url, data=data, headers=headers)
            # guessgame(level)

            #return render_template('GuessGame.html', value=level,user = current_user)
            return redirect(url_for('views.guessgame', value=level))
        if game == '2':
            flash('lets play!', category='success')
            return redirect(url_for('views.currencyy_roulette_game', value=level))
            # return render_template('GuessGame.html', value = level,user = current_user)
        if game == '3':
            flash('lets play!', category='success')
            return redirect(url_for('views.memo_game', value=level))
            # return render_template('GuessGame.html', value = level,user = current_user)

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/GuessGame', methods=['GET', 'POST'])
def guessgame():
    if request.method == 'GET':

        level = bugfix[0]
        return render_template('GuessGame.html',value = level,user = current_user)

    if request.method == 'POST':
        level = int(bugfix.pop())
        user_guess = request.form.get('user_guess')
        print(user_guess)
        results = playHTML(level, user_guess)
        if results == True:
            flash("nice guess !", category='succsess')
            return redirect(url_for('views.scores',user = current_user))

        else:
            flash("ohh no !,maybe next time,try again !",category='error')
            return redirect(url_for('views.home', user=current_user))

    return render_template("GuessGame.html", user=current_user)


@views.route('/CurrencyyRouletteGame', methods=['GET', 'POST'])
def currencyy_roulette_game():
    if request.method == 'GET':

        level = bugfix[0]
        global lst
        lst = Play1(level)
        print(lst)
        return render_template('CurrencyR.html',Money_Value = lst[1],user = current_user)

    if request.method == 'POST':
        user_guess = request.form.get('user_guess')
        print(user_guess)
        print(lst[0])
        results = play2(lst[0], user_guess)
        if results == True:
            flash("nice guess !", category='succsess')
            return redirect(url_for('views.scores',user = current_user))

        else:
            flash("ohh no !,maybe next time ,try again!",category='error')
            return redirect(url_for('views.home', user=current_user))

    return render_template("CurrencyR.html", user=current_user)




@views.route('/ScoreTable', methods=['GET', 'POST', 'DELETE'])
def scores():
    user = current_user.email
    print(scorelst[0])
    add_score(int(scorelst[0]),user)
    dct = dct_r_txt()
    rankList = top3rank(dct)
    #print(rankList)
    return render_template("ScoreTable.html",user = current_user,ranklist = rankList)






@views.route('/MemoGame', methods=['GET', 'POST'])
def memo_game():
    if request.method == 'GET':
        global bugfix
        level = bugfix.pop()
        print(level)
        global lst
        sleep(3)
        lst = getHTML(level)
        print(lst)
        return render_template('memoGame.html',Money_Value = lst ,user = current_user),{"Refresh": "1; url=/MemoGame_show"}



@views.route('/MemoGame_show', methods=['GET', 'POST'])
def memo_game_show():
  if request.method == 'GET':
        print('showtime')
        print(lst)
        return render_template('memo_show.html',Money_Value= int(len(lst)),user = current_user)

  if request.method == 'POST':
       myseq =[]
       for i in range(len(lst)):
        user_guess = request.form.get('user_guess'+str(i))
        myseq.append(user_guess)
        print(user_guess)

       results = playmemo(lst,myseq)
       if results == True:
           flash("nice guess !", category='succsess')
           return redirect(url_for('views.scores',user = current_user))

       else:
           flash("ohh no !,maybe next time !",category='error')
           return redirect(url_for('views.home',user = current_user))

  return render_template("memo_show.html",Money_Value=len(lst),user=current_user)