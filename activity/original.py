def uncommon_from_sentences(s1, s2):
    #take result as diction to store
    s1_words = s1.split(" ")
    s2_words = s2.split(" ")
    
    # print(s1)
    
    words_dict = {}
    uncommon_list = []
    
    for word in s1_words:
        if word not in s2:
            words_dict[word] = 1
            
    for word in s2_words:
        if word not in s1:
            words_dict[word] = 1
            
    for word in words_dict:
        uncommon_list.append(word)
            
    return uncommon_list
            

print(uncommon_from_sentences("this apple is sweet", "this apple is sour" ))