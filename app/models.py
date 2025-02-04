from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
class SocialMediaUser(Base):
    __tablename__ = 'social_media_users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    page_name = Column(String)
    profile_pic = Column(String)
    email = Column(String, nullable=True)
    website = Column(String, nullable=True)
    category = Column(String)
    followers_count = Column(Integer)
    likes_count = Column(Integer)
    created_at = Column(DateTime)
    
    posts = relationship("Post", back_populates="user")
    followers = relationship("Follower", back_populates="user")
    following = relationship("Following", back_populates="user")
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    timestamp = Column(DateTime)
    page_id = Column(Integer, ForeignKey('social_media_users.id'))
    
    user = relationship("SocialMediaUser", back_populates="posts")
class Follower(Base):
    __tablename__ = 'followers'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('social_media_users.id'))
    follower_id = Column(Integer)
    follower_name = Column(String)
    
    user = relationship("SocialMediaUser", back_populates="followers")
class Following(Base):
    __tablename__ = 'following'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('social_media_users.id'))
    following_id = Column(Integer)
    following_name = Column(String)
    
    user = relationship("SocialMediaUser", back_populates="following")
