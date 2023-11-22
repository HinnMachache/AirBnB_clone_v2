#!/usr/bin/python3
"""This module defines a DBStorage class for all models in our hbnb clone"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """A DBStorage class for all hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the enviroment variables"""
        USER = getenv("HBNB_MYSQL_USER")
        PASSWD = getenv("HBNB_MYSQL_PWD")
        HOST = getenv("HBNB_MYSQL_HOST")
        DB = getenv("HBNB_MYSQL_DB")
        ENV = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format
                                      (USER, PASSWD, HOST, DB),
                                      pool_pre_ping=True)

        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieves all Classes in db"""
        classes = [User, State, Amenity, Review, City, Place]
        dic = {}

        if cls:
            query = self.__session.query(eval(cls))
            for data in query:
                key = "{}.{}".format(type(data).__name__, data.id)
                print(key)
                dic[key] = data
                del dic[key]._sa_instance_state
        else:
            for obj in classes:
                query = self.__session.query(obj)
                for data in query:
                    key = "{}.{}".format(type(data).__name__, data.id)
                    dic[key] = data
                    del dic[key]._sa_instance_state
        return dic

    def new(self, obj):
        """Adds an obj to the current session"""
        self.__session.add(obj)

    def save(self):
        """Save all changes to tje db"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an obj from the db"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the obj"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()
