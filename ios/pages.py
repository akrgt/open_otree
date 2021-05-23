from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

class ios1(Page):

    form_model = models.Player
    form_fields = ['ios_6',
                   ]

page_sequence = [ios1]
