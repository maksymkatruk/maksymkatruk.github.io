from flask import Flask, render_template

app = Flask(__name__)

animals = [
    "dog", "cat", "monkey", "horse", "tiger"
]

@app.route('/')
def hello_world():
    return render_template('index.html', title='Головна сторінка', animals = animals)

@app.route('/about')
def about():
    return render_template('about.html', title='Про мене')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакти')

if __name__ == '__main__':
    app.run(debug=True)
