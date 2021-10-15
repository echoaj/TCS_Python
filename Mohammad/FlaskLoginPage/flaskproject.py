from flask import Flask, render_template, flash, url_for
from werkzeug.utils import redirect

from forms import*


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdenei2n3n3in2lfdfso9dfndkf'


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        flash("Succces! Your account has been created " + form.username.data, category='success')
        return redirect(url_for('home'))
    return render_template("signup.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)