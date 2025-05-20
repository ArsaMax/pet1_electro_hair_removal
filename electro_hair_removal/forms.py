from flask_wtf import FlaskForm
from wtforms import (
    BooleanField, DateField, EmailField, SelectField, StringField,
    SubmitField, TimeField, TelField
)
from wtforms.validators import DataRequired, Email, Length


dropdown_list_services = [
    'Эпиляция на 1 оборудовании', 'Эпиляция на 2 оборудовании'
]


class ReserveForm(FlaskForm):
    """Форма для создания записи клиента на приём."""

    service_name = SelectField(
        'Выберете вид услуги', choices=dropdown_list_services,
        validators=[DataRequired(message='Обязательное поле')]
    )
    reserve_date = DateField(
        'Выберете дату посещения', format='%Y-%m-%d',
        validators=[DataRequired(message='Обязательное поле')]
    )
    reserve_start_time = TimeField(
        'Выберете время записи на приём', format="%H:%M",
        validators=[DataRequired(message='Обязательное поле')]
    )
    reserve_end_time = TimeField(
        'Выберете время окончания процедуры', format="%H:%M",
        validators=[DataRequired(message='Обязательное поле')]
    )
    name = StringField(
        'Введите ваше имя',
        validators=[Length(0, 128)]
    )
    telephone = TelField(
        'Введите ваш мобильный телефон',
        validators=[DataRequired(message='Обязательное поле'), Length(3, 40)]
    )
    email = EmailField(
        'Введите ваш E-mail',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(6, 128),
            Email(check_deliverability=True)
        ]
    )
    agree_pers_data = BooleanField(
        'Согласие на обработку персональных данных', false_values=None,
        validators=[DataRequired(message='Обязательное поле')]
    )
    submit = SubmitField('Записаться')
