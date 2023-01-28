import csv
import sys,tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt



# twitter keys:
ConsumerApiKey='nWPooNIRBOQMn8SHGKgmFd6Wj'
ConsumerApiSecret='t7p4S4c4tKcViG6JOD1iIDCrrzJRtI10W8cgxkSbSzl4i0bu4u'
AccessApiTokenKey='1445681508690239494-gcoJqjx5r5S17Yied5QvjY2fIptcso'
AccessApiTokenSecret='t2ElVZ31yoV4Nq77Qz1xehePd5wwvNpUjWWDHBr7Xv9jF'

# Authentication and creating Api
auth=tweepy.OAuthHandler(ConsumerApiKey,ConsumerApiSecret)
auth.set_access_token(AccessApiTokenKey,AccessApiTokenSecret)
api=tweepy.API(auth)


def percentage(part,whole):
    return 100*(float(part)/float(whole))


def analysis(search_item , noOfSearchTerm):
    search_term=search_item
    noOfSearchTerm=int(noOfSearchTerm)

    tweets=tweepy.Cursor(api.search_tweets,q=search_term,lang="en").items(noOfSearchTerm)

    positive=0
    wpositive=0
    negative=0
    wnegative=0
    neutral=0
    polarity=0  #average result of all tweets
    subjectivity=0


    for tweet in tweets:
        # print(TextBlob(tweet.text))
        analysis=TextBlob(tweet.text)
        polarity+=analysis.sentiment.polarity
        subjectivity+=analysis.sentiment.subjectivity

        if analysis.sentiment.polarity==0:
            neutral=neutral+1
        elif analysis.sentiment.polarity>0 and analysis.sentiment.polarity<=0.5:
            wpositive=wpositive+1
        elif analysis.sentiment.polarity>0.5 and analysis.sentiment.polarity<=1:
            positive=positive+1
        elif analysis.sentiment.polarity>=-0.5 and analysis.sentiment.polarity<0:
            wnegative=wnegative+1
        elif analysis.sentiment.polarity>=-1 and analysis.sentiment.polarity<-0.5:
            negative=negative+1

    # Calculating Percentage
    positive=percentage(positive,noOfSearchTerm)
    wpositive=percentage(wpositive,noOfSearchTerm)
    negative=percentage(negative,noOfSearchTerm)
    wnegative=percentage(wnegative,noOfSearchTerm)
    neutral=percentage(neutral,noOfSearchTerm)

    positive=format(positive,'.2f')
    wpositive=format(wpositive,'.2f')
    negative=format(negative,'.2f')
    wnegative=format(wnegative,'.2f')
    neutral=format(neutral,'.2f')



    #data valuse
    
    print('How people are reacting on ',search_term,' by analysing ',str(noOfSearchTerm),' Tweets :')


    #result value
    val = ""

    polarity=polarity/noOfSearchTerm
    if (polarity==0):
        val = 'Neutral'
    elif (polarity>0 and polarity<=0.5):
        val = 'Weakly Positive'
    elif (polarity>0.5 and polarity<=1):
        val = 'Positive'
    elif (polarity>=-0.5 and polarity<0):
        val = 'Weakly Negative'
    elif (polarity>=-1 and polarity<-0.5):
        val = 'Negative'

    # Accuracy
    acc=format((100-(subjectivity/noOfSearchTerm)*100),'.2f')

    data = [wpositive,positive,wnegative,negative,neutral]
    label = ["Weakly Positive","Positive" , "Weakly Negative","Negative","Neutral"]


    full_data = {}
    full_data["data"] = data
    full_data["label"] = label
    full_data["val"] = val
    full_data["accuracy"] = acc

    return full_data

    

   
