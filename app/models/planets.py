class Planet:
    def __init__(self, id, name, description, number_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.number_of_moons = number_of_moons


planets = [
    Planet(1, "Venus", "A scorching, cloud-covered planet. It is the same size as earth but with hostile conditions.", 0),
    Planet(2, "Earth", "Only known planet to support life, covered by vast oceans and diverse ecosystem", 1),
    Planet(3, "Jupiter", "The largest planet in the solar system, a massive gas ciant with a powerful magnetic field", 95),
    Planet(4, "Saturn", "A stunning gas giant famous for its beautiful, extensive ring system", 146)
]
