import wikipedia




array = []


'''
searching all Related topic in wikipidia.
'''
result = wikipedia.search("trump")


for search in result:
    print(wikipedia.page(search).summary); 

    array.append(wikipedia.page(search).summary)




    

