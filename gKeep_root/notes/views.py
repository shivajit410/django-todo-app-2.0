from django.shortcuts import redirect, render

from .forms import TodoForm
from .models import Todo
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    form = TodoForm
    # form = TodoForm(request.Post)

    if request.method == 'POST':
        content = request.POST.get('content')
        todo_object = Todo(data=content)
        todo_object.save()

    context = {'todos':todos}
    return render(request, 'notes/index.html', context)


def deleteTodo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')    