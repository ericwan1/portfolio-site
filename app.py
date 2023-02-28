from flask import Flask, redirect, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = True)

@app.route("/")
def home():
    return render_template('/templates/home_page.html')

@app.route("/kormu/")
def kormu():
    return render_template('/templates/articles/kmusic_recc.html')

@app.route("/kpop-merch-prices/")
def kpop_merch_prices():
    return render_template('/templates/articles/kpop_price.html')

@app.route("/mosaic/")
def mosaic():
    return render_template('/templates/articles/mosaic.html')
