from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Booklist
from . models import Book


# Create your views here.
# def demo(request):
#     return HttpResponse("Hello World!")
def handle_btn_click(request):
    if request.method == "POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        author=request.POST.get('author',)
        img=request.FILES['img']
        book=Book(name=name,desc=desc,author=author,img=img)
        book.save()
        return redirect('/')
    return render(request,'add.html')
def index(request):
    book=Book.objects.all()
    context={
        'books':book
    }
    return render(request,'index.html',context)

def detail(request,book_no):
    book=Book.objects.get(id=book_no)
    return render(request,"detail.html",{'book':book})

def add_book(request):
    if request.method == "POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        author=request.POST.get('author',)
        img=request.FILES('image',)
        book=Book(name=name,desc=desc,author=author,image=img)
        book.save()
    return render(request,'add.html')

def update(request,book_no):
    book=Book.objects.get(id=book_no)
    form=Booklist(request.POST or None, request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'book':book})

def delete(request,book_no):
    if request.method=='POST':
        book=Book.objects.get(id=book_no)
        book.delete()
        return redirect('/')
    return render(request,'delete.html',)

