from django.contrib import admin
from OTS.models import Candidate
from OTS.models import Question
from OTS.models import Result
admin.site.register(Candidate)
admin.site.register(Result)
admin.site.register(Question)
