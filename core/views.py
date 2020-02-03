from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import summForm, ranktopoption
import requests

# Variable Global que guarda la KEY de la API

urlKEY = 'RGAPI-d3571e2f-ed4e-45fd-9a96-eae84b7be616'

# Create your views here.

def idchamp():
    all_champion_id = {
        1: "Annie",
        2: "Olaf",
        3: "Galio",
        4: "TwistedFate",
        5: "XinZhao",
        6: "Urgot",
        7: "LeBlanc",
        8: "Vladimir",
        9: "Fiddlesticks",
        10: "Kayle",
        11: "Master Yi",
        12: "Alistar",
        13: "Ryze",
        14: "Sion",
        15: "Sivir",
        16: "Soraka",
        17: "Teemo",
        18: "Tristana",
        19: "Warwick",
        20: "Nunu",
        21: "MissFortune",
        22: "Ashe",
        23: "Tryndamere",
        24: "Jax",
        25: "Morgana",
        26: "Zilean",
        27: "Singed",
        28: "Evelynn",
        29: "Twitch",
        30: "Karthus",
        31: "Cho'Gath",
        32: "Amumu",
        33: "Rammus",
        34: "Anivia",
        35: "Shaco",
        36: "Dr.Mundo",
        37: "Sona",
        38: "Kassadin",
        39: "Irelia",
        40: "Janna",
        41: "Gangplank",
        42: "Corki",
        43: "Karma",
        44: "Taric",
        45: "Veigar",
        48: "Trundle",
        50: "Swain",
        51: "Caitlyn",
        53: "Blitzcrank",
        54: "Malphite",
        55: "Katarina",
        56: "Nocturne",
        57: "Maokai",
        58: "Renekton",
        59: "JarvanIV",
        60: "Elise",
        61: "Orianna",
        62: "MonkeyKing",
        63: "Brand",
        64: "LeeSin",
        67: "Vayne",
        68: "Rumble",
        69: "Cassiopeia",
        72: "Skarner",
        74: "Heimerdinger",
        75: "Nasus",
        76: "Nidalee",
        77: "Udyr",
        78: "Poppy",
        79: "Gragas",
        80: "Pantheon",
        81: "Ezreal",
        82: "Mordekaiser",
        83: "Yorick",
        84: "Akali",
        85: "Kennen",
        86: "Garen",
        89: "Leona",
        90: "Malzahar",
        91: "Talon",
        92: "Riven",
        96: "KogMaw",
        98: "Shen",
        99: "Lux",
        101: "Xerath",
        102: "Shyvana",
        103: "Ahri",
        104: "Graves",
        105: "Fizz",
        106: "Volibear",
        107: "Rengar",
        110: "Varus",
        111: "Nautilus",
        112: "Viktor",
        113: "Sejuani",
        114: "Fiora",
        115: "Ziggs",
        117: "Lulu",
        119: "Draven",
        120: "Hecarim",
        121: "Khazix",
        122: "Darius",
        126: "Jayce",
        127: "Lissandra",
        131: "Diana",
        133: "Quinn",
        134: "Syndra",
        136: "AurelionSol",
        141: "Kayn",
        142: "Zoe",
        143: "Zyra",
        145: "Kai'sa",
        150: "Gnar",
        154: "Zac",
        157: "Yasuo",
        161: "Velkoz",
        163: "Taliyah",
        164: "Camille",
        201: "Braum",
        202: "Jhin",
        203: "Kindred",
        222: "Jinx",
        223: "TahmKench",
        235: "Senna",
        236: "Lucian",
        238: "Zed",
        240: "Kled",
        245: "Ekko",
        246: "Qiyana",
        254: "Vi",
        266: "Aatrox",
        267: "Nami",
        268: "Azir",
        350: "Yuumi",
        412: "Thresh",
        420: "Illaoi",
        421: "Rek'Sai",
        427: "Ivern",
        429: "Kalista",
        432: "Bard",
        497: "Rakan",
        498: "Xayah",
        516: "Ornn",
        517: "Sylas",
        518: "Neeko",
        555: "Pyke",
    }
    return all_champion_id

def home(request):
    url = 'https://la2.api.riotgames.com/lol/platform/v3/champion-rotations'
    args = { 'api_key': urlKEY }
    response = requests.get(url, params=args)
    idchampconfirmed = idchamp()

    if response.status_code == 200:
        response_json = response.json()
        freeChampionIds = response_json['freeChampionIds']
        champfree = [] 
        for x, y in idchampconfirmed.items():
            for i in freeChampionIds:
                if x == i:
                    champfree.append(y)
        data = {
            'freeChampionIds':freeChampionIds,
            'all_champion_id':idchampconfirmed,
            'champfree':champfree,
            'summForm':summForm(),
        }
    
    if request.method == 'POST':
        summoner = summForm(request.POST)
        if summoner.is_valid():
            user = summoner.cleaned_data['idsumm']
            server = summoner.cleaned_data['server']
            return HttpResponseRedirect('summoner/'+server+'/'+user)
    return render(request, 'core/home.html', data)

def summoner(request,serverid,summonerid):
    invocador = summonerid
    url = 'https://'+serverid+'.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+invocador
    args = { 'api_key': urlKEY }
    response = requests.get(url, params=args)
    if response.status_code == 200:
        response_json = response.json()
        levelinvocador = response_json['summonerLevel']
        nameinvocador = response_json['name']
        iconoinvocador = response_json['profileIconId']
        data = {
            'icono':iconoinvocador,
            'nombre':nameinvocador,
            'nivel':levelinvocador
        }
    else:
        data = {
            'mensajeError':'Nombre de Invocador No Encontrado'
        }
    return render(request, 'core/summoner.html', data)

def ranktop(request):
    data = {
        'ranktopoption':ranktopoption
    }
    return render(request, 'core/ranktop.html', data)

def champs(request):
    _idchamp = idchamp()
    tag_champ = {}
    for x, y in _idchamp.items():
        url = 'http://ddragon.leagueoflegends.com/cdn/10.2.1/data/es_AR/champion/'+y+'.json'
        response = requests.get(url)
        if response.status_code == 200:
            response_json = response.json()
            datachamp = response_json['data']
            identifiedchamp = datachamp[y]
            tagchamp = identifiedchamp['tags']
            tag_champ[y] = tagchamp
            data = {
                'idchamp':_idchamp.values(),
                'tag_champ':tag_champ
            }
    return render(request, 'core/champs.html', data)

def championid(request,champid):

    url = 'http://ddragon.leagueoflegends.com/cdn/10.2.1/data/es_AR/champion/'+champid+'.json'
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        datachamp = response_json['data']
        identifiedchamp = datachamp[champid]
        titlechamp = identifiedchamp['title']
        namechamp = identifiedchamp['id']
        tagchamp = identifiedchamp['tags']
        imagechamp = 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/'+namechamp+'_0.jpg'
        data = {
            'namechamp':namechamp,
            'titlechamp':titlechamp.capitalize(),
            'imagechamp':imagechamp,
            'tagchamp':tagchamp
        }
    return render(request, 'core/champsid.html',data)