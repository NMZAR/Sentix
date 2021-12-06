from numpy import short
from numpy.core.fromnumeric import argsort
import spacy




polisher_nl_pipe = spacy.load("en_core_web_sm")

def Sentiment_analyser():



    userinput = input("What Sentiment do you want to know? : ")
    



    #user_input = input("Give me data: ")


    # def for_write():
    #     data_for_write = open("Database.txt", "w")
    #     data_for_write.write(user_input)
    # for_write()





    def for_read():
        data_for_read = open("Database.txt", "r")
        return data_for_read.read()
    for_read()



    def for_polish_data():
        polished_file = polisher_nl_pipe(for_read())
        return list(polished_file.sents) 
    for_polish_data()


    polished_sentence_list = for_polish_data()
    
    sentences_value_array = []
    sentences_value_array.clear()
    
    


    def Sentence_similarity_value_collect():     
        for sentence_value in polished_sentence_list:            
            each_polished_sentence_value = sentence_value.similarity(polisher_nl_pipe(userinput))
            sentences_value_array.append(each_polished_sentence_value)               
    Sentence_similarity_value_collect()   


    sorted_index_value =  argsort(sentences_value_array)
    print(sorted_index_value)


    #Storing Sentences in sorting Order.
   


    # #making Multi dimentional array   
    # Sentences_and_values_array = []
    # Sentences_and_values_array.clear()
    # def Storing_sentence_and_values(): 
    #     i = 0
    #     for Sentences_value in polished_sentence_list:
    #         Sentences_and_values_array.append([polished_sentence_list[i], sentences_value_array[i]])
    #         i = i + 1
        

    #     short_listed = sorted(Sentences_and_values_array)
    #     print(short_listed)
       
            
                
    # Storing_sentence_and_values()

        
        
  


    
  

Sentiment_analyser()