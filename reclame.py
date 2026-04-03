from algemene_functies import mijn_functies2
def aanbieding_1(smaak, prijs, korting):
    nieuweprijs = prijs * (1 - korting)
    reclame = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuweprijs:.2f} euro."
    return reclame
print (aanbieding_1("aardbei",4,0.1))
def inkomsten_totaal(totaal_inkomsten,btw):
    totaal = sum(totaal_inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
mijn_lijst = [220,430,125,160,205,90,345]
print(inkomsten_totaal(mijn_lijst,0.09))
def gemiddelde_inkomsten(gemiddelde):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
print(gemiddelde_inkomsten(mijn_lijst))
def laag_hoog(mijn_lijst):
    return [min(mijn_lijst), max(mijn_lijst)]
print(laag_hoog(mijn_lijst))
def meervoudig(invoerlijst):
    return laag_hoog(invoerlijst)
invoerlijst = [10,5,3,2,1,2,9]
print(meervoudig(invoerlijst))
def combinatie(invoer_lijst_2):
    korte_lijst = laag_hoog(invoer_lijst_2)
    return mijn_functies2(korte_lijst[0], korte_lijst[1])
print(combinatie(invoerlijst))