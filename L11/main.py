from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = 'some_secret_key'

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
    
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        if not name and not age:
            flash(('Введіть імя та вік!', "error"))
            return render_template('add_person.html', title='add_person')

        if not name and len(name) < 2:
            flash(('Імя повинно містити мінімум 2 символи!', "error"))
            return render_template('add_person.html', title='add_person')

        if age.isdigit() == False:
            flash(('Вік повинен бути числом!', "error"))
            return render_template('add_person.html', title='add_person')
        
       

        people[name] = int(age)
        flash((f'Додано: {name}, вік: {age}', "success"))

    return render_template('add_person.html', title='add_person')

if __name__ == '__main__':
    app.run(debug=True)