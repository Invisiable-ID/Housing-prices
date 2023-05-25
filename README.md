# Housing-prices
Statistics of Shenzhen district housing prices, using Crawler and Python Visualization

"https://sz.lianjia.com/ershoufang/dapengxinqu/". It's a website containing Housing prices in many cities in China. This project requires data of housing prices of every district in ShenZhen, China.

We use Crawler to collect the data as well as process it by using Python Visualization method.

## Crawler
Program files include _init_.py, items.py, middlewares.py, pipelines.py, settings.py and Lianjia.py(on "Crawler Main Program" branch).

XPath, also known as XML path is query language for selecting nodes from an XML or an HTML document.

XPath is the most important part. Writing an XPath is pretty time consuming and for the real-time scenario, it is almost not the desired way for professionals as well as managers because it consumes a lot of time and affects the production. We use a browser extension called Ruto-XPath Finder. 

* FIRST, use Python Program to visit the target website, and get the page. 
* NEXT, filter out key information with XPath. 
* THEN, auto page turning function is needed. That makes it possible for us to loop through all pages of this website.
* FINALLY, produce documents and forms.

## Python Visualization(Pandas, Numpy, Seaborn and Matplotlib)
"Python Visualization.ipynb" is the main file of this part.

Draw bar charts and pie charts.
