from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from marvel.forms import MarvelForm, MarvelForm2
from marvel.models import Marvel, db
from marvel.helpers import character_generator


site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    print('Home Page Boiiiiiii')
    return render_template('index.html')

@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    marvelform = MarvelForm()
    marvelform2 = MarvelForm2()

    try:
        if request.method == 'POST' and marvelform.validate_on_submit():
            name = marvelform.name.data
            description = marvelform.description.data
            comics_appeared_in = marvelform.comics_appeared_in.data
            super_power = marvelform.super_power.data
            user_token = current_user.token

            marvel = Marvel(name, description, comics_appeared_in, super_power, user_token)

            db.session.add(marvel)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
        elif request.method == 'POST' and marvelform2.validate_on_submit():
            name = marvelform.name.data
            user_token = current_user.token
            data = character_generator(name)
            description = data[0]['description']
            comics = data[0]['comics']


            marvel = Marvel(name, description, comics, user_token)

            db.session.add(marvel)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
    except:
        raise Exception('Character not created, please check your form and try again.')
    
    
    user_token = current_user.token
    marvels = Marvel.query.filter_by(user_token=user_token)

    return render_template('profile.html', form=marvelform, marvels=marvels)