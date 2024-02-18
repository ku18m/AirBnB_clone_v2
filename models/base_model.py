#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import re
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer,
                        String, DateTime,
                        ForeignKey, Float,
                        Table
                        )
import models


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            try:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f'
                    )
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f'
                    )
                del kwargs['__class__']
            except KeyError:
                pass
            self.set(**kwargs)
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dict_repr = self.to_dict().copy()
        dict_repr.pop('__class__', None)
        return '[{}] ({}) {}'.format(cls, self.id, dict_repr)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def set(self, **kwargs):
        """sets attributes"""
        for key, value in kwargs.items():
            if not re.findall("id", key):
                try:
                    value = float(value)
                    if value.is_integer():
                        value = int(value)
                except (ValueError, TypeError):
                    pass
            setattr(self, key, value)

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
        models.storage.save()
