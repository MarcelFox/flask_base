from flask import Blueprint, render_template, request
from flask import current_app as app
from App import db
from App.models.User import User

#for blackjack:
import random
import string


index = Blueprint('index', __name__)


@index.route('/')
def main_page():

    def createUser():
        admin = User(username='admin',
                     email='admin@example.com',
                     password='coconuts')
        # app.logger.info("[ADMIN]: " + admin.username)
        db.session.add(admin)
        db.session.commit()

    user = User.query.filter_by(username='admin').first()
    if user is None:
        createUser()

    return render_template('index.html', user=user)


@index.route('/ajax')
def ajax():
    if (request.args.get('tableCard1')):
        tableCard1 = request.args.get('tableCard1')

    tableCard2 = getHit()
    playerCard1 = getHit()
    playerCard2 = getHit()

    return render_template('ajax.html',
                            tableCard1 = '?',
                            tableCard2 = tableCard2,
                            playerCard1 = playerCard1,
                            playerCard2 = playerCard2,
                            tbScore = tableCard2['value'],
                            plScore = playerCard1['value'] + playerCard2['value'],
                            )


@index.route('/gethit')
def getHit():
    # https://py3.codeskulptor.org/#user304_TemoFkvS1X_0.py
    cards={
        1: ['A', 'N', 'a', 'n'],
        2: ['B', 'O', 'b', 'o'],
        3: ['C', 'P', 'c', 'p'],
        4: ['D', 'Q', 'd', 'q'],
        5: ['E', 'R', 'e', 'r'],
        6: ['F', 'S', 'f', 's'],
        7: ['G', 'T', 'g', 't'],
        8: ['H', 'U', 'h', 'u'],
        9: ['I', 'V', 'i', 'v'],
        # ['J', 'W', 'j', 'w'],
        # ['K', 'X', 'k', 'x'],
        # ['L', 'Y', 'l', 'y'],
        # ['M', 'Z', 'm', 'z']
    }
    
    cardName = random.choice(string.ascii_letters)
    for i in cards:
        if cardName in cards[i]:
            cardValue = i
            break
        else:
            cardValue = 10

    card = {'name': cardName, 'value': cardValue}

    return card


@index.route('/getCardValue')
def getCardValue():

    # https://py3.codeskulptor.org/#user304_TemoFkvS1X_0.py
    cards={
        1: ['A', 'N', 'a', 'n'],
        2: ['B', 'O', 'b', 'o'],
        3: ['C', 'P', 'c', 'p'],
        4: ['D', 'Q', 'd', 'q'],
        5: ['E', 'R', 'e', 'r'],
        6: ['F', 'S', 'f', 's'],
        7: ['G', 'T', 'g', 't'],
        8: ['H', 'U', 'h', 'u'],
        9: ['I', 'V', 'i', 'v'],
        # ['J', 'W', 'j', 'w'],
        # ['K', 'X', 'k', 'x'],
        # ['L', 'Y', 'l', 'y'],
        # ['M', 'Z', 'm', 'z']
    }
    
    cardName = request.args.get('value')
    print(cardName)
    for i in cards:
        if cardName in cards[i]:
            cardValue = i
            break
        else:
            cardValue = 10

    return str(cardValue)


app.register_blueprint(index)
