import urllib.request


def download(town):
    if town == 'Montpellier':
        url = 'https://data.montpellier3m.fr/sites/default/files/ressources' \
                '/TAM_MMM_TpsReel.csv'
        dl = "TpsReel_MPL.csv"
        urllib.request.urlretrieve(url, dl)
        return dl

    elif town == 'Rennes':
        url = 'https://data.rennesmetropole.fr/explore/dataset/prochains-pa' \
                'ssages-des-lignes-de-metro-du-reseau-star-en-temps-reel/do' \
                'wnload/?format=csv&timezone=Europe/Berlin&lang=fr&use_labe' \
                'ls_for_header=true&csv_separator=%3B'
        dl = "TpsReel_RNS.csv"
        urllib.request.urlretrieve(url, dl)
        return dl

    elif town == 'Lille':
        url = 'https://opendata.lillemetropole.fr/explore/dataset/ilevia-pr' \
                'ochainspassages/download/?format=csv&timezone=Europe/Paris' \
                '&lang=fr&use_labels_for_header=true&csv_separator=%3B'
        dl = "TpsReel_LIL.csv"
        urllib.request.urlretrieve(url, dl)
        return dl

    elif town == 'Angers':
        url = 'https://data.angers.fr/explore/dataset/bus-tram-circulation-' \
                'passages/download/?format=csv&timezone=Europe/Berlin&lang=' \
                'fr&use_labels_for_header=true&csv_separator=%3B'
        dl = "TpsReel_ANE.csv"
        urllib.request.urlretrieve(url, dl)
        return dl
