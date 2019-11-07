from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user

from CloudWebsiteAssignment3.models.users import User
from CloudWebsiteAssignment3.endpoints.Login.forms import LoginForm


login = Blueprint('login', __name__)


@login.route('/login', methods=['GET', 'POST'])
def login_view():
    form = LoginForm()

    if not form.validate_on_submit():
        return render_template('Login/login.html', form=form)
    else:
        email = form.email.data
        password = form.password.data

        # Query for a user with the provided username
        result = User.query.filter_by(email=email).first()

        if result is not None and password == result.password_:
            # Login user
            login_user(result)
            return render_template('index.html', user=result)
        else:
            return render_template('Login/login.html', form=form)


@login.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()

    return redirect('login')


@login.route('/forget_pw')
def forget_pw():
    return render_template("Login/forget_pw.html")


@login.route('/reset_pw')
def reset_pw():
    return render_template("Login/reset_pw.html")

