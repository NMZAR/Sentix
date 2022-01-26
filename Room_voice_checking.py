import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("listening this room :")


    
    audio = r.listen(source, timeout=60)
    


    
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))

        
    
        #Data storing in sentiment data base...
        data_for_sentiment = open("sentiment_database", "w", encoding="utf8")
        data_for_sentiment.write(str(text))


        


    except:
        print("Sorry could not recognize what you said")





        '''
        later we can recognaize in a duration.
        '''



