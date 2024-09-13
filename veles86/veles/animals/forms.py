from django.forms import ModelForm, BooleanField, Form

from django import forms
from django.forms import inlineformset_factory

from .models import *

from betterforms.multiform import MultiModelForm
from betterforms.forms import BetterModelForm
from django.forms import (TextInput, CharField, Textarea, CheckboxSelectMultiple,
                          Select, SelectMultiple, DateInput, CheckboxInput, NumberInput, EmailInput,
                          FileInput,)

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm

class DogFormCreate(ModelForm):
    class Meta:
        model=Dog
        #fields=[ 'gender', 'name', 'fenotip', 'check_box' ] # 'date'
        fields = '__all__'
        exclude = ('views',)
        widgets = {
            'name': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'fenotip': Select(attrs={'style': 'border: 3px solid #0d6efd'}),
            'gender': Select(attrs={'style': 'border: 3px solid #0d6efd'}),
            'date_of_birth': DateInput(format='%Y-%m-%d', attrs={"type": "date", 'style': 'border: 3px solid #0d6efd'}),
            'personality': Select(attrs={'style': 'border: 3px solid #0d6efd'}),
            'color': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'features': Textarea(attrs={'cols': 80, 'rows': 3, 'style': 'border: 3px solid #0d6efd'}),

        }



class HealthFormCreate(ModelForm):
    #check_box=BooleanField(label='Подтвердите')
    # в класс мета заносим модель и нужные нам поля
    class Meta:
        model=Health
        fields = [ 'weight', 'sterilization', 'date_vaccination', 'date_worms' ]
        # exclude = ('subject',) исключение поля из формы
        widgets = {
            'weight': NumberInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'sterilization': Select(attrs={'style': 'border: 3px solid #0d6efd'}),
            'date_vaccination': DateInput(format='%Y-%m-%d',
                                          attrs={"type": "date", 'style': 'border: 3px solid #0d6efd'}),
            'date_worms': DateInput(format='%Y-%m-%d', attrs={"type": "date", 'style': 'border: 3px solid #0d6efd'}),
        }


class DiseaseFormCreate(ModelForm):
    check_box = BooleanField(label='Подтвердите данные')
    class Meta:
        model = Disease_Vid
        fields = ['health', 'description', ]
        widgets = {
            'health': Select(attrs={'style': 'border: 3px solid #0d6efd'}),
            'description': Textarea(attrs={'cols': 80, 'rows': 3, 'style': 'border: 3px solid #0d6efd'}),
        }


class Adress_FindFormCreate(ModelForm):
    class Meta:
        model = Adress_Find
        fields = '__all__'
        exclude = ('subject',)
        widgets = {
            'sity': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'street': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'home': NumberInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'notes': Textarea(attrs={'cols': 80, 'rows': 3, 'style': 'border: 3px solid #0d6efd'}),
            'date_find': DateInput(format='%Y-%m-%d', attrs={"type": "date", 'style': 'border: 3px solid #0d6efd'}),
            'check_box': CheckboxInput(attrs={'style': 'border: 3px solid #0d6efd'}),

        }



class Adress_OwnerFormCreate(ModelForm):
    class Meta:
        model = Adress_Owner
        fields = '__all__'
        exclude = ('subject',)
        widgets = {
            'sity': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'street': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'home': NumberInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'apartment': NumberInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'surname': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'name': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'patronymic': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'phone_number': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'email': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'date_location': DateInput(format='%Y-%m-%d', attrs={"type": "date", 'style': 'border: 3px solid #0d6efd'}),

        }



class DogFormList(ModelForm):
    class Meta:
        model=Dog
        #fields = ['name']
        fields = '__all__'


class DogEditMultiForm(MultiModelForm):
    form_classes = {
        'dog': DogFormCreate,
        'health': HealthFormCreate,
        'disease': DiseaseFormCreate,
        'adress_f': Adress_FindFormCreate,
        'adress_o': Adress_OwnerFormCreate,

    }


class DogFormUpdate(ModelForm):
    check_box=BooleanField(label='Подтвердите изменения')
    # в класс мета заносим модель и нужные нам поля
    class Meta:
        model=Dog
        fields = '__all__'
        exclude = ('views', 'image',) #исключение поля из формы
        widgets = {
                 'name': TextInput(attrs={'style': 'border: 3px solid #0d6efd' }),
                 'fenotip': Select(attrs={'style': 'border: 3px solid #0d6efd' }),
                 'gender': Select(attrs={'style': 'border: 3px solid #0d6efd'}),
                 'date_of_birth': DateInput(format='%Y-%m-%d', attrs={"type": "date" , 'style': 'border: 3px solid #0d6efd'}),
                 'personality': Select(attrs={'style': 'border: 3px solid #0d6efd'}),
                 'color': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
                 'features': Textarea(attrs={'cols': 80, 'rows': 3, 'style': 'border: 3px solid #0d6efd'}),
                 'check_box': CheckboxInput(attrs={'style': 'border: 3px solid #0d6efd'}),
        }


