
from string import capwords
import Database



similar_sentences_array = []



'''
calling senteces list from database.
'''
sentence_list = Database.Sentiment_analyser();





def Manually_checking_Function():


    '''
    user word box that user want to check.
    '''
    userinput = input("What Sentiment do you want to know? : ")

    """
    Sentences Array that are similar with word....
    """
    


    '''
    looping for each senteneces.
    '''
    for sentence in sentence_list:
       
            '''
            looping for each Sentences token.
            '''
            for token in sentence:
                '''
                checking word now
                '''

                ###Capitalization.....
                Capitalize_token = capwords(token.text)


            
                '''
                checking user word is available in sentences or not.
                '''
                if (Capitalize_token == capwords(userinput)):
                    similar_sentences_array.append(sentence);


    '''
    giving return to the function similar sentences.
    '''



    #Data storing in sentiment data base...
    data_for_sentiment = open("sentiment_database", "w", encoding="utf8")
    data_for_sentiment.write(str(similar_sentences_array))


    


                






'''
later we can search by simalar word.
'''

'''
Later we can search more than one word together.
'''


                