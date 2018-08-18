from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    menu = "home"
    title = "Home"
    content = ["This is the Home Page"]

    return render_template(
        "index.html",
        title=title,
        menu=menu,
        paragraph=content
        )

@app.route('/about', methods=['GET', 'POST'])
def about():
    menu = "about"
    title = "About"
    content = ["This is the About Page"]
    return render_template(
        "index.html",
        title=title,
        menu=menu,
        paragraph=content
        )

@app.route('/search', methods=['GET', 'POST'])
def search():
    menu = "search"
    keyword = request.args.get('keyword', None)
    title = "Search Page"
    content = []
    result_set = []

    if keyword:
        response = requests.get(
        'https://www.google.com.au/complete/search?client=psy-ab&hl=en-AU&gs_rn=64&q='+ keyword)
        results = response.json()
        for result in results[1]:
            result_set.append(str(result[0]).replace('<b>', '').replace('</b>', ''))

        content = ["This is Search Page. User: " + keyword ]
    return render_template(
        "index.html",
        title=title,
        menu=menu,
        paragraph=content,
        result_set=result_set
        )

@app.route('/test', methods=['GET', 'POST'])
def test_api():
    menu = "test"
    user = request.args.get('user', "None")
    title = "Test API Page"
    content = ["This is Test API Page. User: " + user ]

    return render_template(
        "index.html",
        title=title,
        menu=menu,
        paragraph=content
        )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
