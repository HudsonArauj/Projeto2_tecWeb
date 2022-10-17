from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        id = request.POST.get('id')
        tag = request.POST.get('tag')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        if tag is None:
            tag = 'none'
        note = Note(id,title, content,tag)
        note.save()
        return redirect('index')
    else:
        notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': notes})

def delete(request):  
    id = request.POST.get('id')
    note = Note.objects.get(id = id)  
    note.delete()  
    return redirect('index')

def edit(request, id):  
    note = Note.objects.get(id=id)  
    return render(request,'notes/edit.html', {'note':note})

def update(request,id):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    id = request.POST.get('id')
    tag = request.POST.get('tag')
    Note.objects.filter(id=id).update(title=title,content=content,tag = tag)
    return redirect('index')

def tags(request):
    # Notes distintas por tags
    notes = Note.objects.all().values('tag').distinct()
    return render(request, 'notes/tags.html', {'notes':  notes})


def tagSelect(request,tag):
    notes = Note.objects.filter(tag=tag)
    return render(request, 'notes/tagSelect.html', {'notes':  notes})

def home(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})