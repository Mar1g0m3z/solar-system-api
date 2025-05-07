from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db

# class Planet:
#     def __init__(self, id, name, description, number_of_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.number_of_moons = number_of_moons


# planets = [
#     Planet(1, "Venus", "A scorching, cloud-covered planet. It is the same size as earth but with hostile conditions.", 0),
#     Planet(2, "Earth", "Only known planet to support life, covered by vast oceans and diverse ecosystem", 1),
#     Planet(3, "Jupiter", "The largest planet in the solar system, a massive gas ciant with a powerful magnetic field", 95),
#     Planet(4, "Saturn", "A stunning gas giant famous for its beautiful, extensive ring system", 146)
# ]
class Planet(db.Model):
    # planet will have id attribute, maps to a DB column of type int. if no id given, auto increment a value?
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    number_of_moons: Mapped[int]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "number_of_moons": self.number_of_moons
        }

    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name=planet_data["name"],
            description=planet_data["description"],
            number_of_moons=planet_data["number_of_moons"]
        )
