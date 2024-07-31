from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import LinkForm
from .models import URL_map
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = LinkForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if custom_id:
            if URL_map.query.filter_by(short=custom_id).first() is not None:
                flash(f'Имя {custom_id} уже занято!',
                      'not-unique-link')
                return render_template('link.html', form=form)
            short_link = form.custom_id.data
        else:
            short_link = get_unique_short_id()
        url = URL_map(
            original=form.original_link.data,
            short=short_link,
        )
        db.session.add(url)
        db.session.commit()
        link = url_for('redirect_to_original',
                       short_id=url.short, _external=True)
        flash(link, category='link')

    return render_template('link.html', form=form)


@app.route('/<short_id>')
def redirect_to_original(short_id):
    url_map = URL_map.query.filter_by(short=short_id).first_or_404()
    return redirect(url_map.original, code=302)
