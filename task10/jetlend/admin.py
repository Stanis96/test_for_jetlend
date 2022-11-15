from django.contrib import admin

from jetlend.models import Borrower, Loan

# Register your models here.


admin.site.register(Borrower)
admin.site.register(Loan)
