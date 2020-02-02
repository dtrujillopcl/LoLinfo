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

class summForm(forms.Form):
    idsumm = forms.CharField(max_length=50, label='')
    server = forms.ChoiceField(required=True,label='',choices=SERVERS_CHOICE)
