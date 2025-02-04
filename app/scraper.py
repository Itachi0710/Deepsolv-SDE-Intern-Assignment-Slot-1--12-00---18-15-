import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_facebook_page_details(username: str):
    url = f'https://www.facebook.com/{username}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract data (you can extend this based on what you need)
    page_name = soup.find('title').text
    profile_pic = soup.find('img', {'class': 'profilePic'})['src']
    email = soup.find('a', {'href': 'mailto:'})  # Email extraction (if available)
    website = soup.find('a', {'href': 'https://www.facebook.com/'})['href']  # Website URL (if available)
    category = soup.find('div', {'class': 'profileDetails'}).text.strip()  # Category
    
    # Getting followers and likes (this might change based on Facebook's structure)
    followers_count = int(soup.find('div', {'class': 'followers'}).text.replace('Followers', '').strip())
    likes_count = int(soup.find('div', {'class': 'likes'}).text.replace('Likes', '').strip())
    
    page_details = {
        'username': username,
        'page_name': page_name,
        'profile_pic': profile_pic,
        'email': email,
        'website': website,
        'category': category,
        'followers_count': followers_count,
        'likes_count': likes_count,
        'created_at': datetime.now()  # Placeholder for the page creation date
    }

    return page_details
