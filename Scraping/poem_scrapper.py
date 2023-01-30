import requests
from bs4 import BeautifulSoup
import pandas as pd

def createCorpus(results):
    titles =[]
    corpus = []
    for page in results:
        url = requests.get(page)
        soup = BeautifulSoup(url.content,'html.parser')
        title = soup.find(class_ = "title-poem")
        titles.append(title.get_text())
        poem = soup.find(class_ = "poem-entry")
        corpus.append(poem.find('p').get_text())
        print(poem)
    poems = pd.DataFrame({'title':titles,'text':corpus})
    print(poems)
    return poems

def main():  
    prefix = "https://mypoeticside.com/poets/"
    writer = input("Enter a writer's name e.g. rabindranath-tagore:  ")
    suffix = "-poems"
    header = {'User-Agent': "Safari/18614.2.9.1.12"}
    url = requests.get(prefix+writer+suffix,headers=header)
    soup = BeautifulSoup(url.content,'html.parser')
    # first get list of all poems for that author
    poem_list = soup.find(class_="list-poems")
    #find links
    links = poem_list.findAll('a')
    # create page links for the poems
    results = ["https:"+link.get('href') for link in links]
    poems = createCorpus(results)
    poems.to_csv("writers/"+writer+".csv")

if __name__ == "__main__":
    main()
