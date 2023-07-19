from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from .views import ClassroomView, ClassroomDetailView, CommentCreateView, ClassroomCreateView 

from . import views
=======
from .views import ClassroomView, ClassroomDetailView,CommentCreateView, ClassroomCreateView, \
    AdviseStudentView, PdfListView, UploadPdfView, createEnrollmentView
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> origin/comment_add

urlpatterns=[
    path('', ClassroomView.as_view(), name='classroom'),
    path('<int:pk>/', ClassroomDetailView.as_view(), name='classroom_detail'),
    path('<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment_create'),
    path('new/', ClassroomCreateView.as_view(), name='classroom_create'),
<<<<<<< HEAD
    path('<int:pk>/studentadvise/', views.add_student.as_view() , name="advise"),
=======
    path('<int:pk>/studentadvise/', AdviseStudentView.as_view(), name='student_advise'),
    path('<int:pk>/studentadvise/<str:student_username>/', createEnrollmentView, name='enroll'),
    path('<int:pk>/pdflist/', PdfListView.as_view(), name='pdf_list'),
    path('<int:pk>/pdflist/new/', UploadPdfView.as_view(), name='upload_pdf'),
    
    

>>>>>>> origin/comment_add
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)