from django.contrib import admin
from .models import Work, Complete, HappyCustomer, Skill


admin.site.register(Work)
admin.site.register(Complete)
admin.site.register(HappyCustomer)
admin.site.register(Skill)


admin.site.site_title = 'Isaac Okeyo'
admin.site.site_header = 'Isaac Admin'
admin.site.index_title = 'Welcome Isaac'
