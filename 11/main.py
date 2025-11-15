from flask import Flask, render_template , request


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

@app.route('/add_animal', methods=['GET', 'POST'])
def add_animal():
    msg = None
    if request.method == 'POST':
        name = request.form.get('name')
        animals.append(name)
        msg = f'Додано: {name}'
        #if name == (" "):

    return render_template('add_animal.html', title='add_animal', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)
