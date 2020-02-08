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

author = 'Noneclue'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'lemon'
    players_per_group = 3
    num_rounds = 3

    instructions_template = 'lemon/Instructions.html'
    initial_endowment = c(50)

    product_list = {
        'high': c(30),
        'medium': c(20),
        'low': c(10)
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sale_price = models.CurrencyField()
    sale_quality = models.StringField()

    bought_id = models.PositiveIntegerField(
        choices=[(i, 'Buy from seller %i' % i) for i in
                 range(1, Constants.players_per_group)] + [(0, 'Buy nothing')],
        widget=widgets.RadioSelect(),
        doc="""0 means no purchase made"""
    )

    def set_sale_prices(self):
        if self.bought_id != 0:
            seller = self.get_player_by_id(self.bought_id)
            self.sale_price = seller.seller_proposed_price
            self.sale_quality = seller.seller_proposed_quality

    def set_payoff(self):
        for i in self.get_players():
            i.payoff = Constants.initial_endowment

        if self.bought_id != 0:
            buyer = self.get_player_by_role('buyer')
            buyer.payoff += Constants.product_list[self.sale_quality] + 5\
                - self.sale_price

            seller = self.get_player_by_id(self.bought_id)
            seller.payoff += self.sale_price\
                - Constants.product_list[self.sale_quality]


class Player(BasePlayer):
    # seller
    seller_proposed_price = models.CurrencyField(
        min=0,
        max=Constants.initial_endowment,
        verbose_name='Please indicate a price (from 0 to %i) you want to sell'
                     % Constants.initial_endowment
    )
    seller_proposed_quality = models.StringField(
        choices=list(Constants.product_list.keys()),
        verbose_name=('あなたが生産したい品質の製品を選んでください.'
                      '/Please select a quality grade you want to produce'),
        widget=widgets.RadioSelectHorizontal()
    )

    def role(self):
        if self.id_in_group == 3:
            return 'buyer'
        else:
            return 'seller {}'.format(self.id_in_group)
