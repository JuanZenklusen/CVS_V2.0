from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from .models import Profile, Academic_Data, Job

#este modelo de formulario es para crear un nuevo usuairo
class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control',}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control',}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-control',}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control',}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password',}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password',}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


#este modelo de formulario es para editar los campos auth que vienen de usuarios de django
class UpdateUserForm(forms.ModelForm):
    #username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


#este modelo de formulario es para editar los campos de datos personales que no vienen de usuarios de django
class UpdateProfileForm(forms.ModelForm):
    dni = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'DNI', 'class': 'form-control'}))
    prefijo_cuil = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'XX', 'class': 'form-control'}))
    sufijo_cuil = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'X', 'class': 'form-control'}))
    cod_area = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Código de área', 'class': 'form-control'}))
    telefono = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Teléfono','class': 'form-control'}))
    domicilio = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Domicilio','class': 'form-control'}))
    localidad = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Localidad','class': 'form-control'}))
    provincia = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Provincia','class': 'form-control'}))
    nacionalidad = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Nacionalidad','class': 'form-control'}))
    genero = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Género','class': 'form-control'}))
    day = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'DD', 'class': 'form-control'}))
    month = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'MM', 'class': 'form-control'}))
    year = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA', 'class': 'form-control'}))
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    estado_civil = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Estado civil','class': 'form-control'}))
    imprime_estado_civil = forms.BooleanField(label='Incluir en cv', required=False,)
    cantidad_hijos = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Hijos','class': 'form-control'}))
    imprime_cantidad_hijos = forms.BooleanField(label='Incluir en cv', required=False,)


    class Meta:
        model = Profile
        fields = ['dni', 'prefijo_cuil', 'sufijo_cuil', 'cod_area', 'telefono', 'domicilio', 'localidad', 'provincia', 'nacionalidad', 'genero', 'day', 'month', 'year', 'foto', 'estado_civil', 'imprime_estado_civil', 'cantidad_hijos', 'imprime_cantidad_hijos']



class AcademicDataForm(forms.ModelForm):
    escuela = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Institución/Universidad', 'class': 'form-control'}))
    titulo = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Titulo obtenido', 'class': 'form-control'}))
    descripcion = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descripción', 'class': 'form-control'}))
    year_inicio = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA','class': 'form-control'}))
    year_fin = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA', 'class': 'form-control'}))


    class Meta:
        model = Academic_Data
        fields = ['nivel', 'estado', 'escuela', 'titulo', 'descripcion', 'year_inicio', 'year_fin']

    def save(self, user, commit=True):
        instance = super(AcademicDataForm, self).save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance
    

class JobForm(forms.ModelForm):
    empresa = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Empresa/Comercio/Familia', 'class': 'form-control'}))
    puesto = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Actividad desempeñada', 'class': 'form-control'}))
    month_inicio = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'MM', 'class': 'form-control'}))
    year_inicio = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA', 'class': 'form-control'}))
    month_fin = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'MM', 'class': 'form-control'}))
    year_fin = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'AAAA', 'class': 'form-control'}))
    referencia_nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre y apellido', 'class': 'form-control'}))
    referencia_puesto = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Puesto', 'class': 'form-control'}))
    referencia_cod_area = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Cod. área (sin cero)', 'class': 'form-control'}))
    referencia_telefono = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Teléfono (sin 15)', 'class': 'form-control'}))

    class Meta:
        model = Job
        fields = ['empresa', 'puesto', 'month_inicio', 'year_inicio', 'month_fin', 'year_fin', 'referencia_nombre', 'referencia_puesto', 'referencia_cod_area', 'referencia_telefono']
    
    def save(self, user, commit=True):
        instance = super(JobForm, self).save(commit=False)
        instance.user = user
        if commit:
            instance.save()
        return instance
