from . import models
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ratemo1(Page):
    form_model = models.Player
    form_fields = ['ratemo_1',
                    'ratemo_2',
                    'ratemo_3',
                    'ratemo_4',
                    'ratemo_5',
                    'ratemo_6',
                    'ratemo_7',
                    'ratemo_8',
                    'ratemo_9',
                    'ratemo_10',
                    'ratemo_11',
                    'ratemo_12']

class ratemo2(Page):
    form_model = models.Player
    form_fields = ['ratemo_13',
                    'ratemo_14',
                    'ratemo_15',
                    'ratemo_16',
                    'ratemo_17',
                    'ratemo_18',
                    'ratemo_19',
                    'ratemo_20',
                    'ratemo_21',
                    'ratemo_22',
                    'ratemo_23',
                    'ratemo_24']


page_sequence = [ratemo1,ratemo2]
