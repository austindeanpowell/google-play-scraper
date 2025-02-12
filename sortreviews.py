#JSON formats data in human-readable style to serialize and deserialize, ideal for use in APIs and data storage.
import json
from datetime import date, datetime
from google_play_scraper import Sort, reviews

# Fetch 15 reviews for co_star, only with 5-star ratings
co_star_reviews, _ = reviews(
    #Put URL here
    'com.costarastrology',
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    #Replace Count and filter_Score_with desired outcome
    count=15,
    filter_score_with=3
)

# Print the results in a readable format
print("\nCo-star Reviews:")
print(json.dumps(co_star_reviews, indent=4, sort_keys=True, default=str))
