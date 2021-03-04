import urllib.request


def download(town):
    if town == 'Montpellier':
        url = 'https://data.montpellier3m.fr/sites/default/files/ressources/'
        csv_f = 'TAM_MMM_TpsReel.csv'
        dl = "TempsReel_MPL.csv"
        urllib.request.urlretrieve(url + csv_f, dl)
        return dl

    elif town == 'Rennes':
        url1 = 'https://data.rennesmetropole.fr/explore/dataset/'
        url2 = 'prochains-passages-des-lignes-de-metro-du-reseau-star-en-'
        url3 = 'temps-reel/download/?format=csv&timezone=Europe/'
        csv_f = 'Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
        dl = "TpsReel_RNS.csv"
        urllib.request.urlretrieve(url1 + url2 + url3 + csv_f, dl)
        return dl

    elif town == 'Lille':
        url1 = 'https://opendata.lillemetropole.fr/explore/dataset/'
        url2 = 'ilevia-prochainspassages/download/?format=csv&timezone=Europe/'
        csv_f = 'Paris&lang=fr&use_labels_for_header=true&csv_separator=%3B'
        dl = "TpsReel_LIL.csv"
        urllib.request.urlretrieve(url1 + url2 + csv_f, dl)
        return dl

    elif town == 'Angers':
        url1 = 'https://data.angers.fr/explore/dataset/'
        url2 = 'bus-tram-circulation-passages/download/'
        url3 = '?format=csv&timezone=Europe/'
        csv_f = 'Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
        dl = "TpsReel_ANE.csv"
        urllib.request.urlretrieve(url1 + url2 + url3 + csv_f, dl)
        return dl
