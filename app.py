
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
# import urllib.request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/news')
def news():

    link = 'https://inshorts.com/en/read'
    req = requests.get(link)

    soup = bs(req.content, 'html5lib')
    box = soup.findAll('div', attrs = {'class':'news-card z-depth-1'})

    ha,ia,ba,la = [],[],[],[]
    # for i in range(len(box)):
    for i in range(6):
        h = box[i].find('span', attrs = {'itemprop':'headline'}).text

        m = box[i].find('div', attrs = {'class':'news-card-image'})
        m = m['style'].split("'")[1]
        # urllib.request.urlretrieve(img, f"static/news/_{i}.jpg")

        b = box[i].find('div', attrs = {'itemprop':'articleBody'}).text
        try:
            l = box[i].find('a', attrs = {'class':'source'})['href']
        except:
            pass

        ha.append(h)
        ia.append(m)
        ba.append(b)
        la.append(l)
    return render_template('news.html', ha=ha, ia=ia, ba=ba, la=la)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
