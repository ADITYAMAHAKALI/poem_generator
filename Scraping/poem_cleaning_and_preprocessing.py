import os
import pandas as pd
import numpy as np

'''
    The objective of this programme is to extract sentences out of the poems
    and remove unwanted characters with more sensible ones so that final 
    output poems look more human written rather than machine generated
'''
# the following replace dictionary has been obtained by observing the 
# irregularities in the scraped data
replace_dict = {
    '?>>':'<<',
    '(' : '',
    ')' : '',
    ':' : ',', 
    ',,,' : ',',
    '---':' ',
    '--':' ',
    '\r':''
   
}
def preProcess(file):
    poems = pd.read_csv(file)
    number_poems = poems.shape[0]
    poem_sentences = pd.DataFrame(columns=['corpus_id','sentences'])
    for i in range(number_poems):
        text = poems.text[i]
        for x,y in replace_dict.items():
            text = text.replace(x, y)
        text = ''.join([i for i in text if not i.isdigit()])
        text = text.lower()
        sentences = text.split("\n")
        corpus_id = [i] * len(sentences)
        # Saving Sentences and poem ID
        df_sentences= pd.DataFrame({'corpus_id':corpus_id,'sentences':sentences})
        
        poem_sentences = pd.concat([poem_sentences,df_sentences])
    poem_sentences = poem_sentences[poem_sentences.sentences != '']
    poem_sentences.reset_index(drop=True, inplace=True)  
    #saves clean sentences to a .csv file 
    return poem_sentences


def main():
    files =[]
    for (dirpath, dirnames, filenames) in os.walk("./writers/"):
        files = filenames
        break
    for file in files:
        df = preProcess("./writers/" + file)
        df.to_csv("cleaned_sentences/" + file)
    
if __name__ == '__main__':
    main()