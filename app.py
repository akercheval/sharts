from flask import Flask, request, render_template
import random
app = Flask(__name__)

CARD_ORDER = {
    '2'     : 0,
    '3'     : 1,
    '4'     : 2,
    '5'     : 3,
    '6'     : 4,
    '7'     : 5,
    '8'     : 6,
    '9'     : 7,
    '10'    : 8,
    'Jack'  : 9,
    'Queen' : 10,
    'King'  : 11,
    'Ace'   : 12
}

players = 0

@app.route("/", methods=['GET'])
def hello():
    return render_template('form.html')

@app.route("/", methods=['POST'])
def start():
    name = request.form['text']
    global players
    players += 1
    return "Hello " + name + "! There are " + str(players) + " players online now"
    
    #return str(cards[name])

def deal():
    suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    faces = ["Jack", "Queen", "King", "Ace"]
    cards = []
    for suit in suits:
        for i in range(2, 11):
            newCard = (str(i), suit)
            cards.append(newCard)
        for face in faces:
            newCard = (face, suit)
            cards.append(newCard)

    random.shuffle(cards)
    hands = {'Adam' : [], 'Avery' : [], 'Phil' : [], 'Will': []}
    while cards != []:
        hands["Adam"].append(cards.pop())
        hands["Avery"].append(cards.pop())
        hands["Phil"].append(cards.pop())
        hands["Will"].append(cards.pop())
    
    for player, hand in hands.items():
        hearts = []
        clubs = []
        diamonds = []
        spades = []
        for number, suit in hand:
           if suit == "Hearts":
                hearts.append((number, suit)) 
           if suit == "Clubs":
                clubs.append((number, suit)) 
           if suit == "Diamonds":
                diamonds.append((number, suit)) 
           if suit == "Spades":
                spades.append((number, suit)) 
            
        hearts.sort(key=lambda val: CARD_ORDER[str(val[0])])
        clubs.sort(key=lambda val: CARD_ORDER[str(val[0])])
        spades.sort(key=lambda val: CARD_ORDER[str(val[0])])
        diamonds.sort(key=lambda val: CARD_ORDER[str(val[0])])
        hands[player] = hearts + clubs + diamonds + spades

    return hands
    
cards = deal()
