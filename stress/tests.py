from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):

    def play_round(self):
        # start game
        yield MyPage
        yield Results
