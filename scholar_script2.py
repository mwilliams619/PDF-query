import scholarly
from scholarly import ProxyGenerator
from collections import Counter

# Set up a ProxyGenerator object to use free proxies
# This needs to be done only once per session
# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)

# Now search Google Scholar from behind a proxy
# Define your search query
search_query = "Your search query here"

# Define the years you want to count articles for
years = list(range(2010, 2024))

# Initialize a counter for each year
article_count_by_year = Counter()

# Perform the search and count articles for each year
for year in years:
    query = scholarly.search_keywords(f'{search_query} {year}')
    article_count = sum(1 for _ in query)
    article_count_by_year[year] = article_count

# Print the results
for year, count in article_count_by_year.items():
    print(f"Year {year}: {count} articles")