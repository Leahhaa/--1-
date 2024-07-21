from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Главная страница'}
    return render_template('main.html', **context)

@app.route('/clothes')
def clothes():
    context = {'title': 'DRKSHDW',
               'more': 'Узнать побольше',
               }
    return render_template('clothes.html', **context)


@app.route('/shoes')
def shoes():
    context = {'title': 'shoes',
               'more': 'Узнать побольше',
               }
    return render_template('shoes.html', **context)

@app.route('/jackets')
def jacket():
    context = {'title': 'RICK OWENS',
               'more': 'Узнать побольше',
               }
    return render_template('jackets.html', **context)




if __name__ == '__main__':
    app.run(debug=True)