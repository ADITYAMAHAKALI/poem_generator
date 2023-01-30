from flask import Flask,render_template,url_for,request
from poem_generator import createPoem
# for nlp
import os
import numpy as np
import pandas as pd
import spacy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            if request.form['submit_button'] == "Generate Poem" :
                theme = request.form["theme"]
                verses = int(request.form["verses"])
                files =[]
                texts = []
                writers =[]
                poems = {}
                for (dirpath, dirnames, filenames) in os.walk("./Scraping/writers/"):
                    files = filenames
                    break
                i = 1
                for file in files:
                    writer= files[i-1].split('.')[0]
                    writers.append(writer)
                    text = createPoem(writer,theme,verses)
                    texts.append(text)
                    i +=1
                poems = zip(writers,texts)
            return render_template("home.html",poems=poems,theme=theme)
        except Exception as e:
            return render_template("home.html",poems=[])
    else:
        return render_template("home.html",poems=[])
    
if __name__ =="__main__":
    app.run()
