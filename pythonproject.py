import requests
from bs4 import BeautifulSoup
import pandas as pd
from numpy import random

print("welcome in web screaping poject")
content = requests.get("https://www.dawn.com/")
data = BeautifulSoup(content.content, 'lxml')
extract = data.find(class_='js-nav-items')
allitems = []
allmydata=[]
for items in extract.find_all('a'):
    mydata = items.getText()
    allitems.append(mydata)
show = pd.DataFrame(allitems)
print(show)


def function_latest_news(url):
    latest = requests.get(url)
    data3 = BeautifulSoup(latest.text, 'lxml')
    latestnew = data3.find_all(class_='story')
    for latestnews in latestnew:
        #print(latestnews)
        #image and alt text fetcing
        try:
            image=latestnews.find('img')
            images=image['src']
            alt=image['alt']
            #print('image',images)
            #print('Image alternative Text',alt)
        except Exception:
            images="image not found"
            #print('image not found')
        #main all detail fetching-------------------------------------
        try:
            heading = latestnews.find(class_='story__title')
            title = heading.text.strip()
           # print('Heading',heading.text.strip())
        except Exception:
            title = "That field is empty"
            #print(title)
            
            #link tag and links fetching and main content fetching
            
        try:
            links=latestnews.find('a')
            link=links.get('href')
            detail_content = requests.get(link)
            d_content=BeautifulSoup(detail_content.content,"lxml")
            finds=d_content.find('article')
            story=finds.find(class_='story__content')
            for storys in story.find_all('p'):    
                maincontent=story.find('p').text.strip()
                #print('our main content is ',maincontent)
            mycontent=maincontent
            #print('link ',mycontent)
            
        except Exception:
            link="this field is empty"
            #print('link  ',link)
            #story title fetching
        try:
            storytitle = latestnews.find(class_='story__title')
            storytitle1 = storytitle.text.strip()
            #print('Story Title',storytitle1)
        except Exception:
            storytitle1 = "That field is empty"
            #print(storytitle1)    
            #timestamp fetching----------------------------------------
        try:
            status = latestnews.find(class_='timestamp--label')
            status1 = status.text.strip()
            #print('status1',status1)
        except Exception:
            status1 = "That field is empty"
            #print('Status' ,status1)
            #timeupload fetching---------------------------------------------
        try:
            timeupload = latestnews.find(class_='timestamp--time')
            timeupload1 = timeupload.text.strip()
            #print('TIMEUPLOAD',timeupload1)
        except Exception:
            timeupload1 = "That field is empty"
            #print('Upload Time',timeupload1)
            
            #timestamp calender fetching------------------------------------

        try:
            timecalender = latestnews.find(class_='timestamp__calendar')
            timecalendar1 = timecalender.text.strip()
            #print('Time Calendar',timecalendar1)
        except Exception:
            timecalendar1 = "That field is empty"
            #print('Calendar Time', timecalendar1)

    #store data in dictory
        mydict={
            'iamge_link':images,
            'image_alt':alt,
            'title':'title',
            'heading_link':link,
            'main_content':maincontent,
            'article_title':storytitle1,
            'article_status':status1,
            'article_uploaded':timeupload1,
            'article_calendar':timecalendar1,
            'hahhhaha':'welcome in my world'
         }
        #print('dictionary',mydict)
        allmydata.append(mydict)
        print('Data will be processinggg------------please wait')
       
    data=pd.DataFrame(allmydata)
    print(data)
    print('If you want to save data in csv format file if yes enter 1 otherwise  0  ')
    csvinput=int(input('Enter 1 or 0 to perform operation'))
    if(csvinput==1):
        random_no=random.randint(900)4
        file_name=f"first2{random_no}.csv"
        file = data.to_csv(file_name, index=False, encoding='utf-8')
        print('Data Saved Successfully',file)
    else:
        print('Successfulyy exit')

       
 #-------------------------for testing purpose data -------------------------------------------
 # myrecords.append({'title':title,'storytitle':storytitle1,'status':status1,'timeupload':timeupload1,
            # 'timecalender':timecalendar1})
      #  myrecords.append({title, storytitle1, status1,
                        # timeupload1, timecalendar1})
        # myrecords.append(title)
        # myrecords.append(storytitle1)
        # myrecords.append(status1)
        # myrecords.append(timeupload1)
        #for onedict in allmydata:
     #   print('--------',onedict)
    #print('latest news information in that function', url)
    #print(myrecords)
    #for record in myrecords:
     #   print(record,'------------------------------')
    #data = pd.DataFrame(myrecords, columns=[
     #                   'Title', 'Status', 'Time', 'Upload'])
    #print(data.head())
    #csv = int(
     #   input('Are You Store Data in Csv File if Yes then Enter 1 otherwise 0'))
    #if(csv == 1):
     #   file = data.to_csv('first.csv', index=False, encoding='utf-8')
      #  print('data is stored', file)
    #else:
     #   print('Successfully Exit')
    #print(csv)
    #print(allitems)
        # myrecords.append(timecalendar1)columns=['hello','new','wel','never','a','b','c','d','e','da']
        #print('--------------------------------------------------')


select = int(input('Kindly Select a Catagory to ANALYSE the Data'))
if(select == 1):
    function_latest_news("https://www.dawn.com/")
elif(select == 2):

    function_latest_news("https://www.dawn.com/latest-news")
elif(select == 3):

    function_latest_news("https://www.dawn.com/trends/coronavirus")
elif(select == 4):

    function_latest_news("https://www.dawn.com/pakistan")
elif(select == 5):

    function_latest_news("https://www.dawn.com/business")
elif(select == 7):

    function_latest_news("https://www.dawn.com/opinion")
elif(select == 8):

    function_latest_news("https://images.dawn.com/")
elif(select == 9):

    function_latest_news("https://www.dawn.com/sport")
elif(select == 10):

    function_latest_news("https://www.dawn.com/magazines")
elif(select == 11):

    function_latest_news("https://www.dawn.com/world")
elif(select == 12):

    function_latest_news("https://www.dawn.com/tech")
elif(select == 13):

    function_latest_news("https://www.dawn.com/prism")
elif(select == 14):

    function_latest_news("https://www.dawn.com/popular")
elif(select == 15):
    function_latest_news("https://www.dawn.com/multimedia")