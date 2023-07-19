from django.contrib import admin

<<<<<<< HEAD
from .models import Classroom, Comment
=======
from .models import Classroom, Comment, Enrollment, Pdf
>>>>>>> origin/comment_add

# Register your models here.


admin.site.register(Classroom)
admin.site.register(Comment)
<<<<<<< HEAD

=======
admin.site.register(Enrollment)
admin.site.register(Pdf)
>>>>>>> origin/comment_add
