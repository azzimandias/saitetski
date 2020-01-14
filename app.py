from flask import Flask
from flask import render_template


app = Flask(__name__)
if __name__ == '__main__':
    app.run()


@app.route('/')
def MainPage():
    name = 'Алексий'
    return render_template('MainPage.html', n=name)


@app.route('/SingIn')
def SingIn():
    return render_template('SingIn.html')


@app.route('/SingUp')
def SingUp():
    return render_template('SingUp.html')


@app.route('/Profile')
def Profile():
    return render_template('Profile.html')


@app.errorhandler(404)
def fourzerofour(e):
    return render_template('ErrorPage.html'), 404

