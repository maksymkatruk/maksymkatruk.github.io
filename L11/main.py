from flask import Flask, render_template, request


app = Flask(__name__)

people = {
    "maksym": 20,
    "kateryna": 19,
    "vlad": 21,
    "olya": 18,
    "andrey": 22
}

@app.route('/')
def hello_world():
    return render_template('index.html', title='Головна сторінка', people=people)

@app.route('/about')
def about():
    return render_template('about.html', title='Про мене')

@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    msg = None
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        people[name] = int(age)
        msg = f'Додано: {name}, вік: {age}'

    return render_template('add_person.html', title='add_person', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)