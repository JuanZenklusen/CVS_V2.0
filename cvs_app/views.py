from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UpdateUserForm, UpdateProfileForm, AcademicDataForm
from .models import Profile, Academic_Data
from django.contrib.auth.models import User

def index(request):
    context = {

    }

    return render(request, 'index.html', context)


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario creado: {username}')

            return redirect(to='profile')

        return render(request, self.template_name, {'form': form})
    

@login_required
def profile(request):
    #elementos comunes para todas las vistas
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    #elementos para esta vista
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #messages.success(request, 'Su perfil ha sido actualizado')
            return redirect(to='profile')
        
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form, 'datos_personales': datos_personales, 'academic_data': academic_data})

'''@login_required
def academic_data(request):
    datos_personales = get_object_or_404(Profile, user=request.user)

    pass'''


@login_required
def create_academic_data(request):
    #elementos comunes para todas las vistas
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    #elementos para esta vista
    if request.method == 'POST':
        academic_form = AcademicDataForm(request.POST)
        if academic_form.is_valid():
            academic_form.save(user=request.user)
            return redirect('academic')
    else:
        academic_form = AcademicDataForm()
    
    return render(request, 'academic.html', {'datos_personales': datos_personales, 'academic_data': academic_data, 'academic_form': academic_form})


@login_required
def update_academic_data(request, id):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    #elemento solo para esta vista:
    update_academic_data = get_object_or_404(Academic_Data, id=id)
    if request.method == 'POST':
        academic_form = AcademicDataForm(request.POST, instance=update_academic_data)
        if academic_form.is_valid():
            academic_form.save(user=request.user)
            return redirect('academic')
    else:
        academic_form = AcademicDataForm(instance=update_academic_data)
    return render(request, 'academic.html', {'datos_personales': datos_personales, 'academic_data': academic_data, 'academic_form': academic_form, 'update_academic_data': update_academic_data,})


@login_required
def delete_academic_data(request, id):
    #elementos comunes para todas las vistas:
    datos_personales = get_object_or_404(Profile, user=request.user)
    academic_data = Academic_Data.objects.filter(user=request.user).order_by('-nivel_id', 'estado_id')
    #elemento solo para esta vista:
    delete_academic_data = get_object_or_404(Academic_Data, id=id)
    if request.method == 'POST':
        delete_academic_data.delete()
        return redirect('profile')
    return render(request, 'delete-academic.html', {'datos_personales': datos_personales, 'academic_data': academic_data, 'delete_academic_data': delete_academic_data,})