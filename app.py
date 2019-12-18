import flask
from TapSearch import TapSearch
ts = TapSearch()
app= flask.Flask(__name__)
@app.route('/',methods=['GET','POST'])
def first():
    "First Page"
    ts.clear()
    return flask.render_template('first.html')
@app.route('/search',methods=['GET','POST'])
def search():
    "Search Page"
    inputText = flask.request.form['documents']
    inputText = inputText.replace('\r', '')
    ts.documents = inputText
    ts.preProcessing()
    ts.index()
    print(ts.documentIndex)
    return flask.render_template('search.html')
@app.route('/results',methods=['GET','POST'])
def result():
    searchWord = flask.request.form['search_word']
    searchResults = ts.search(searchWord.lower())
    print(searchResults)
    searchResults.sort()
    return flask.render_template('results.html', searchResults=searchResults, documentIndex=ts.documentIndex, searchWord=searchWord)




if __name__ =='__main__':
    app.debug=True
    app.run(host='0.0.0.0', port= 5000)
