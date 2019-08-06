## TODO find methods for getting all gymnasts that are not in the list like https://thegymter.net/konnor-mcclain/

## Imports
import re
import requests as req
from bs4 import BeautifulSoup

## Imports for google sheets API
import pygsheets
import pandas as pd

import numpy as np

## Gather links from gymternet
# active gymnasts
active_gymnasts = req.get("https://thegymter.net/gymnast-database/")
active_gymnasts_soup = BeautifulSoup(active_gymnasts.text, 'lxml')

# retired gymnasts 
retired_gymnasts = req.get("https://thegymter.net/retired-gymnast-database/")
retired_gymnasts_soup = BeautifulSoup(retired_gymnasts.text, 'lxml')

#print(retired_gymnasts.text)

links = []

# Add html href to links array using regex
#for active_link in active_gymnasts_soup.findAll('a', attrs={'href': re.compile("^http*s://")}):
#    links.append(active_link.get('href'))

#for retired_link in retired_gymnasts_soup.findAll('a', attrs={'href': re.compile("^http*s://")}):
#    links.append(retired_link.get('href'))

for active_link in active_gymnasts_soup.find_all('a', href=True):
    links.append(active_link.get('href'))

for retired_link in retired_gymnasts_soup.find_all('a', href=True):
    links.append(retired_link.get('href'))

#print(links)

