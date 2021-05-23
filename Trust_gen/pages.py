from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

class survey(Page):
    form_model = models.Player
    form_fields = ['Trust_1',
                   'Trust_2',
                   'Trust_3',
                   'Trust_4',
                   'Trust_5']
                   
    def before_next_page(self):
        self.player.comp()



page_sequence = [survey]
