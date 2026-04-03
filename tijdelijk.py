from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aardbei" : "3",
        "vanille" : "4",
        "chocolade" : "5"
    }
    aanbieding = (3*0.8)
    reclame_tekst = F"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}."
    reclame_tekst2 = reclame_tekst[:63]
    reclame_tekst3 = reclame_tekst2.upper()
    reclame_tekst4 = reclame_tekst3.split()
    for el in reclame_tekst2.split() :
        if len(el) >= 5:
            print(el.upper())
        else:
            print(el)
decoreer("aanbieding")
print_aanbieding()