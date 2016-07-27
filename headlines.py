from flask import Flask,render_template
import feedparser

app = Flask(__name__)

RSS_FEEDS = {
	"bbc" : "http://feeds.bbci.co.uk/news/rss.xml",
	"screen": "http://screenrant.com/feed/"
}
# BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml",

# SCREENRANT_FEED = "http://screenrant.com/feed/"

# @app.route('/')
# @app.route('/<publication>')
# @app.route('/bbc')
# def bbc():
# 	return get_news('bbc')

# @app.route('/screen')
# def screen():
# 	return get_news('screen')

@app.route('/')
@app.route('/<publication>')
def get_news(publication="bbc"):
	feed = feedparser.parse(RSS_FEEDS[publication])
	# first_article = feed['entries'][0]
	return render_template("home.html",articles=feed["entries"])

	# print (first_article)
# 	return """<html>
#     <body>
#         <h1> Headlines </h1>
#         <b>{0}</b> <br/>
#         <i>{1}</i> <br/>
#         <p>{2}</p> <br/>
#     </body>
# </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))


if __name__ == '__main__':
	app.run(port=5000, debug=True)