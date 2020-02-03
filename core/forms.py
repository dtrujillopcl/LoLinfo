from django import forms

SERVERS_CHOICE = [
    ('la2', 'LAS'),
    ('la1', 'LAN'),
    ('br', 'Brasil'),
    ('euw1', 'EUW'),
    ('eun1', 'EUNE'),
    ('na1', 'Norteamerica'),
    ('oc1', 'Oceania'),
    ('kr', 'Corea'),
    ('jp1', 'Japon'),
    ('ru', 'Rusia'),
    ('tr1', 'Turquia'),
]

QUEUE_CHOICE = [
    ('RANKED_SOLO_5X5','Ranked SoloQ'),
    ('RANKED_TFT','Ranked TFT'),
    ('RANKED_FLEX_SR','Ranked Flex'),
    ('RANKED_FLEX_TT','Rnked Flex2')
]

TIER_CHOICE = [
    ('CHALLENGER','Retador'),
    ('GRANDMASTER','Gran Maestro'),
    ('MASTER','Maestro'),
    ('DIAMOND','Diamante'),
    ('PLATINUM','Platino'),
    ('GOLD','Oro'),
    ('SILVER','Plata'),
    ('BRONZE','Bronce'),
    ('IRON','Hierro')
]

DIVISION_CHOICE = [
    ('I','I'),
    ('II','II'),
    ('III','III'),
    ('IV','IV')
]

class summForm(forms.Form):
    idsumm = forms.CharField(max_length=50, label='')
    server = forms.ChoiceField(required=True,label='',choices=SERVERS_CHOICE)

class ranktopoption(forms.Form):
    server = forms.ChoiceField(required=True,label='Server',choices=SERVERS_CHOICE)
    queue = forms.ChoiceField(required=True,label='Queue',choices=QUEUE_CHOICE)
    tier = forms.ChoiceField(required=True,label='Tier',choices=TIER_CHOICE)
    division = forms.ChoiceField(required=True,label='Division',choices=DIVISION_CHOICE)
