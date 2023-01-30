import os
import numpy as np
import pandas as pd
import spacy




def createPoem(writer,word,verses):
    # load english model from spacy
    nlp = spacy.load('en_core_web_lg')
    initial_string = nlp(word)
    sentences = pd.read_csv(f"./Scraping/cleaned_sentences/{writer}.csv")
    size = sentences.shape[0]
    poem_id = ()
    poem = []
    for i in range(verses):
        random_sent_index = np.random.randint(0,size,size=10)
        sent_list = list(sentences.sentences.iloc[random_sent_index])
        # transform sentences into spacy doc object
        docs = nlp.pipe(sent_list)
        similarity_list = []
        for sent in docs:
            if(sent.vector_norm):
                similarity = initial_string.similarity(sent)
                similarity_list.append(similarity)
        # save similarity into a dataframe
        temp = pd.DataFrame({'similarity':similarity_list,'doc_id':sentences.corpus_id.iloc[random_sent_index]},index=random_sent_index)
        temp = temp[temp.doc_id != poem_id]
        # sort this similarity in descending order
        temp.sort_values(by="similarity",inplace = True, ascending=True)
        sent_index = temp.index[0]
        sent = sentences.sentences[sent_index]
        replace_dict = {'\n' :  '', '\r' :  ''}
        for x,y in replace_dict.items():
            sent = sent.replace(x, y)
        poem.append(sent)
        poem_id = temp.doc_id.iloc[0]
        initial_string = nlp(sent)
    
    return "\n".join(poem)
    
def main():
    files =[]
    for (dirpath, dirnames, filenames) in os.walk("./writers/"):
        files = filenames
        break
    
    i = 1
    for file in files:
        print(f"{i}. {file.split('.')[0]}")
        i +=1
    idx = int(input("select a writer from the Above, enter number:  "))
    word = input("Enter a word(as a theme) for which you wan't to generate poems")
    verses = int(input("Enter number of verses in your output poem: "))
    # getting writer's name
    writer= files[idx-1].split('.')[0]
    file = file[idx-1]
    poem = createPoem(file,writer,word,verses)
    print(poem)

def main2():
    word = input("Enter a word(as a theme) for which you wan't to generate poems:  ")
    verses = int(input("Enter number of verses in your output poem: "))
    files =[]
    for (dirpath, dirnames, filenames) in os.walk("./Scraping/writers/"):
        files = filenames
        break
    i = 1
    for file in files:
        print(f"\n\n{i}. {file.split('.')[0]}")
        writer= files[i-1].split('.')[0]
        #print(f"\n\nBy writer: {writer}")
        print(writer)
        poem = createPoem(writer,word,verses)
        print(poem)
        #print(30 * "__" )
        print("\n\n")
        i +=1
        
if __name__ == "__main__":
    #main()
    main2()