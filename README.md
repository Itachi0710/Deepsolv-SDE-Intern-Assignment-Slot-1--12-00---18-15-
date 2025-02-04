# Facebook Insights Microservice

A FastAPI-based service to scrape and analyze Facebook Page insights with MongoDB storage.

## Features

- Scrape Facebook Page details (Profile, Posts, Followers)
- Store scraped data in MongoDB
- REST API endpoints for:
  - Page details retrieval
  - Search/filter pages by criteria
  - Pagination support
  - Followers/Posts listings
- Asynchronous operations
- Proper error handling
- Configurable environment settings

## Prerequisites

- Python 3.9+
- MongoDB 4.4+
- Facebook account credentials (for scraping)
- (Optional) Redis for caching

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/facebook-insights-microservice.git
cd facebook-insights-microservice

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Create .env file:
DATABASE_URL=DATABASE_URL=mysql+pymysql://root:root@localhost/facebook_insights

DB_NAME=facebook_insights


Scraping Notes
The current implementation uses basic scraping with BeautifulSoup

Facebook's anti-scraping measures might require:

Rotating user agents

Request rate limiting

Proxy rotation

Headless browser implementation (Selenium/Playwright)

Handle CAPTCHAs and login requirements appropriately

Testing
uvicorn app.main:app --reload - start the server
