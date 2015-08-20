from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField, RadioField
from wtforms.validators import Required
from content import get_games

class SelectGame(Form):
    listing=get_games()
    game_tuples=[]
    for date in listing:
        for game in listing[date]:
            game_tuples.append(
                (game[0]+' @ '+game[1]+' | '+date+' | '+game[2],
                game[0]+' @ '+game[1]+' | '+date+' | '+game[2])
                )
    print game_tuples
    chosen_game=SelectField('chosen_game', choices=game_tuples, validators=[Required()])