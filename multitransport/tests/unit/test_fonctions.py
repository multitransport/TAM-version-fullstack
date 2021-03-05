from multitransport.fonctions import *

def test_liste_stations():
    assert isInstance(liste_stations("multitrsp.db"), list)
