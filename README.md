# Reddit scraper

This repo contains a simple library `reddit_scraper` and walkthrough notebook  `reddit_scraper_walkthrough.ipynb` that illustrates how to scrape simple statistics from reddit using [grequests](https://github.com/spyoungtech/grequests) and sqlite.

## Install instructions

After pulling the repo install the small set of requirements to use the `reddit_scraper` library

```python
pip install -r requirements.txt
```

## Create a sqlite database to contain the scraped data

Create a sqlite database (in the directory of this repo) to store scraped data

```python
python reddit_scraper/sqlite_interactions.py
```

## Start scraping

Start scraping on a 30 minute interval.

```python
python reddit_scraper/main.py
```

To run in the background add `&` to the end of the above, or run in a screen.

## Start dashboard

Start a dash dashboard to visualize results.

```python
python dashboard/main.py
```