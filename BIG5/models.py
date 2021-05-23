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
import random
from django import forms


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'BIG5'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    big5_1 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='活発で，外向的だと思う',
                                widget=forms.RadioSelect())

    big5_2 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='他人に不満をもち，もめごとを起こしやすいと思う',
                                widget=forms.RadioSelect())

    big5_3 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='しっかりしていて，自分に厳しいと思う',
                                widget=forms.RadioSelect())

    big5_4 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='心配性で，うろたえやすいと思う',
                                widget=forms.RadioSelect())

    big5_5 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='新しいことが好きで，変わった考えをもつと思う',
                                widget=forms.RadioSelect())

    big5_6 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='ひかえめで，おとなしいと思う',
                                widget=forms.RadioSelect())

    big5_7 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='人に気をつかう，やさしい人間だと思う',
                                widget=forms.RadioSelect())

    big5_8 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='だらしなく，うっかりしていると思う',
                                widget=forms.RadioSelect())

    big5_9 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='冷静で，気分が安定していると思う',
                                widget=forms.RadioSelect())

    big5_10 = models.CharField(initial=None,
                                choices=['1.全く違うと思う','2.おおよそ違うと思う','3.少し違うと思う','4.どちらでもない','5.少しそう思う','6.まあまあそう思う','7.強くそう思う'],
                                verbose_name='発想力に欠けた，平凡な人間だと思う',
                                widget=forms.RadioSelect())