class HealthFormUpdate(ModelForm):
    check_box=BooleanField(label='Подтвердите изменения')
    # в класс мета заносим модель и нужные нам поля
    class Meta:
        model=Health
        fields = '__all__'
        exclude = ('subject',) #исключение поля из формы
        widgets = {
            'weight': NumberInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'sterilization': Select(attrs={'style': 'border: 3px solid #0d6efd'}),
            'date_vaccination': DateInput(format='%Y-%m-%d', attrs={"type": "date" , 'style': 'border: 3px solid #0d6efd'}),
            'date_worms': DateInput(format='%Y-%m-%d', attrs={"type": "date", 'style': 'border: 3px solid #0d6efd'}),
            'check_box': CheckboxInput(attrs={'style': 'border: 3px solid #0d6efd'}),
        }


class DiseaseFormCreate(ModelForm):
    check_box=BooleanField(label='Подтвердите изменения')
    # в класс мета заносим модель и нужные нам поля
    class Meta:
        model=Disease_Vid
        fields = '__all__'
        exclude = ('pacient',) #исключение поля из формы
        widgets = {
            'health': Select(attrs={'style': 'border: 3px solid #0d6efd'}),
            'description': Textarea(attrs={'cols': 80, 'rows': 3, 'style': 'border: 3px solid #0d6efd'}),
            'check_box': CheckboxInput(attrs={'style': 'border: 3px solid #0d6efd'}),
        }



class Adress_FindFormCreate(ModelForm):
    check_box=BooleanField(label='Подтвердите изменения')
    # в класс мета заносим модель и нужные нам поля
    class Meta:
        model=Adress_Find
        fields = '__all__'
        exclude = ('subject',) #исключение поля из формы
        widgets = {
            'sity': TextInput(attrs={'style': 'border: 3px solid #0d6efd' }),
            'street': TextInput(attrs={'style': 'border: 3px solid #0d6efd' }),
            'home': NumberInput(attrs={'style': 'border: 3px solid #0d6efd'}),
            'notes': Textarea(attrs={'cols': 80, 'rows': 3, 'style': 'border: 3px solid #0d6efd'}),
            'date_find': DateInput(format='%Y-%m-%d', attrs={"type": "date", 'style': 'border: 3px solid #0d6efd'}),
            'check_box': CheckboxInput(attrs={'style': 'border: 3px solid #0d6efd'}),
        }


class Adress_OwnerFormCreate(ModelForm):
    check_box=BooleanField(label='Подтвердите изменения')
    # в класс мета заносим модель и нужные нам поля
    class Meta:
        model=Adress_Owner
        fields = '__all__'
        exclude = ('subject',) #исключение поля из формы
        widgets = {
             'sity': TextInput(attrs={'style': 'border: 3px solid #0d6efd' }),
             'street': TextInput(attrs={'style': 'border: 3px solid #0d6efd' }),
             'home': NumberInput(attrs={'style': 'border: 3px solid #0d6efd'}),
             'apartment': NumberInput(attrs={'style': 'border: 3px solid #0d6efd'}),
             'surname': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
             'name': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
             'patronymic': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
             'phone_number': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
             'email': TextInput(attrs={'style': 'border: 3px solid #0d6efd'}),
             'date_location': DateInput(format='%Y-%m-%d', attrs={"type": "date", 'style': 'border: 3px solid #0d6efd'}),
             'check_box': CheckboxInput(attrs={'style': 'border: 3px solid #0d6efd'}),
        }


ImagesFormSet = inlineformset_factory( Dog, DogImages, fields=("image",),extra=1,max_num=4,)

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PostForm(ModelForm):
    image_field = MultipleFileField(label='Выберете иллюстрации к новости')
    title = CharField(max_length=200, min_length=5, label='Название новости',
                            widget=TextInput(attrs={'style': 'border: 3px solid #0d6efd'}))
    content = CharField( min_length=10, label='Содержание новости',
                            widget=Textarea(attrs={'cols': 80, 'rows': 6, 'style': 'border: 3px solid #0d6efd'}))
    class Meta:
        model=Post
        fields = ('category', 'title', 'content',)
        widgets = {
            'category': Select(attrs={'style': 'border: 3px solid #0d6efd'}),
        }


class MessageForm(BSModalModelForm):
    check_box = BooleanField(label='Подтвердите')
    author = CharField(max_length=100, min_length=5, label='Автор сообщения - ФИО',
                      widget=TextInput(attrs={'style': 'border: 3px solid #0d6efd'}))
    phone_number = CharField(label='Номер телефона для связи',
                       widget=TextInput(attrs={'style': 'border: 3px solid #0d6efd'}))
    email = CharField(label='Email для связи',
                       widget=TextInput(attrs={'style': 'border: 3px solid #0d6efd'}))
    theme = CharField(max_length=100, min_length=5, label='Тема сообщения',
                      widget=TextInput(attrs={'style': 'border: 3px solid #0d6efd'}))
    text = CharField( min_length=10, max_length=320, label='Содержание новости',
                            widget=Textarea(attrs={'cols': 80, 'rows': 5, 'style': 'border: 3px solid #0d6efd'}))

    class Meta:
        model=Message
        fields = '__all__'











