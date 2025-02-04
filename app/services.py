from sqlalchemy.orm import Session
from app import models, scraper

def get_page_details(username: str, db: Session):
    page = db.query(models.SocialMediaUser).filter(models.SocialMediaUser.username == username).first()

    if not page:
        # Scrape and store data
        details = scraper.fetch_facebook_page_details(username)
        if details:
            page = models.SocialMediaUser(**details)
            db.add(page)
            db.commit()
            db.refresh(page)

    return page
