from django.contrib import admin
from .models import Donor, Campaign, Donation

admin.site.register(Donor)
admin.site.register(Campaign)
admin.site.register(Donation)