from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(60), nullable=True)
    lastname: Mapped[str] = mapped_column(String(60), nullable=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    #password: Mapped[str] = mapped_column(nullable=False)
    #is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    # Relaciones
    posts 
    comments 

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname
            # do not serialize the password, its a security breach
        }
    

#################### Comment ####################

class Comment(db.Model):

    __tablename__ = "comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(500), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False) # Usuario que comenta
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=False) # Post al que pertenece el comentario
    
def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id
            # do not serialize the password, its a security breach
        }



#################### POST ####################

class Post(db.Model):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))  # ID del autor del post


 # Relaciones
    comments 
    media 

def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }


#################### MEDIA ####################

class Media(db.Model):
    __tablename__ = "media"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[int] = mapped_column(Enum(MediaType), nullable=False) # define un conjunto de tipos de contenido multimedia
    url: Mapped[str] = mapped_column(String(60), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)

def serialize(self):
        return {
            "id": self.id,
            "type": self.type.value, # "value" dato o información que se almacena
            "url": self.url,
            "post_id": self.post_id
            # do not serialize the password, its a security breach
        }




#################### FOLLOWER ####################

class Follower(db.Model):
    __tablename__ = "follower"
    user_from_id: Mapped[int] = mapped_column(ForeignKey(user.id), primary_key=True)
    user_to_id: Mapped[int] = mapped_column(ForeignKey(user.id), primary_key=True)
    
    def serialize(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }