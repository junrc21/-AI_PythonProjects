class City:

    def __init__(self, name):
        self.name = name
        self.isVisited = False
        self.adj = []

    def addCityAdj(self, city):
        self.adj.append(city)

        