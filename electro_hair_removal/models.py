from . import db


class Service (db.Model):
    """Модель для списка оказываемых услуг."""

    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    reserves = db.relationship('Reserve', backref='reserve')
    reviews = db.relationship('Review', backref='review')


class Reserve (db.Model):
    """Модель для учёта записей(бронирования) на приём клиентов."""

    __tablename__ = 'reserves'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String())
    telephone = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(128))
    service_name = db.Column(db.String(), db.ForeignKey('services.name'))
    full_price = db.Column(db.Integer, nullable=False)
    reserve_date = db.Column(db.Date, index=True)
    reserve_start_time = db.Column(db.DateTime, index=True)
    reserve_end_time = db.Column(db.DateTime, index=True)
    users = db.relationship('User', backref='user')
    reviews = db.relationship('Review', backref='review')


class Review (db.Model):
    """Модель для отзывов от клиентов."""

    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(), db.ForeignKey('reserves.user_name'))
    service_name = db.Column(db.String(), db.ForeignKey('services.name'))
    reserve_date = db.Column(db.Date, index=True)
    review_date = db.Column(db.Date, index=True)
    text = db.Column(db.Text, nullable=False)
    telephone = db.Column(db.String(), db.ForeignKey('reserves.telephone'))
    email = db.Column(db.String(), db.ForeignKey('reserves.email'))


class User (db.Model):
    """
    Модель клиенты.
    Информационная модель.
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), db.ForeignKey('reserves.user_name'))
    telephone = db.Column(
        db.ForeignKey('reserves.telephone'), db.String(20), nullable=False,
    )
    email = db.Column(db.String(128), db.ForeignKey('reserves.email'))
