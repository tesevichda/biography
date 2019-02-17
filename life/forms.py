from django import forms

from .models import Person, Event


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('first_name', 'patronymic', 'surname', 'snils', 'passport',
                    'birth_date', 'gender', 'email')


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'description', 'event_date')
