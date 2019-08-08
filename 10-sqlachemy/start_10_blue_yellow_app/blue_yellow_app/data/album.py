import sqlalchemy
from blue_yellow_app.data.modelbase import SqlAlchemyBase


class Album(SqlAlchemyBase):
    __tablename__ = 'Album'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    price = sqlalchemy.Column(sqlalchemy.Float)
    album_image = sqlalchemy.Column(sqlalchemy.String)