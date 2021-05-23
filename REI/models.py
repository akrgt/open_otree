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
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'REI'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ratemo_1 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='たいていの人より，ものごとを論理的に解決するのが上手である．',
                                widget=widgets.RadioSelect())
    ratemo_2 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='直観に頼らなければならない状況は好きではない．',
                                widget=widgets.RadioSelect())
    ratemo_3 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='自分の予感を信じることにしている．',
                                widget=widgets.RadioSelect())
    ratemo_4 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='論理的な考えの持ち主だ．',
                                widget=widgets.RadioSelect())
    ratemo_5 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='ものごとを注意深く理論的に解決するのは，得意ではない．',
                                widget=widgets.RadioSelect())
    ratemo_6 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常に当てはまる'],
                                verbose_name='簡単な問題より複雑な問題の方が好きだ．',
                                widget=widgets.RadioSelect())
    ratemo_7 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='なぜだか理由を説明できないが，その人が正しいか間違っているかを，感じとることができる．',
                                widget=widgets.RadioSelect())
    ratemo_8 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常に当てはまる'],
                                verbose_name='分析的に考える方ではない．',
                                widget=widgets.RadioSelect())
    ratemo_9 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='私にはすごい直観力はない．',
                                widget=widgets.RadioSelect())
    ratemo_10 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='考えることは，楽しいことだと思わない．',
                                widget=widgets.RadioSelect())
    ratemo_11 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='直観は問題を解決するのに役立つ方法だろう．',
                                widget=widgets.RadioSelect())
    ratemo_12 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='感情に基づいて重要な決定をするのは，愚かなことだと思う．',
                                widget=widgets.RadioSelect())
    ratemo_13 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='行動を決める時，直観に頼ることが多い．',
                                widget=widgets.RadioSelect())
    ratemo_14 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='私にとって，新しい考え方を学ぶことは，とても魅力的である．',
                                widget=widgets.RadioSelect())
    ratemo_15 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='複雑な問題を解決するのは，得意ではない．',
                                widget=widgets.RadioSelect())
    ratemo_16 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='知的な挑戦が好きだ．',
                                widget=widgets.RadioSelect())
    ratemo_17 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='直観に頼って重要な決定をするのは，いい考えだと思わない．',
                                widget=widgets.RadioSelect())
    ratemo_18 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='もし私が直観に頼るならば，間違いをおかすことが多くなるだろう．',
                                widget=widgets.RadioSelect())
    ratemo_19 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='直観的な印象に頼るのが好きだ．',
                                widget=widgets.RadioSelect())
    ratemo_20 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='一生懸命考えなければならないような問題を解決するのが好きだ．',
                                widget=widgets.RadioSelect())
    ratemo_21 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='答えを見つけるために直観に従って，うまくいかなかったことはほとんどない．',
                                widget=widgets.RadioSelect())
    ratemo_22 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='人生や生活上のいろんな問題を考えるとき，直観的にやるとうまくいく．',
                                widget=widgets.RadioSelect())
    ratemo_23 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='注意深く論理的な分析が必要とされる問題を解決するのは，得意ではない．',
                                widget=widgets.RadioSelect())
    ratemo_24 = models.CharField(initial=None,
                                choices=['全くあてはまらない','あまりあてはまらない','どちらともいえない','少しあてはまる','非常にあてはまる'],
                                verbose_name='いろいろ考えるのは好きではない．',
                                widget=widgets.RadioSelect())
