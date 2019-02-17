from django.contrib import admin
from .models import Person
from .models import Event
from .models import Document
from .models import Education
from .models import Pupil

admin.site.register(Person)
admin.site.register(Document)
admin.site.register(Education)
admin.site.register(Pupil)
admin.site.register(Event)
