from City import City
from Adjacent import Adjacent

class Map:
    SaoPaulo = City("São Paulo")
    RioJaneiro = City("Rio de Janeiro")
    Bahia = City("Bahia")
    Minas = City("Minas Gerais")
    EspiritoSanto = City("Espirito Santo")
    MatoGrosso = City("Mato Grosso")
    Parana = City("Parana")
    RioGrandeNorte = City("Rio Grande do Norte")
    Recife = City("Recife")
    Alagoas = City("Alagoas")
    Para = City("Para")
    Amazonas = City("Amazonas")
    Brasilia = City("Brasilia")
    RioGrandeSul = City("Rio Grande Sul")
    
    SaoPaulo.addCityAdj(Adjacent(RioJaneiro))
    SaoPaulo.addCityAdj(Adjacent(EspiritoSanto))
    SaoPaulo.addCityAdj(Adjacent(Minas))
    SaoPaulo.addCityAdj(Adjacent(Parana))

    RioJaneiro.addCityAdj(Adjacent(SaoPaulo))
    RioJaneiro.addCityAdj(Adjacent(Minas))
    RioJaneiro.addCityAdj(Adjacent(EspiritoSanto))

    Bahia.addCityAdj(Adjacent(Minas))
    Bahia.addCityAdj(Adjacent(EspiritoSanto))
    Bahia.addCityAdj(Adjacent(Alagoas))
    Bahia.addCityAdj(Adjacent(Brasilia))

    Minas.addCityAdj(Adjacent(EspiritoSanto))
    Minas.addCityAdj(Adjacent(RioJaneiro))
    Minas.addCityAdj(Adjacent(SaoPaulo))
    Minas.addCityAdj(Adjacent(Brasilia))

    EspiritoSanto.addCityAdj(Adjacent(SaoPaulo))
    EspiritoSanto.addCityAdj(Adjacent(RioJaneiro))
    EspiritoSanto.addCityAdj(Adjacent(Bahia))

    MatoGrosso.addCityAdj(Adjacent(Brasilia))
    MatoGrosso.addCityAdj(Adjacent(Amazonas))
    MatoGrosso.addCityAdj(Adjacent(Para))

    Parana.addCityAdj(Adjacent(SaoPaulo))
    Parana.addCityAdj(Adjacent(RioGrandeSul))
    
    RioGrandeNorte.addCityAdj(Adjacent(Recife))
    
    Recife.addCityAdj(Adjacent(RioGrandeNorte))
    Recife.addCityAdj(Adjacent(Alagoas))

    Alagoas.addCityAdj(Adjacent(Bahia))    
    Alagoas.addCityAdj(Adjacent(Recife))
    
    Para.addCityAdj(Adjacent(Amazonas))
    Para.addCityAdj(Adjacent(MatoGrosso))
    
    Amazonas.addCityAdj(Adjacent(Para))    
    Amazonas.addCityAdj(Adjacent(MatoGrosso))
    
    Brasilia.addCityAdj(Adjacent(SaoPaulo))
    Brasilia.addCityAdj(Adjacent(MatoGrosso))
    Brasilia.addCityAdj(Adjacent(Bahia))
    Brasilia.addCityAdj(Adjacent(Minas))
    
    RioGrandeSul.addCityAdj(Adjacent(Parana))

map = Map()

for i in range(len(map.SaoPaulo.adj)):
    print(map.SaoPaulo.adj[i].city.name)




    