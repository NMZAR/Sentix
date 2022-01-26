from numpy import negative, positive, equal
import Manually_checking
import web_articales_checking
from textblob import TextBlob 
import matplotlib.pyplot as plt




    
# def start():


#         user_input_for_wish = input('do you want to know sentiment of this room y/n: ' )

#         if user_input_for_wish == 'y':
#                 print("reconizing voice")
# ##################################################################################

#         else:
#                 Database.Sentiment_analyser()
# start()
# 
#  




Manually_checking.Manually_checking_Function()

#web_articales_checking.Checking_articales()





positive = 0
negative = 0
equal = 0
##############################################################################################    
'''
bugs: Need to fix (gatter than 0.2000) storing values....
bugs: sentences Need capitalize...
bugs: user input capitalize...
'''
'''
feature: display...

'''
##############################################################################################
sentences = open("sentiment_database", "r", encoding="utf8")
analysing_file =  sentences.read()



analysis = TextBlob(analysing_file)

print(analysing_file);

#####################################################################################



if analysis.sentiment.polarity < 0:
       
        negative = - (analysis.sentiment.polarity) 
        positive = 1 - negative
    
        

if analysis.sentiment.polarity >0: 
        
        positive = analysis.sentiment.polarity


else:
        
        equal = 0.1



###################################################################################


def function_for_pie_chart(negative,positive,equal):

    if analysis.sentiment.polarity !=0:

        labels = ['Negative', 'Positve']
        values = [negative, positive]
        plt.style.use('ggplot')
        plt.title("Overall Sentiments")
        plt.pie( x=values, labels=labels, autopct= '%.2f%%', shadow= True, startangle=220)
        plt.legend(loc = 'best')
        plt.show()

    else:
        print(equal)
        labels = ['Neutral']
        values = [equal]
        plt.title("Overall Sentiments")
        plt.pie( x=values, labels=labels, autopct= '%.2f%%')
        plt.show()


function_for_pie_chart(negative,positive,equal)
