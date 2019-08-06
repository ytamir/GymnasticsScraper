## TODO find methods for getting all gymnasts that are not in the list like https://thegymter.net/konnor-mcclain/

## Imports
import re
import requests as req
from bs4 import BeautifulSoup

## Imports for google sheets API
import pygsheets
import pandas as pd

## Gather links from gymternet
resp = req.get("https://thegymter.net/gymnast-database/")
soup = BeautifulSoup(resp.text, 'lxml')
links = []

## Add html href to links array using regex
for link in soup.findAll('a', attrs={'href': re.compile("^http*s://")}):
    links.append(link.get('href'))

## Remove top and bottom links
removedTopLinks = [x for x in links if x not in ['https://thegymter.net/', 'https://thegymter.net/', 'https://thegymter.net/', 'https://thegymter.net/meet-coverage/', 'https://thegymter.net/2019-gymnastics-calendar/', 'https://thegymter.net/2018-gymnastics-calendar/', 'https://thegymter.net/2017-gymnastics-calendar/', 'https://thegymter.net/2016-gymnastics-calendar/', 'https://thegymter.net/2015-gymnastics-calendar/', 'https://thegymter.net/2014-gymnastics-calendar/', 'https://thegymter.net/2013-gymnastics-calendar/', 'https://thegymter.net/features/', 'https://thegymter.net/category/breaking-news/', 'https://thegymter.net/whats-your-team/', 'https://thegymter.net/category/mag/', 'https://thegymter.net/category/ncaa/', 'https://thegymter.net/category/interviews/', 'https://thegymter.net/category/qa/', 'https://thegymter.net/category/meet-the-elite/', 'https://thegymter.net/category/on-our-minds/', 'https://thegymter.net/category/the-leo-panel/', 'https://thegymter.net/category/four-year-rewind/', 'https://thegymter.net/category/in-translation/', 'https://thegymter.net/category/fun-games/', 'https://thegymter.net/gymnast-database/', 'https://thegymter.net/category/the-research-files/', 'https://thegymter.net/2020-womens-olympic-qualifiers/', 'https://thegymter.net/2020-womens-olympic-qualifiers/', 'https://thegymter.net/2020-mens-olympic-qualifiers/', 'https://thegymter.net/2018-2020-apparatus-world-cup-rankings/', 'https://thegymter.net/2018-2020-apparatus-world-cup-mens-rankings/', 'https://thegymter.net/the-best-scores-in-2019/', 'https://thegymter.net/the-best-scores-in-2019/', 'https://thegymter.net/the-best-mens-scores-in-2019/', 'https://thegymter.net/about/', 'https://thegymter.net/contribute/']]
removedTopBottomLinks = [y for y in removedTopLinks if y not in ['https://thegymter.net/gymnast-database/?share=twitter', 'https://thegymter.net/gymnast-database/?share=facebook', 'https://thegymter.net/2014/12/24/happy-holidays-from-the-gymternet/', 'https://thegymter.net/gymnast-database/#comment-6958', 'https://thegymter.net/gymnast-database/?like_comment=6958&_wpnonce=84cd555441', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-6961', 'https://thegymter.net/gymnast-database/?like_comment=6961&_wpnonce=76ecb655b2', 'https://thegymter.net/gymnast-database/#comment-14352', 'https://thegymter.net/gymnast-database/?like_comment=14352&_wpnonce=016825513a', 'https://thegymter.net/gymnast-database/#comment-9063', 'https://thegymter.net/gymnast-database/?like_comment=9063&_wpnonce=120c72e9b0', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-9068', 'https://thegymter.net/gymnast-database/?like_comment=9068&_wpnonce=cccea55bc8', 'https://thegymter.net/2016/04/02/helena-bonilla/', 'https://thegymter.net/gymnast-database/#comment-14805', 'https://thegymter.net/gymnast-database/?like_comment=14805&_wpnonce=6e09a2f298', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-14806', 'https://thegymter.net/gymnast-database/?like_comment=14806&_wpnonce=f81d3bc70b', 'https://thegymter.net/gymnast-database/#comment-17174', 'https://thegymter.net/gymnast-database/?like_comment=17174&_wpnonce=a0633e5c70', 'https://thegymter.net/2016/11/03/the-best-world-finishes-of-all-time/', 'https://thegymter.net/gymnast-database/#comment-20968', 'https://thegymter.net/gymnast-database/?like_comment=20968&_wpnonce=5a74dffc1f', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-20969', 'https://thegymter.net/gymnast-database/?like_comment=20969&_wpnonce=ccaedda2ec', 'https://thegymter.net/gymnast-database/#comment-24445', 'https://thegymter.net/gymnast-database/?like_comment=24445&_wpnonce=be94911552', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-24446', 'https://thegymter.net/gymnast-database/?like_comment=24446&_wpnonce=2a76cc484f', 'https://thegymter.net/gymnast-database/#comment-24448', 'https://thegymter.net/gymnast-database/?like_comment=24448&_wpnonce=a74a0e2f33', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-24450', 'https://thegymter.net/gymnast-database/?like_comment=24450&_wpnonce=6fb6bda0bc', 'https://thegymter.net/gymnast-database/#comment-30098', 'https://thegymter.net/gymnast-database/?like_comment=30098&_wpnonce=175fa623b2', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-30100', 'https://thegymter.net/gymnast-database/?like_comment=30100&_wpnonce=22d34fc256', 'https://thegymter.net/gymnast-database/#comment-30200', 'https://thegymter.net/gymnast-database/?like_comment=30200&_wpnonce=2c1e255066', 'https://thegymter.net/gymnast-database/#comment-45114', 'https://thegymter.net/gymnast-database/?like_comment=45114&_wpnonce=01e2612351', 'https://gravatar.com/site/signup/', 'https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=lch3153%40gmail%2ecom&lc=US&item_name=The%20Gymternet&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted', 'https://thegymter.net/2019/08/03/2019-german-championships-results/', 'https://thegymter.net/2019/08/03/2019-pan-american-games-results/', 'https://thegymter.net/2019/07/31/2019-pan-american-games-live-blog-event-finals-day-2/', 'https://thegymter.net/2019/07/30/2019-pan-american-games-live-blog-event-finals-day-1/', 'https://thegymter.net/2019/07/29/2019-pan-american-games-live-blog-mens-all-around-final/', 'https://thegymter.net/2019/07/29/2019-pan-american-games-live-blog-womens-all-around-final/', 'https://thegymter.net/2019/07/29/around-the-gymternet-never-tell-me-the-odds/', 'https://thegymter.net/2019/07/28/2019-pan-american-games-live-blog-mens-qualifications-subdivision-2/', 'https://thegymter.net/2019/07/28/2019-pan-american-games-live-blog-mens-qualifications-subdivision-1/', 'https://thegymter.net/2019/07/27/2019-pan-american-games-live-blog-womens-qualifications-subdivision-3/', 'https://www.facebook.com/thegymternet', 'https://thegymter.net/2019/08/', 'https://thegymter.net/2019/07/', 'https://thegymter.net/2019/06/', 'https://thegymter.net/2019/05/', 'https://thegymter.net/2019/04/', 'https://thegymter.net/2019/03/', 'https://thegymter.net/2019/02/', 'https://thegymter.net/2019/01/', 'https://thegymter.net/2018/12/', 'https://thegymter.net/2018/11/', 'https://thegymter.net/2018/10/', 'https://thegymter.net/2018/09/', 'https://thegymter.net/2018/08/', 'https://thegymter.net/2018/07/', 'https://thegymter.net/2018/06/', 'https://thegymter.net/2018/05/', 'https://thegymter.net/2018/04/', 'https://thegymter.net/2018/03/', 'https://thegymter.net/2018/02/', 'https://thegymter.net/2018/01/', 'https://thegymter.net/2017/12/', 'https://thegymter.net/2017/11/', 'https://thegymter.net/2017/10/', 'https://thegymter.net/2017/09/', 'https://thegymter.net/2017/08/', 'https://thegymter.net/2017/07/', 'https://thegymter.net/2017/06/', 'https://thegymter.net/2017/05/', 'https://thegymter.net/2017/04/', 'https://thegymter.net/2017/03/', 'https://thegymter.net/2017/02/', 'https://thegymter.net/2017/01/', 'https://thegymter.net/2016/12/', 'https://thegymter.net/2016/11/', 'https://thegymter.net/2016/10/', 'https://thegymter.net/2016/09/', 'https://thegymter.net/2016/08/', 'https://thegymter.net/2016/07/', 'https://thegymter.net/2016/06/', 'https://thegymter.net/2016/05/', 'https://thegymter.net/2016/04/', 'https://thegymter.net/2016/03/', 'https://thegymter.net/2016/02/', 'https://thegymter.net/2016/01/', 'https://thegymter.net/2015/12/', 'https://thegymter.net/2015/11/', 'https://thegymter.net/2015/10/', 'https://thegymter.net/2015/09/', 'https://thegymter.net/2015/08/', 'https://thegymter.net/2015/07/', 'https://thegymter.net/2015/06/', 'https://thegymter.net/2015/05/', 'https://thegymter.net/2015/04/', 'https://thegymter.net/2015/03/', 'https://thegymter.net/2015/02/', 'https://thegymter.net/2015/01/', 'https://thegymter.net/2014/12/', 'https://thegymter.net/2014/11/', 'https://thegymter.net/2014/10/', 'https://thegymter.net/2014/09/', 'https://thegymter.net/2014/08/', 'https://thegymter.net/2014/07/', 'https://thegymter.net/2014/06/', 'https://thegymter.net/2014/05/', 'https://thegymter.net/2014/04/', 'https://thegymter.net/2014/03/', 'https://thegymter.net/2014/02/', 'https://thegymter.net/2013/10/', 'https://thegymter.net/2013/04/', 'https://wordpress.com/?ref=footer_blog']]

firstGymnast = req.get(removedTopBottomLinks[0])

##print(firstGymnast.text)

## Parsing Table
tablesoup = BeautifulSoup(firstGymnast.text, 'lxml')

##table2 = soup.find('table')
data = []

tables = tablesoup.find_all('table')

for table in tables:
    ## print(table)
    ## print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

print(data)
##print(table2)























## db 
#authorization
gc = pygsheets.authorize(service_file='creds.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['Directionally Challenged Jumpy', 'Steve', 'Sarah']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('gymnastsDb')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))