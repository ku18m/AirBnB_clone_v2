#!/usr/bin/python3
"""This module defines a class to manage mysql database for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


env_mysql = {}
env_mysql['env'] = os.getenv('HBNB_ENV')
env_mysql['user'] = os.getenv('HBNB_MYSQL_USER')
env_mysql['host'] = os.getenv('HBNB_MYSQL_HOST')
env_mysql['password'] = os.getenv('HBNB_MYSQL_PWD')
env_mysql['database'] = os.getenv('HBNB_MYSQL_DB')
type_storage = os.getenv('HBNB_TYPE_STORAGE')


class DBStorage:
    """This class manages storage of hbnb models in mysql"""
    __engine = None
    __session = None
    __classes = {
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
        'User': User
    }

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                env_mysql['user'],
                env_mysql['password'],
                env_mysql['host'],
                env_mysql['database']
            ),
            pool_pre_ping=True,
        )
        if env_mysql['env'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects from the current database session"""
        if cls is None:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Review).all()
            objs += self.__session.query(User).all()
        else:
            if isinstance(cls, str):
                cls = self.__classes.get(cls)
            objs = self.__session.query(cls).all()
        dics = []
        for obj in objs:
            dics.append(obj)
        return dics

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
