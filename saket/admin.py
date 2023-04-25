from django.contrib import admin
from .models import Person,NewEvent, Courses_for_arts, Courses_for_sci,Courses_for_commers,Courses_for_commersPlusMaths,News, Contact
# Register your models here.
admin.site.register(Person)
admin.site.register(NewEvent)
admin.site.register(News)
admin.site.register(Courses_for_sci)
admin.site.register(Courses_for_arts)
admin.site.register(Courses_for_commersPlusMaths)
admin.site.register(Courses_for_commers)
admin.site.register(Contact)