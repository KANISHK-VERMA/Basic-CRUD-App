from django.shortcuts import render,redirect,get_object_or_404
from .forms import Sform
from.models import Student
from django.http import HttpResponseRedirect
# Create your views here.
def form_view(request,*args,**kwargs):
    if request.method=="POST":
        student=Sform(request.POST)
        if student.is_valid():
            student.save()
            return redirect('ndetail')

    else:
     student=Sform()

     return render(request,'sportal.html',{'student':student})

def home_view(request,*args,**kwargs):

    return render(request,'base.html')
#def detail_view(request,pk):
 #   student=get_object_or_404(Sform,pk=pk)
  #  return render(request,'sdetail.html',{'student':student})

def detail_view(request,*args,**kwargs):
    obj=Student.objects.all()
    context = {
        'object':obj
    }
    return render(request,'sdetail.html',context)

def edit_view(request,pk):
    obj=get_object_or_404(Student,pk=pk)
   # if request.method == "POST":
    student = Sform(request.POST or None,instance=obj)
    if student.is_valid():
            student.save()
           # return redirect('ndetail',pk=obj.pk)
            return HttpResponseRedirect("/"+pk)
    return render(request,"sedit.html",{'student':student})

def delete_view(request,pk):
    obj=get_object_or_404(Student,pk=pk)

   # if request.method == "POST":
    if request.method=="POST":
            obj.delete()
           # return redirect('ndetail',pk=obj.pk)
            return redirect("../../")
    context = {
        'object': obj
    }
    return render(request,"sdelete.html",context)

