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


author = '後藤　晶'

doc = """
Yamagishi, T., Mifune, N., Li, Y., Shinada, M., Hashimoto, H., Horita, Y., ... Simunovic, D. (2013). Is behavioral pro-sociality game-specific? Pro-social preference and expectations of pro-sociality. Organizational Behavior and Human Decision Processes, 120(2), 260–271. doi: 10.1016/j.obhdp.2012.06.002
"""


class Constants(BaseConstants):
    name_in_url = 'Trust_gen'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Trust_1 = models.IntegerField(initial=None,
                                    choices=[
                                        [1, '全くそう思わない'],
                                        [2, 'そう思わない'],
                                        [3, 'どちらかといえばそう思わない'],
                                        [4, 'どちらともいえない'],
                                        [5, 'どちらかといえばそう思う'],
                                        [6, 'そう思う'],
                                        [7, '強くそう思う'],
                                        ],
                                verbose_name='ほとんどの人は基本的に正直である',
                                widget=widgets.RadioSelect()
                                )

    Trust_2 = models.IntegerField(initial=None,
                                    choices=[
                                        [1, '全くそう思わない'],
                                        [2, 'そう思わない'],
                                        [3, 'どちらかといえばそう思わない'],
                                        [4, 'どちらともいえない'],
                                        [5, 'どちらかといえばそう思う'],
                                        [6, 'そう思う'],
                                        [7, '強くそう思う'],
                                        ],
                                verbose_name='ほとんどの人は信頼できる',
                                widget=widgets.RadioSelect()
                                )

    Trust_3 = models.IntegerField(initial=None,
                                    choices=[
                                        [1, '全くそう思わない'],
                                        [2, 'そう思わない'],
                                        [3, 'どちらかといえばそう思わない'],
                                        [4, 'どちらともいえない'],
                                        [5, 'どちらかといえばそう思う'],
                                        [6, 'そう思う'],
                                        [7, '強くそう思う'],
                                        ],
                                verbose_name='ほとんどの人は基本的に善良で親切である',
                                widget=widgets.RadioSelect()
                                )

    Trust_4 = models.IntegerField(initial=None,
                                    choices=[
                                        [1, '全くそう思わない'],
                                        [2, 'そう思わない'],
                                        [3, 'どちらかといえばそう思わない'],
                                        [4, 'どちらともいえない'],
                                        [5, 'どちらかといえばそう思う'],
                                        [6, 'そう思う'],
                                        [7, '強くそう思う'],
                                        ],
                                verbose_name='ほとんどの人は他人を信頼している',
                                widget=widgets.RadioSelect()
                                )

    Trust_5 = models.IntegerField(initial=None,
                                    choices=[
                                        [1, '全くそう思わない'],
                                        [2, 'そう思わない'],
                                        [3, 'どちらかといえばそう思わない'],
                                        [4, 'どちらともいえない'],
                                        [5, 'どちらかといえばそう思う'],
                                        [6, 'そう思う'],
                                        [7, '強くそう思う'],
                                        ],
                                verbose_name='私は，人を信頼するほうである',
                                widget=widgets.RadioSelect()
                                )

    Trust_gen = models.IntegerField()


    def comp(self):
        self.Trust_gen = self.Trust_1 + self.Trust_2 + self.Trust_3 + self.Trust_4 + self.Trust_5