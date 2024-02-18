#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import (BaseModel, Base, Column, String,
                               ForeignKey, Float, Integer, Table)


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False
        ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
        )
    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity",
                             secondary="place_amenity", viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """Returns the list of Review instances with place_id
        equals to the current Place.id
        """
        from models import storage
        from models.review import Review
        return storage.all(Review).values()

    @property
    def amenities(self):
        """Returns the list of Amenity instances with place_id
        equals to the current Place.id
        """
        from models import storage
        from models.amenity import Amenity
        return storage.all(Amenity).values()

    @amenities.setter
    def amenities(self, obj):
        """Sets the list of amenity_ids"""
        from models.amenity import Amenity
        if type(obj) is Amenity:
            self.amenity_ids.append(obj.id)
            self.save()
