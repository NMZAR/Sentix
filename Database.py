
import spacy



NLP = spacy.load("en_core_web_sm")





def Sentiment_analyser():

    


    # def for_write():
    #         data_for_write = open("Database.txt", "w")
    #         data_for_write.write(user_input_given_data)
    # for_write()


    


###############################################################
    '''
    Reading Data From data base text file.
    '''
    def for_read():
        text = open("Database.txt", "r",  encoding="utf8")
        return text.read()     
    for_read()





#################################################################


    

    ########################################################################################
    '''
    Polish Data By NLP From data_for_read File and making senteces list...
    '''
    doc = NLP(for_read())
 
    '''
    Listing Sentences.
    '''
    sentence_list= list(doc.sents)






    return sentence_list;



    # store = sentence_list[1]

    # for token in store:
    #     print(token.text); 


    


    ##for sentences in polished_sentence_list:
        ##print(token.)

    



   #########################################################################################
















    
#     sentences_value_array = []
#     sentences_value_array.clear()
#     index_value_of_sorted_array = []
#     index_value_of_sorted_array.clear()
    
    
#     ##############################################################################################    
#     '''
#     bugs: Need to fix (gatter than 0.2000) storing values....
#     bugs: sentences Need capitalize...
#     bugs: user input capitalize...
#     Bugs: can't read more than 2 file....
#     '''
#     ##############################################################################################





# #####################################################################################################
#     '''
#     Collecting Senteces Values....
#     '''
#     def Sentence_similarity_value_collect():     
#         for sentence_value in polished_sentence_list:            
#             each_polished_sentence_value = sentence_value.similarity(polisher_nl_pipe(userinput))
#             sentences_value_array.append(each_polished_sentence_value)               
#     Sentence_similarity_value_collect()   

# ######################################################################################################

  
    





# #Collecting index value of sorted array and biggest value holded sentence index number.
#     index_value_of_sorted_array = argsort(sentences_value_array)
#     sorted_senteces_value_array = sorted(sentences_value_array)
    
#     sentences_size_no = (len(index_value_of_sorted_array) - 1)

    
    
  
    
    
#     # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#     #print(index_value_of_sorted_array) ### index value of sorted array
#     #print(index_value_of_sorted_array[sentences_size_no])
#     # print(sorted_senteces_value_array) ### shorted values of senteces.
#     # print("<<<<<<<<<<<<<<<<<<<<<<<<<")
#     #print(sentences_value_array[index_value_of_sorted_array[sentences_size_no]]) #sentences most bigger values
#     # print("----------------------")
#     #print(polished_sentence_list[index_value_of_sorted_array[sentences_size_no]])#most similar senteces
#     #the most powerful women  .........Sheikh Hasina worked with Khaleda Zia
    

#     '''
#     Fetures:  Later will be add accuracy good. better. best

#     '''


#     Serialised_sentences_array = []
#     Serialised_sentences_array.clear()
#     #Sorting sentences bigger to smaller value...
#     while 0.35 < sorted_senteces_value_array[sentences_size_no]:
        
#         Serialised_sentences_array.append((polished_sentence_list[index_value_of_sorted_array[sentences_size_no]]))
#         sentences_size_no = sentences_size_no - 1


   

#     print(Serialised_sentences_array)
#     print("+++++++++++++")




# # # ######################################################################

# #Data storing in sentiment data base...
#     data_for_sentiment = open("sentiment_database", "w", encoding="utf8")
#     data_for_sentiment.write(str(Serialised_sentences_array))


# # ######################################################################




#     # #Storing Sentences in sorted Order.
#     # sorted_Sentence = []
#     # sorted_Sentence.clear()


#     # def multidimention_array ():
#     #     i = 0
#     #     x = 0
#     #     array_index_no_in_sort = []
#     #     array_index_no_in_sort.clear()

#     #     for sentences in polished_sentence_list:
#     #         array_index_no_in_sort.append(sorted_index_value[i])
#     #         i = i + 1

#     #     for sentences in polished_sentence_list:
#     #         array_index_number_for_sentences =  array_index_no_in_sort[x]
#     #         sorted_Sentence.append(polished_sentence_list[array_index_number_for_sentences])
#     #         x = x + 1
#     #     print(polished_sentence_list)
   
    

#     # #making Multi dimentional array   
#     # Sentences_and_values_array = []
#     # Sentences_and_values_array.clear()
#     # def Storing_sentence_and_values(): 
#     #     i = 0
#     #     for Sentences_value in polished_sentence_list:
#     #         Sentences_and_values_array.append([polished_sentence_list[i], sentences_value_array[i]])
#     #         i = i + 1
        

#     #     short_listed = sorted(Sentences_and_values_array)
#     #     print(short_listed)
       
            
                
#     # Storing_sentence_and_values()
