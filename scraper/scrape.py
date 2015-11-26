# encoding=utf-8
import tweepy, warnings, json, time, io
import datetime
from tweepy import OAuthHandler

#declaring constants
MAX_TWEETS = 50 #tweets per day per language(as in langs)


#reading settings from file
#note: keys.cfg must be is assumed to be in the same dir as __file__
json_data=open("keys.cfg").read()
data = json.loads(json_data)

consumer_key = data['consumer_key'] 
consumer_secret = data['consumer_secret']
access_token = data['access_token']
access_secret= data['access_secret']
lang = data['lang']

oAuth = OAuthHandler(consumer_key,consumer_secret)
oAuth.set_access_token(access_token,access_secret)
api = tweepy.API(oAuth)

trends = api.trends_place(1)[0]
queries = [ x['name'].encode('utf8') for x in trends['trends']]

mlist = []
for query in queries:
    searched_tweets = [status._json for status in tweepy.Cursor(api.search, q=query,lang=lang).items(MAX_TWEETS)]
    """
    for i in searched_tweets:
        a = {}
        a["id"] = i.id

        a["lang"] = i.lang  
        
        if lang == 'en':
            a["text_en"],a["text_de"],a["text_ru"] = i.text,"",""
        elif lang == 'de':
            a["text_de"],a["text_en"],a["text_ru"] = i.text,"",""
        else:
            a["text_ru"],a["text_en"],a["text_de"] = i.text,"",""        
        
        fmt = '%Y-%m-%dT%H:%M:%S000Z'
        temp = datetime.datetime.strptime(str(i.created_at),'%Y-%m-%d %H:%M:%S')
        a["created_at"] = temp.strftime(fmt)   
            
        a["tweet_hashtags"] = [tags["text"] for tags in i.entities["hashtags"]]
        a["tweet_urls"] = [obj["expanded_url"] for obj in [tags for tags in i.entities["urls"]]]
        mlist.append(a)               
    print len(mlist)        
    """
with io.open(time.strftime("%d_%m_%Y") + '.json','w',encoding='utf-8')  as output:
    output.write(unicode(json.dumps(searched_tweets, ensure_ascii=False, encoding='utf8')))
