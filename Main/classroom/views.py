from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin
<<<<<<< HEAD
from django.core.exceptions import ValidationError
from django.views.generic import CreateView, DetailView, UpdateView, ListView, TemplateView
from .forms import StudentAddForm

from .models import Classroom, Comment, Profile
=======
from django.views.generic import ListView, DetailView, CreateView,TemplateView
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,FileResponse
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .filters import StudentFilter
from .forms import PdfUpload_Form
from .models import Classroom, Comment, Profile, Enrollment, Pdf
>>>>>>> origin/comment_add

#from .filters import StudentFilter



class ClassroomView(LoginRequiredMixin, TemplateView):

    login_url = 'account_login'

    template_name = 'classroom.html'

    def get(self, request):
        user = Profile.objects.get(pk=request.user.pk)
        user_classroom = user.classroom_set.all()


        context = {'user_classroom': user_classroom, 'user': user}
        return render(request, self.template_name, context)
            


class ClassroomCreateView(LoginRequiredMixin, CreateView):

    login_url = 'account_login'

    model = Classroom
    fields = ['name', 'code']
    template_name = 'createclass.html'
    success_url = '/classroom'
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



class ClassroomDetailView(LoginRequiredMixin, DetailView):

    login_url = 'account_login'

    model = Classroom
    template_name = 'classroom_detail.html'

    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs) 
        classroom_pk = self.kwargs['pk']                    
        comments = Comment.objects.filter(classroom=classroom_pk)
        context["comments"] = comments
        return context

<<<<<<< HEAD

class add_student(TemplateView):
=======
class AdviseStudentView(LoginRequiredMixin, ListView):

    login_url = 'login'

    model = Profile
    template_name ='student_advising.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StudentFilter(self.request.GET, queryset=self.get_queryset()
                .filter(user_type=Profile.UserType.STUDENT).filter(is_superuser=False))
        context['classroom'] = self.kwargs['pk']
        return context
>>>>>>> origin/comment_add

    template_name = 'add.html'

<<<<<<< HEAD
    def get(self, request, pk):
        form = StudentAddForm()

        args = {'form': form,}
        return render(request, self.template_name, args)

    def post(self, request, pk):
        form = StudentAddForm(request.POST)
        if request.method == "POST":
            if form.is_valid():

                username = form.cleaned_data['username']
                student = Profile.objects.get(username=username)
                classroom = Classroom.objects.get(pk=pk)

                classroom.students.add(student.id)
                classroom.save()
=======
def createEnrollmentView(request, pk , student_username):
    student = Profile.objects.get(username = student_username)
    classroom = Classroom.objects.get(id=pk)
    enrollment = Enrollment(students=student,classes=classroom)
    enrollment.save()
    return redirect('/classroom/' + str(pk) + '/studentadvise/')
    
>>>>>>> origin/comment_add

        
        args = {}
        return render(request, 'classroom.html', args)
    

class CommentListView(LoginRequiredMixin, ListView):

    login_url = 'account_login'

    model = Comment
    template_name = 'classroom.html'
    context_object_name = 'all_comment_list'
    ordering = ['-date_posted']

class CommentCreateView(LoginRequiredMixin, CreateView):

    login_url = 'account_login'

    model = Comment
    fields = ['comment_text']
    template_name = 'comment.html'

    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs) 
        classroom_id = self.kwargs['pk']                    
        comments = Comment.objects.filter(classroom=classroom_id)
        context["comments"] = comments
        return context
    
    def get_success_url(self, **kwargs):          
        return '/classroom/'+ str(self.kwargs['pk'])

    def form_valid(self,form):
        form.instance.commentor = self.request.user
        form.instance.classroom = Classroom.objects.get(id = self.kwargs['pk'])  
        return super().form_valid(form)

class PdfListView(LoginRequiredMixin, ListView):

    login_url = 'login'

    model = Pdf
    template_name = 'pdflist.html'
    context_object_name = 'all_pdf_list'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs) 
        classroom_id = self.kwargs['pk']                    
        pdfs = Pdf.objects.filter(classroom=classroom_id)
        context["pdfs"] = pdfs
        return context
     

class UploadPdfView(LoginRequiredMixin, CreateView):

    login_url = 'login'

    model = Pdf
    form_class = PdfUpload_Form
    template_name = 'uploadpdf.html'
    
    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs) 
        classroom_id = self.kwargs['pk']                    
        pdfs = Pdf.objects.filter(classroom=classroom_id)
        context["pdfs"] = pdfs
        return context

    def get_success_url(self, **kwargs):          
        return '/classroom/'+ str(self.kwargs['pk'])+'/pdflist/'

    def form_valid(self,form):
        if self.request.user.user_type == Profile.UserType.TEACHER:
            form.instance.teacher= self.request.user
            form.instance.classroom = Classroom.objects.get(id = self.kwargs['pk'])
            form.instance.pdflink = self.request.FILES['pdflink']
            return super().form_valid(form)
        else:
            raise ValidationError("Only teacher can upload a pdf.")