## Remove top and bottom links
removedTopLinks = [x for x in links if x not in ['/gymnast-database/?replytocom=6958#respond', '/gymnast-database/?replytocom=6961#respond', '/gymnast-database/?replytocom=14352#respond', '/gymnast-database/?replytocom=9063#respond', '/gymnast-database/?replytocom=9068#respond', '/gymnast-database/?replytocom=14805#respond', '/gymnast-database/?replytocom=14806#respond', '/gymnast-database/?replytocom=17174#respond', '/gymnast-database/?replytocom=20968#respond', '/gymnast-database/?replytocom=20969#respond', '/gymnast-database/?replytocom=24445#respond', '/gymnast-database/?replytocom=24446#respond', '/gymnast-database/?replytocom=24448#respond', '/gymnast-database/?replytocom=30098#respond', '/gymnast-database/?replytocom=30100#respond', '/gymnast-database/?replytocom=30200#respond', 'http://lspatterson2016.wordpress.com', '/gymnast-database/?replytocom=45114#respond', '/gymnast-database/#respond', '#comment-form-guest', '#comment-form-load-service:WordPress.com', '#comment-form-load-service:Twitter', '#comment-form-load-service:Facebook', "javascript:HighlanderComments.doExternalLogout( 'wordpress' );", '#', "javascript:HighlanderComments.doExternalLogout( 'googleplus' );", '#', "javascript:HighlanderComments.doExternalLogout( 'twitter' );", '#', "javascript:HighlanderComments.doExternalLogout( 'facebook' );", '#', 'javascript:HighlanderComments.cancelExternalWindow();','#content','https://thegymter.net/retired-gymnast-database/','https://thegymter.net/', 'https://thegymter.net/', 'https://thegymter.net/', 'https://thegymter.net/meet-coverage/', 'https://thegymter.net/2019-gymnastics-calendar/', 'https://thegymter.net/2018-gymnastics-calendar/', 'https://thegymter.net/2017-gymnastics-calendar/', 'https://thegymter.net/2016-gymnastics-calendar/', 'https://thegymter.net/2015-gymnastics-calendar/', 'https://thegymter.net/2014-gymnastics-calendar/', 'https://thegymter.net/2013-gymnastics-calendar/', 'https://thegymter.net/features/', 'https://thegymter.net/category/breaking-news/', 'https://thegymter.net/whats-your-team/', 'https://thegymter.net/category/mag/', 'https://thegymter.net/category/ncaa/', 'https://thegymter.net/category/interviews/', 'https://thegymter.net/category/qa/', 'https://thegymter.net/category/meet-the-elite/', 'https://thegymter.net/category/on-our-minds/', 'https://thegymter.net/category/the-leo-panel/', 'https://thegymter.net/category/four-year-rewind/', 'https://thegymter.net/category/in-translation/', 'https://thegymter.net/category/fun-games/', 'https://thegymter.net/gymnast-database/', 'https://thegymter.net/category/the-research-files/', 'https://thegymter.net/2020-womens-olympic-qualifiers/', 'https://thegymter.net/2020-womens-olympic-qualifiers/', 'https://thegymter.net/2020-mens-olympic-qualifiers/', 'https://thegymter.net/2018-2020-apparatus-world-cup-rankings/', 'https://thegymter.net/2018-2020-apparatus-world-cup-mens-rankings/', 'https://thegymter.net/the-best-scores-in-2019/', 'https://thegymter.net/the-best-scores-in-2019/', 'https://thegymter.net/the-best-mens-scores-in-2019/', 'https://thegymter.net/about/', 'https://thegymter.net/contribute/']]
removedTopBottomLinks = [y for y in removedTopLinks if y not in ['https://thegymter.net/gymnast-database/?share=twitter', 'https://thegymter.net/gymnast-database/?share=facebook', 'https://thegymter.net/2014/12/24/happy-holidays-from-the-gymternet/', 'https://thegymter.net/gymnast-database/#comment-6958', 'https://thegymter.net/gymnast-database/?like_comment=6958&_wpnonce=84cd555441', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-6961', 'https://thegymter.net/gymnast-database/?like_comment=6961&_wpnonce=76ecb655b2', 'https://thegymter.net/gymnast-database/#comment-14352', 'https://thegymter.net/gymnast-database/?like_comment=14352&_wpnonce=016825513a', 'https://thegymter.net/gymnast-database/#comment-9063', 'https://thegymter.net/gymnast-database/?like_comment=9063&_wpnonce=120c72e9b0', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-9068', 'https://thegymter.net/gymnast-database/?like_comment=9068&_wpnonce=cccea55bc8', 'https://thegymter.net/2016/04/02/helena-bonilla/', 'https://thegymter.net/gymnast-database/#comment-14805', 'https://thegymter.net/gymnast-database/?like_comment=14805&_wpnonce=6e09a2f298', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-14806', 'https://thegymter.net/gymnast-database/?like_comment=14806&_wpnonce=f81d3bc70b', 'https://thegymter.net/gymnast-database/#comment-17174', 'https://thegymter.net/gymnast-database/?like_comment=17174&_wpnonce=a0633e5c70', 'https://thegymter.net/2016/11/03/the-best-world-finishes-of-all-time/', 'https://thegymter.net/gymnast-database/#comment-20968', 'https://thegymter.net/gymnast-database/?like_comment=20968&_wpnonce=5a74dffc1f', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-20969', 'https://thegymter.net/gymnast-database/?like_comment=20969&_wpnonce=ccaedda2ec', 'https://thegymter.net/gymnast-database/#comment-24445', 'https://thegymter.net/gymnast-database/?like_comment=24445&_wpnonce=be94911552', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-24446', 'https://thegymter.net/gymnast-database/?like_comment=24446&_wpnonce=2a76cc484f', 'https://thegymter.net/gymnast-database/#comment-24448', 'https://thegymter.net/gymnast-database/?like_comment=24448&_wpnonce=a74a0e2f33', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-24450', 'https://thegymter.net/gymnast-database/?like_comment=24450&_wpnonce=6fb6bda0bc', 'https://thegymter.net/gymnast-database/#comment-30098', 'https://thegymter.net/gymnast-database/?like_comment=30098&_wpnonce=175fa623b2', 'https://thegymter.wordpress.com', 'https://thegymter.net/gymnast-database/#comment-30100', 'https://thegymter.net/gymnast-database/?like_comment=30100&_wpnonce=22d34fc256', 'https://thegymter.net/gymnast-database/#comment-30200', 'https://thegymter.net/gymnast-database/?like_comment=30200&_wpnonce=2c1e255066', 'https://thegymter.net/gymnast-database/#comment-45114', 'https://thegymter.net/gymnast-database/?like_comment=45114&_wpnonce=01e2612351', 'https://gravatar.com/site/signup/', 'https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=lch3153%40gmail%2ecom&lc=US&item_name=The%20Gymternet&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted', 'https://thegymter.net/2019/08/03/2019-german-championships-results/', 'https://thegymter.net/2019/08/03/2019-pan-american-games-results/', 'https://thegymter.net/2019/07/31/2019-pan-american-games-live-blog-event-finals-day-2/', 'https://thegymter.net/2019/07/30/2019-pan-american-games-live-blog-event-finals-day-1/', 'https://thegymter.net/2019/07/29/2019-pan-american-games-live-blog-mens-all-around-final/', 'https://thegymter.net/2019/07/29/2019-pan-american-games-live-blog-womens-all-around-final/', 'https://thegymter.net/2019/07/29/around-the-gymternet-never-tell-me-the-odds/', 'https://thegymter.net/2019/07/28/2019-pan-american-games-live-blog-mens-qualifications-subdivision-2/', 'https://thegymter.net/2019/07/28/2019-pan-american-games-live-blog-mens-qualifications-subdivision-1/', 'https://thegymter.net/2019/07/27/2019-pan-american-games-live-blog-womens-qualifications-subdivision-3/', 'https://www.facebook.com/thegymternet', 'https://thegymter.net/2019/08/', 'https://thegymter.net/2019/07/', 'https://thegymter.net/2019/06/', 'https://thegymter.net/2019/05/', 'https://thegymter.net/2019/04/', 'https://thegymter.net/2019/03/', 'https://thegymter.net/2019/02/', 'https://thegymter.net/2019/01/', 'https://thegymter.net/2018/12/', 'https://thegymter.net/2018/11/', 'https://thegymter.net/2018/10/', 'https://thegymter.net/2018/09/', 'https://thegymter.net/2018/08/', 'https://thegymter.net/2018/07/', 'https://thegymter.net/2018/06/', 'https://thegymter.net/2018/05/', 'https://thegymter.net/2018/04/', 'https://thegymter.net/2018/03/', 'https://thegymter.net/2018/02/', 'https://thegymter.net/2018/01/', 'https://thegymter.net/2017/12/', 'https://thegymter.net/2017/11/', 'https://thegymter.net/2017/10/', 'https://thegymter.net/2017/09/', 'https://thegymter.net/2017/08/', 'https://thegymter.net/2017/07/', 'https://thegymter.net/2017/06/', 'https://thegymter.net/2017/05/', 'https://thegymter.net/2017/04/', 'https://thegymter.net/2017/03/', 'https://thegymter.net/2017/02/', 'https://thegymter.net/2017/01/', 'https://thegymter.net/2016/12/', 'https://thegymter.net/2016/11/', 'https://thegymter.net/2016/10/', 'https://thegymter.net/2016/09/', 'https://thegymter.net/2016/08/', 'https://thegymter.net/2016/07/', 'https://thegymter.net/2016/06/', 'https://thegymter.net/2016/05/', 'https://thegymter.net/2016/04/', 'https://thegymter.net/2016/03/', 'https://thegymter.net/2016/02/', 'https://thegymter.net/2016/01/', 'https://thegymter.net/2015/12/', 'https://thegymter.net/2015/11/', 'https://thegymter.net/2015/10/', 'https://thegymter.net/2015/09/', 'https://thegymter.net/2015/08/', 'https://thegymter.net/2015/07/', 'https://thegymter.net/2015/06/', 'https://thegymter.net/2015/05/', 'https://thegymter.net/2015/04/', 'https://thegymter.net/2015/03/', 'https://thegymter.net/2015/02/', 'https://thegymter.net/2015/01/', 'https://thegymter.net/2014/12/', 'https://thegymter.net/2014/11/', 'https://thegymter.net/2014/10/', 'https://thegymter.net/2014/09/', 'https://thegymter.net/2014/08/', 'https://thegymter.net/2014/07/', 'https://thegymter.net/2014/06/', 'https://thegymter.net/2014/05/', 'https://thegymter.net/2014/04/', 'https://thegymter.net/2014/03/', 'https://thegymter.net/2014/02/', 'https://thegymter.net/2013/10/', 'https://thegymter.net/2013/04/', 'https://wordpress.com/?ref=footer_blog','https://thegymter.net/gymnast-database/?like_comment=6958&_wpnonce=e3d73c3856', 'https://thegymter.net/gymnast-database/?like_comment=6961&_wpnonce=14ff128907', 'https://thegymter.net/gymnast-database/?like_comment=14352&_wpnonce=2c45e5bdff', 'https://thegymter.net/gymnast-database/?like_comment=9063&_wpnonce=fd1ee97d2c', 'https://thegymter.net/gymnast-database/?like_comment=9068&_wpnonce=effcb96406', 'https://thegymter.net/gymnast-database/?like_comment=14805&_wpnonce=1b63ab64b8', 'https://thegymter.net/gymnast-database/?like_comment=14806&_wpnonce=431835c522', 'https://thegymter.net/gymnast-database/?like_comment=17174&_wpnonce=7a18322062', 'https://thegymter.net/gymnast-database/?like_comment=20968&_wpnonce=2b318c876f', 'https://thegymter.net/gymnast-database/?like_comment=20969&_wpnonce=3fe32fc666', 'https://thegymter.net/gymnast-database/?like_comment=24445&_wpnonce=49af5c7b68', 'https://thegymter.net/gymnast-database/?like_comment=24446&_wpnonce=655838a53b', 'https://thegymter.net/gymnast-database/?like_comment=24448&_wpnonce=4ad7057ea2', 'https://thegymter.net/gymnast-database/?like_comment=24450&_wpnonce=3e43a56082', 'https://thegymter.net/gymnast-database/?like_comment=30098&_wpnonce=d4937eb157', 'https://thegymter.net/gymnast-database/?like_comment=30100&_wpnonce=72ec1c9e16', 'https://thegymter.net/gymnast-database/?like_comment=30200&_wpnonce=ced4f857e6', 'https://thegymter.net/gymnast-database/?like_comment=45114&_wpnonce=a89289fae2', 'https://thegymter.net/2019/08/05/around-the-gymternet-im-nauseous/', 'https://thegymter.net/2019/08/04/2019-european-youth-olympic-festival-results/', 'https://thegymter.net/2019/08/03/2019-pan-american-games-mens-results/', 'https://thegymter.net/retired-gymnast-database/?share=twitter', 'https://thegymter.net/retired-gymnast-database/?share=facebook']]
print(removedTopBottomLinks)
#print(len(removedTopBottomLinks))
#firstGymnast = req.get(removedTopBottomLinks[0])

##print(firstGymnast.text)

## Parsing Table
#tablesoup = BeautifulSoup(firstGymnast.text, 'lxml')

##table2 = soup.find('table')


## all tables

# tables = tablesoup.find_all('table')
# data = []
# for table in tables:
#     ## print(table)
#     ## print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#     rows = table.find_all('tr')
#     for row in rows:
#         cols = row.find_all('td')
#         cols = [ele.text.strip() for ele in cols]
#         data.append([ele for ele in cols if ele])




updategymnasttable = False
if(updategymnasttable):
# Parse Gymnasts Table
    datatable = []
    count = 0

    # Loop through link array
    for gymnastlink in removedTopBottomLinks:
        print(gymnastlink + "   " + str(count))
        count+=1

        # Get webpage for each gymnast
        Gymnast = req.get(gymnastlink)

        # Make webpage into html
        tablesoup = BeautifulSoup(Gymnast.text, 'lxml')
        # Find the first table 
        table = tablesoup.find('table')
        # Find all the rows inside of the table
        rows = table.find_all('tr')

        data =[]

        # Loop through the rows in the table 
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append(cols[1])
            print(data)
        datatable.append(data)
        cols = []
        data = []

    print(datatable)























## db 
#authorization
gc = pygsheets.authorize(service_file='creds.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a table with datatable and column names 
df = pd.DataFrame(np.array(datatable),
                    columns=['Full Name', 'Nation', 'DOB', 'Status'])
print(df)


#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('gymnastsDb')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))