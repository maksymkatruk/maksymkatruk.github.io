from flask import Flask, render_template , request


app = Flask(__name__)

foods = [
    {"name": "apple", "price": 1.2, "quantity": 10},
    {"name": "banana", "price": 0.8, "quantity": 20},
    {"name": "orange", "price": 1.0, "quantity": 15},
    {"name": "pineapple", "price": 1.7, "quantity": 20},
    {"name": "kiwi", "price": 0.6, "quantity": 10},
    {"name": "strawberry", "price": 1.4, "quantity": 15},
]



@app.route('/')
def hello_world():
    return render_template('index.html', title='Головна сторінка')

@app.route('/items')
def items():
    return render_template('items.html', title='Продукти', foods = foods)

@app.route('/control', methods=['GET', 'POST'])
def control():
    @app.route('/control', methods=['GET', 'POST'])
    def control():
        if request.method == 'POST':
            name = request.form['name']
            price = float(request.form['price'])
            quantity = int(request.form['quantity'])
            foods.append({"name": name, "price": price, "quantity": quantity})
        return render_template('control.html', title='Адмін Панель', foods=foods)


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return render_template('cart.html', title='Кошик')



if __name__ == '__main__':
    app.run(debug=True)
