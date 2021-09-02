from os import environ

SESSION_CONFIGS = [
    {
        'name': 'dictator',
        'display_name': "独裁者ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['dictator'],
    },
    {
        'name': 'ultimatum_non_strategy',
        'display_name': "直接応答法による最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
        'treatment': 'direct_response',
    },
    {
        'name': 'ultimatum_strategy',
        'display_name': "ストラテジーメソッドによる最終提案ゲーム",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum'],
        'treatment': 'strategy',
    },
    {
        'name': 'pggfg',
        'display_name': '処罰あり公共財ゲーム',
        'num_demo_participants': 3,
        'app_sequence': ['pggfg'],
    },
    dict(
        name="trust",
        display_name= "信頼ゲーム",
        num_demo_participants= 2,
        app_sequence= ['trust'],
     ),
    dict(
        name="trust_and",
        display_name= "信頼ゲームと一般的信頼",
        num_demo_participants= 2,
        app_sequence= ['trust','Trust_gen'],
     ),
     dict(
        name="svo",
        display_name= "SVOスライダー",
        num_demo_participants= None,
        app_sequence= ['svotree2'],
     ),
    dict(
        name="Trust_gen",
        display_name= "一般的信頼",
        num_demo_participants= None,
        app_sequence= ['Trust_gen'],
     ),
    dict(
        name="CRT",
        display_name= "認知反射テスト（認知熟慮テスト）",
        num_demo_participants= None,
        app_sequence= ['CRT'],
     ),
    dict(
        name="REI",
        display_name= "情報処理スタイル尺度",
        num_demo_participants= None,
        app_sequence= ['REI'],
     ),
    dict(
        name="BIG5",
        display_name= "BIG5",
        num_demo_participants= None,
        app_sequence= ['BIG5'],
     ),
    {
        'name': 'public_goods_simple',
        'display_name': "練習用の単純な公共財ゲーム",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods_simple', 'survey'],
    },
    {
        'name': 'ret_adding',
        'display_name': "リアルエフォートタスク（足し算）",
        'num_demo_participants': 1,
        'app_sequence': ['ret_adding'],
    },
    {
        'name': 'ret_typing',
        'display_name': "リアルエフォートタスク（タイピング）",
        'num_demo_participants': 1,
        'app_sequence': ['ret_typing'],
    },
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = True

ADMIN_USERNAME = 'test'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'test'

AUTH_LEVEL = 'DEMO'

DEMO_PAGE_INTRO_HTML = """
        <strong>明治大学行動経済学研究所（BEER）</strong>
<ul>
    <li>
        このサーバは明治大学情報コミュニケーション学部専任講師後藤　晶によって運営されています．
    </li>
    <li>
        なにかご不明な点があれば，akiragoto[at]meiji.ac.jpまでお問い合わせください．
    </li>
    <li>
        パスやIDは全てtestにしてあります．
    </li>
    <li>
        なお，永遠のβバージョンであり，現在も改変作業を進めています.
    </li>
</ul>

"""

SECRET_KEY = 't7&6b_b%72tug8p@9gdhmjf^v0uc!1q-!qd&4vb40uk=65*9ct'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
