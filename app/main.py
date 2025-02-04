from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas, services, database

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/page/{username}", response_model=schemas.SocialMediaUserSchema)
async def get_page_details(username: str, 
                            min_followers: Optional[int] = None, 
                            max_followers: Optional[int] = None,
                            name: Optional[str] = None, 
                            category: Optional[str] = None,
                            db: Session = Depends(get_db)):
    page = await services.get_page_details(username, db)
    
    if min_followers and max_followers:
        if not (min_followers <= page.followers_count <= max_followers):
            raise HTTPException(status_code=404, detail="Page not in the specified follower count range")
    
    if name and name.lower() not in page.page_name.lower():
        raise HTTPException(status_code=404, detail="Page name does not match")
    
    if category and category.lower() not in page.category.lower():
        raise HTTPException(status_code=404, detail="Page category does not match")
    
    return page

@app.get("/page/{username}/followers", response_model=List[schemas.FollowerSchema])
async def get_page_followers(username: str, db: Session = Depends(get_db)):
    page = db.query(models.SocialMediaUser).filter(models.SocialMediaUser.username == username).first()
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    
    return page.followers

@app.get("/page/{username}/posts", response_model=List[schemas.PostSchema])
async def get_page_posts(username: str, limit: int = 15, skip: int = 0, db: Session = Depends(get_db)):
    page = db.query(models.SocialMediaUser).filter(models.SocialMediaUser.username == username).first()
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    
    posts = db.query(models.Post).filter(models.Post.page_id == page.id).offset(skip).limit(limit).all()
    return posts
