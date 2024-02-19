from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import Courses
from .models import StudentEnrolled
from .models import TeacherTeaches
from .models import FeedbackCsn209
from .models import FeedbackCsn211
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Courses)
admin.site.register(TeacherTeaches)
admin.site.register(FeedbackCsn209)
admin.site.register(FeedbackCsn211)