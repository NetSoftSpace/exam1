from django.contrib import admin

from apps.company.models import Company, Vacancy, Resume


admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(Resume)
