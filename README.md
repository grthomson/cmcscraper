# cmcscraper

beautifulsoup based scraper

Pulls 24H pair trading volume data from coinmarketcap.com for cryptocurrencies, aggregates individual pairs (USD, JPY, KRW, BTC etc.) across exchanges and displays proportion of volume by pair as a pie chart via numpy. This allows one to track which pairs are highest liquidity/volume (e.g., "Korea is showing interest in X").

Currently hard-coded for certain currency pairs, this could easily be modified to work for arbitrary high-volume pairs. 

Note that this is an exercise in scraping - the same results could be achieved more simply using the .json API

![Sample visualization](https://github.com/grthomson/cmcscraper/blob/master/figure_1.png)


