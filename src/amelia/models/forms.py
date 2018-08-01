# -*- coding: utf-8 -*-

"""
    Definicje modeli formularzy.
"""

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    SelectField,
)
from wtforms.validators import (
    DataRequired,
    Email,
)
from amelia.lib.db import (
    WithDb,
    MultiSelectQuery,
)
from amelia.lib.forms import BaseModel
from amelia.models.fields import (
    TextField,
    DateField,
    IntegerField,
    EmailField,
    AutoDateField,
)


class Event(BaseModel):
    """
        Model zdarzenia.
    """

    _SQL_TABLENAME = 'events'
    verbose_name = 'Zdarzenie'
    fields = [
        TextField(
            name='name',
            verbose_name='Nazwa zdarzenia',
            help='Nazwa, maksymalnie 35 znaków'
        ),
        DateField(
            name='start_date',
            verbose_name='Data rozpoczęcia',
        ),
        DateField(
            name='end_date',
            verbose_name='Data zakończenia',
        ),
        TextField(
            name='location',
            verbose_name='Miejsce',
            help='Nazwa, maksymalnie 35 znaków'
        ),
        IntegerField(
            name='slots',
            verbose_name='Liczba miejsc',
            help='Liczba dostępnych miejsc. Zero oznacza brak limitu',
            required=False,
        ),
        TextField(
            name='desc',
            verbose_name='Opis',
            help='Opis, maksymalnie 512 znaków',
            max_length=512
        ),
    ]

    def __str__(self):
        # @FIXME: dopisać reprezentację tekstową pola
        raise NotImplementedError

    @classmethod
    def items(cls):
        """
            Pobiera z bazy danych uproszczoną (sformatowaną) listę rekordów.
        """
        # @FIXME: dopisać logikę zwracającą listę obiektów do wyświetlenia
        # (dropdown w webowym formularzu)
        raise NotImplementedError


class RegistrationForm(BaseModel):
    """
        Model formularza rejestracji.
    """
    _SQL_TABLENAME = 'registrations'
    fields = [
        IntegerField(
            verbose_name='Zdarzenie',
            name='event_id'
        ),
        TextField(
            name='first_name',
            verbose_name='Imię',
            help='Podaj imię, maksymalnie 35 znaków.'
        ),
        TextField(
            name='last_name',
            verbose_name='Nazwisko',
            help='Podaj nazwisko, maksymalnie 35 znaków.'
        ),
        EmailField(
            name='email',
            verbose_name='Adres e-mail',
            help='Podaj poprawny adres e-mail'
        ),
        AutoDateField(
            name='registration_date',
            verbose_name='Data rejestracji',
        ),
    ]

    def __str__(self):
        # @FIXME: dopisać reprezentację tekstową pola
        raise NotImplementedError


_data_required_message = 'To pole jest wymagane'
_wrong_email = 'Podaj poprawny adres e-mail'


class WebRegistrationForm(FlaskForm):
    """
        Webowy formularz rejestracji (Flask).
    """
    event_id = SelectField('Zdarzenie', choices=[])
    first_name = StringField(
        'Imię', validators=[DataRequired(message=_data_required_message)]
    )
    last_name = StringField(
        'Nazwisko', validators=[DataRequired(message=_data_required_message)]
    )
    email = StringField(
        'Adres e-mail', validators=[Email(message=_wrong_email)]
    )
    submit = SubmitField('Wyślij')
