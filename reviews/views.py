from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review
from .forms import UserForm, BookForm, ReviewForm

# Vista de bienvenida
def welcome(request):
    return render(request, 'welcome.html')

# Registro de usuario
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']  # Guardamos la contraseña directamente (no encriptada)
            user.save()
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

# Inicio de sesión
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            if user.password == password:  # Verificación simple de contraseña
                request.session['user_id'] = user.id
                messages.success(request, "Inicio de sesión exitoso.")
                if user.tipo == 'escritor':
                    return redirect('dashboard_escritor')
                else:
                    return redirect('dashboard_publico')
            else:
                messages.error(request, "Contraseña incorrecta.")
        except User.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")
    return render(request, 'login.html')

# Dashboard de usuario público
def dashboard_publico(request):
    return render(request, 'dashboard_publico.html')

# Dashboard de escritor
def dashboard_escritor(request):
    return render(request, 'dashboard_escritor.html')

# Agregar libro (solo para escritores)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro agregado exitosamente.")
            return redirect('dashboard_escritor')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Agregar reseña (todos los usuarios)
def add_review(request, book_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = Book.objects.get(id=book_id)
            review.user = User.objects.get(id=request.session['user_id'])
            review.save()
            messages.success(request, "Reseña agregada exitosamente.")
            return redirect('dashboard_publico')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})
