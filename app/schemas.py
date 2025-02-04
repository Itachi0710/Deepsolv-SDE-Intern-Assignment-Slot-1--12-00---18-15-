from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PostSchema(BaseModel):
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True

class FollowerSchema(BaseModel):
    follower_name: str
    follower_id: int

    class Config:
        orm_mode = True

class SocialMediaUserSchema(BaseModel):
    username: str
    page_name: str
    profile_pic: str
    category: str
    followers_count: int
    likes_count: int
    created_at: datetime
    email: Optional[str] = None
    website: Optional[str] = None
    posts: List[PostSchema] = []
    followers: List[FollowerSchema] = []

    class Config:
        orm_mode = True
