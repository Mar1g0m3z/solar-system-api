from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from sqlalchemy import ForeignKey


class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(
        back_populates="moons")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "planet_id": self.planet_id,
            "planet_name": self.planet.name if self.planet else None
        }

    @classmethod
    def from_dict(cls, moon_data):
        return cls(
            name=moon_data["name"],
            planet_id=moon_data.get("planet_id", None)
        )
