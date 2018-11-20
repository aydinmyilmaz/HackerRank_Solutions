
# coding: utf-8

# In[2]:


text = "enging"
prefixstring = "ravengi"
suffixstring = "gingko"

#text score= prefix score + suffix score


def sublist(word):
    word_sublist= []
    for idx,item in enumerate(word):
        for i in range(idx+1,len(word)+1):
            word_sublist.append(word[idx:i])
    return word_sublist


text_sublist = sublist(text)
prefixstring_sublist = sublist(prefixstring)
suffixstring_sublist = sublist(suffixstring)

prefix_score=0
for item in text_sublist:
    if item in prefixstring_sublist[::-1] and prefix_score< len(item):
        prefix_score = len(item)
            
suffix_score=0
for item in text_sublist:
    if item in suffixstring_sublist and suffix_score< len(item):
        suffix_score = len(item)
        
text_score = prefix_score + suffix_score
print ("text score =",text_score, text[0:text_score] )       

