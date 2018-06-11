from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'User %s' % username


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)  # https://pyformat.info/


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
@app.route('/hello/')
@app.route('/hello/<name>')  # both of two routine can access hello.html
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
