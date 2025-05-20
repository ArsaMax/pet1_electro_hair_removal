from flask import abort, flash, redirect, render_template, url_for, request

from . import app, db
from .forms import ReserveForm
from .models import Reserve


@app.route('/', methods=['GET', 'POST'])
def index():
    form1 = ReserveForm()
    if form1.validate_on_submit():
        service_name = request.form['service_name']
        reserve_date = request.form['reserve_date']
        reserve_start_time = request.form['reserve_start_time']
        reserve_end_time = request.form['reserve_end_time']
        name = request.form['name']
        telephone = request.form['telephone']
        email = request.form['email']
        agree_pers_data = request.form['agree_pers_data']
        reserve = Reserve(
            service_name,
            reserve_date,
            reserve_start_time,
            reserve_end_time,
            name,
            telephone,
            email,
            agree_pers_data
        )
        db.session.add(reserve)
        db.session.commit()
        message = f'Запись клиента с номером телефона {telephone} произведена.'
        return render_template('add_reserve.html', message=message)
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_reserve.html', form1=form1)
