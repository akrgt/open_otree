from . import models
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1


class Production(Page):
    def is_displayed(self):
        return self.player.role().startswith('seller')

    form_model = models.Player
    form_fields = ['seller_proposed_price', 'seller_proposed_quality']


class SimpleWaitPage(WaitPage):
    pass


class Purchase(Page):
    def is_displayed(self):
        return self.player.role() == 'buyer'

    form_model = models.Group
    form_fields = ['bought_id']

    def before_next_page(self):
        self.group.set_sale_prices()


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Production,
    SimpleWaitPage,
    Purchase,
    ResultsWaitPage,
    Results
]
