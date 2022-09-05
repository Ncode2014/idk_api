from flask import Flask, render_template
from w3lib.url import url_query_cleaner

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world'

@app.route("/clean", methods=["GET"])
def clean():
    if not request.args.get("url"):
        return
    query = request.args.get("url")
    try:
        if "music.amazon" in query:
            if request.args.get("track", None) in query:
                clean = url_query_cleaner(query, ['marketplaceId', "ref", "musicTerritory"], remove=True)
                return {"Success": True, "data": clean}
            else:
                return "Belum di implementasi"
    except Exception:
        return "Beberapa fitur belum di masukan "


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)