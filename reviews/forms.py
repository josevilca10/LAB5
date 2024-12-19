from django import forms
from .models import User, Book, Review

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=100, label="Contraseña")
    confirm_password = forms.CharField(widget=forms.PasswordInput, max_length=100, label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'nombre_completo', 'tipo']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
