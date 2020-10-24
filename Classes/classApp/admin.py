from django.contrib import admin

# Register your models here.
from .models import djangoClass

admin.site.register(djangoClass)

# class1 = djangoClass(Title="Intro To American History", CourseNumber=101, InstructorName="Edward Gonzales", Duration=30)
# class1.save()
# class2 = djangoClass(Title="Intermediate Sampling In Music", CourseNumber=151, InstructorName="J Dilla", Duration=40)
# class2.save()
# class3 = djangoClass(Title="Advanced Synth Ambience And Melodies", CourseNumber=201, InstructorName="SwuM", Duration=50)
# class3.save()