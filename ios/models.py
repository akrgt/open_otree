from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
ios尺度
"""


class Constants(BaseConstants):
    name_in_url = 'ios'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):


    ios_6 = models.CharField(initial=None,
                                choices=['（1）','（2）','（3）','（4）','（5）','（6）','（7）'],
                                verbose_name='一般的に，あなたと他の人々の関係を最もよく表している図を1つ選んでください．',
                                widget=widgets.RadioSelect())


