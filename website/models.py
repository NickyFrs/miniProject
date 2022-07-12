
from flask_login import UserMixin
from sqlalchemy.sql import func
from website.dbstore import sdb

class Users(sdb.Model, UserMixin):
    id = sdb.Column(sdb.Integer, primary_key=True)
    username = sdb.Column(sdb.String(150), unique=True, nullable=False)
    email = sdb.Column(sdb.String(150), unique=True, nullable=False)
    password = sdb.Column(sdb.String(100), nullable=False)
    first_name = sdb.Column(sdb.String(60), nullable=False)
    last_name = sdb.Column(sdb.String(60), nullable=False)
    registered_at = sdb.Column(sdb.DateTime(timezone=True), default=func.now())
    last_login = sdb.Column(sdb.DateTime(timezone=True), default=func.now())
    # profile = sdb.Column(Text(255)), nullable=False)
    # intro
    notes = sdb.relationship('Notes')
    posts = sdb.relationship('Posts')
    
    def __repr__(self):
       return '<User {}>'.format(self.username)

                      
    
class Notes(sdb.Model):
    id = sdb.Column(sdb.Integer(), primary_key=True)
    data = sdb.Column(sdb.String(5000))
    date = sdb.Column(sdb.DateTime(timezone=True), default=func.now())
    user_id = sdb.Column(sdb.Integer, sdb.ForeignKey('users.id'))
                     
                
class Posts(sdb.Model):
    id = sdb.Column(sdb.Integer, primary_key=True)
    author_id = sdb.Column(sdb.Integer, sdb.ForeignKey('users.id'))
    # parentId
    # title
    # metaTitle
    # slug
    # summary
    # published
    # createdAt
    # updatedAt
    # publishedAt
    # content
 