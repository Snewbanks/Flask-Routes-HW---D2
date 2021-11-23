from app import app

@app.route('/')
def home():
    return "Home Page"

@app.route('/About')
@app.route('/about')
def about():
    return "Here is out About Us page.  Please feel free to learn Abount Us."

@app.route('/Contact')
@app.route('/contact')
def contact():
    return "Here is our Contact page.  Please feel free to Contact us anytime!"

@app.route('/Test')
@app.route('/test')
def test():
    return "This is out Test Page.     TEST."