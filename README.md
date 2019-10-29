# 明治大学行動経済学研究所
## 概要
oTreeの改修中です.
何らかの改変を行ったプログラムは先頭に「(改)」を、  
改変が不要な場合は「（未改変）」をそれぞれ付け  
リストの上に並べ替えています.

### 疑問点
全ページ表示後の「Finished」と表示される画面（OutOfRangeNotification.html）で  
日本語が「これ以上表示するページはりません」となる件ですが  
otree本体の日本語訳が間違っているのが問題のようです.  
ファイルの場所は仮想環境下で  
\Lib\site-packages\otree\locale\ja\LC_MESSAGES\django.po
にあります.  
ただ、ここを書き換えても表示は直らないんですよね...

### 改修点
#### pggfg/pggfg5  
起動しない理由として
models.pyのsender receiverのパラメータに"on_delete"が抜けていました.
(Djangoのバージョン違いによるバグかもしれません.)

#### ret_adding  
class Player(BasePlayer)/def score_round内
self.payoff_score を c(0)から 0に型変更.
デバッグ用に実験時間を30秒に変更中.

#### ret_typing  
同上  
時間切れ後の読み込みが400ページ全部読み込んでるような動作っぽいので  
軽量化できるポイントかもです.  

#### survey  
models.py/class Player/def set_payoffに　q_countryを追加.  
文言を'あなたの出身国を教えて下さい'に設定.

#### real_effort
Results.htmlに next_button を追加
