from numpy.core.fromnumeric import argsort, sort
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
    index_value_of_sorted_array = []
    index_value_of_sorted_array.clear()
    
    ##############################################################################################    
    '''
    bugs: Need to fix (gatter than 0.2000) storing values....
    bugs: sentences Need capitalize...
    bugs: user input capitalize...
    '''
    ##############################################################################################

    def Sentence_similarity_value_collect():     
        for sentence_value in polished_sentence_list:            
            each_polished_sentence_value = sentence_value.similarity(polisher_nl_pipe(userinput))
            sentences_value_array.append(each_polished_sentence_value)               
    Sentence_similarity_value_collect()   






#Collecting index value of sorted array and biggest value holded sentence index number.
    index_value_of_sorted_array = argsort(sentences_value_array)
    sentences_size_no = (len(index_value_of_sorted_array) - 1)
    

    Serialised_sentences_array = []
    Serialised_sentences_array.clear()
    #Sorting sentences bigger to smaller value....
    for sentences in polished_sentence_list:
        Serialised_sentences_array.append((polished_sentence_list[index_value_of_sorted_array[sentences_size_no]]))
        sentences_size_no = sentences_size_no - 1    

        
    



    #Storing User Review in a order.
    user_review_array = []
    user_review_array.clear()
    range_user_review_input = int (input("How Many sentiments of Human do you want to check? : " ))
    count = 0
######################################################################

    while count < range_user_review_input:
        user_review_array.append(Serialised_sentences_array[count])
        count = count + 1

######################################################################
#Data storing in sentiment data base...
    data_for_sentiment = open("sentiment_database", "w")
    data_for_sentiment.write(str(user_review_array))
        


    # #Storing Sentences in sorted Order.
    # sorted_Sentence = []
    # sorted_Sentence.clear()


    # def multidimention_array ():
    #     i = 0
    #     x = 0
    #     array_index_no_in_sort = []
    #     array_index_no_in_sort.clear()

    #     for sentences in polished_sentence_list:
    #         array_index_no_in_sort.append(sorted_index_value[i])
    #         i = i + 1

    #     for sentences in polished_sentence_list:
    #         array_index_number_for_sentences =  array_index_no_in_sort[x]
    #         sorted_Sentence.append(polished_sentence_list[array_index_number_for_sentences])
    #         x = x + 1
    #     print(polished_sentence_list)
   
    

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


