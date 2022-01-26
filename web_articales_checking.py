from newspaper import Article






def Checking_articales():

    url = input("Enter The link: ")



    #Passing link into article libary
    my_article = Article (url)

    
    #download the articale from link.
    my_article.download()



    #setup article for reading.
    my_article.parse()


    text = my_article.text





    
    #Data storing in sentiment data base...
    data_for_sentiment = open("sentiment_database", "w", encoding="utf8")
    data_for_sentiment.write(str(text))




