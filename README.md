# cmcscraper

beautifulsoup based scraper

Pulls 24H pair trading volume data from coinmarketcap.com for cryptocurrencies, aggregates individual pairs across exchanges (USD, JPY, KRW, BTC etc.), and displays this as a pie chart via numpy. This allows one to track which pairs are strongest (e.g., "Korea is showing interest in X").

Currently hard-coded for certain Ethereum pairs, this could easily be modified to work for arbitrary high-volume pairs. 
