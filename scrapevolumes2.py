# import libraries

import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify url

cmcmktvols = "https://coinmarketcap.com/currencies/ethereum/#markets"

# query site and retun the html to 'page'

page = urlopen(cmcmktvols)

# parse to beautifulsoup and store as 'soup'

soup = BeautifulSoup(page, "html.parser")

# <tr role="row" class="odd">

totvolbox = soup.find("div", attrs={"class":"coin-summary-item col-xs-6 col-md-3"})
totalvolume = totvolbox.text
print(totalvolume)

# Take out the <div> of name and get its value

arrtext = []
arrvols = []

for i in soup.find_all("a"):
   if i.parent.name == "td":
       print(i.text); arrtext.append(i.text)

for volbyexch in soup.find_all("span", class_="volume"):
    volumestring = (volbyexch.text.replace(',',''));  
    volumestring2 = volumestring.replace('$','');
    arrvols.append(volumestring2)

# There must be a nicer way to do this than two separate replace options. "Strip" is unreliable. Perhaps better to remove '$' from the soup in one pass rather than within a loop.


print(*arrtext, sep="\n")

arrvols = list(map(float, arrvols))

print(*arrvols, sep="\n")

print('')

print(len(arrtext))
print(len(arrvols))

# create a 2-D array combining volume with pairs (to make the chart)

arrcombine = []

#j is dummy variable for pulling out every second entry in arrtext (the pairs)

pairs = arrtext[1::2]
print(*pairs)

j=0

for k in arrvols:
  arrcombine.append([k, pairs[j]]); j=j+1

print(*arrcombine, sep="\n")

# print statement just to check the array looks right.

# right now the displayed pairs are hardcoded in. better would be to use the top 10 by volume, say. this would also increase modularity.

ethkrw = 0

ethusd = 0

ethcny = 0

ethusdt = 0

ethbtc = 0

ethcad = 0

etheur = 0

omgeth = 0

neoeth = 0

gnteth = 0

xrpeth = 0

etherc = 0

pairsmatrix = np.array(arrcombine)

for p in arrcombine:
   if p[1] == 'ETH/KRW':
       ethkrw = ethkrw + p[0]
   elif p[1] == 'ETH/USD':
       ethusd = ethusd + p[0]
   elif p[1] == 'ETH/CNY':
       ethcny = ethcny + p[0]
   elif p[1] == 'ETH/USDT':
       ethusdt = ethusdt + p[0]
   elif p[1] == 'ETH/BTC':
       ethbtc = ethbtc + p[0]
   elif p[1] == 'ETH/EUR':
       etheur = etheur + p[0]
   elif p[1] == 'GNT/ETH':
       etherc = etherc + p[0] 
   elif p[1] == 'NEO/ETH':
       neoeth = neoeth + p[0]
   elif p[1] == 'XRP/ETH':
       xrpeth = xrpeth + p[0]
   elif p[1] == 'ETH/CAD':
       ethcad = ethcad + p[0]
   elif p[1] == 'OMG/ETH':
       etherc = etherc + p[0]

#case statement would be quicker, again parametrizing by the highest volume pairs would increase modularity. same goes for the charts.


#fig1, ax1 = plt.subplots()
#ax1.pie(pairsmatrix[:,0], labels=pairsmatrix[:,1])

explode = [0.05]*10

#fig1, ax1 = plt.subplots()
#ax1.pie([ethkrw, ethusd, ethcny, ethbtc, ethusdt, ethcad, etheur, gnteth, neoeth, xrpeth], explode=explode, labels=['ETH/KRW', 'ETH/USD', 'ETH/CNY', 'ETH/BTC', 'ETH/USDT', 'ETH/CAD', 'ETH/EUR', 'GNT/ETH', 'NEO/ETH', 'XRP/ETH'])

#ax1.axis('equal')

#plt.show()

x = np.char.array(['ETH/KRW', 'ETH/USD', 'ETH/CNY', 'ETH/BTC', 'ETH/USDT', 'ETH/CAD', 'ETH/EUR', 'ERC20/ETH', 'NEO/ETH', 'XRP/ETH'])
y = np.array([ethkrw, ethusd, ethcny, ethbtc, ethusdt, ethcad, etheur, etherc, neoeth, xrpeth])
#colors = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan']
porcent = 100.*y/y.sum()

patches, texts = plt.pie(y, startangle=90, radius=1.0, explode=explode)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]

sort_legend = True
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
                                          key=lambda x: x[2],
                                          reverse=True))

plt.legend(patches, labels, loc='center left', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

plt.savefig('piechart.png', bbox_inches='tight')

plt.axis('equal')

plt.show()

#for p in arrcombine:
#   if p[1] == 'ETH/KRW':
#        ethkrw = ethkrw + p[0]

#print(ethkrw)
