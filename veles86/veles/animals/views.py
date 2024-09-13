from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
# from .forms import DogFormCreate, DogFormList, DogEditMultiForm
from .forms import *

from django.urls import reverse_lazy

from django.views.generic import DetailView, CreateView, ListView, UpdateView

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)
from django_tables2 import SingleTableView
from django_tables2.paginators import LazyPaginator
from django.core.paginator import Paginator

from .tables import DogTable

# Create your views here.

def index(request):
    dogs = Dog.objects.all().last()
    test = 'asdf'
    context = {'dogs': dogs, 'test': test}
    print(dogs.date_of_birth)
    print(dogs.dog_age())
    print(datetime.now().year)

    return render(request, 'index.html', context)


def animals(request):
    dogs = Dog.objects.all()
    #dogs = Dog.objects.filter(reverse_adrow__surname='Приют').distinct()  # выбираем только животных находящихся в приюте
    health = Health.objects.all()
    diese = Disease_Vid.objects.all()
    # carusel = DogImages.objects.all()

    context = {'dogs': dogs, 'health': health, 'diese': diese, }
    return render(request, 'animals1.html', context)



class DogCreateView(CreateView):
    template_name = 'dog_create.html'
    form_class = DogEditMultiForm
    success_url = reverse_lazy('admin_panel2')

    def form_valid(self, form):
        dog = form['dog'].save(commit=False)
        dog.save()
        health = form['health'].save(commit=False)
        print(dog)
        health.subject = dog
        health.save()
        disease = form['disease'].save(commit=False)
        disease.pacient = health
        disease.save()
        print(health)
        adr_find = form['adress_f'].save(commit=False)
        adr_find.subject = dog
        adr_find.save()
        adr_owner = form['adress_o'].save(commit=False)
        adr_owner.subject = dog
        adr_owner.save()

        return redirect(self.success_url)


class DogDetailView(DetailView):
    model = Dog  # модель всё та же, но мы хотим получать детали конкретно отдельного животного
    template_name = 'dog_detail.html'  # название шаблона
    form_class = DogFormList
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_d = self.kwargs["pk"]
        context['carusel'] = DogImages.objects.filter(subject__pk=pk_d)
        dog = Dog.objects.get(pk=pk_d)
        print(dog)
        print(dog.views)
        return context


class DogReadView(BSModalReadView):
    model = Dog
    template_name = 'read_dog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_d = self.kwargs["pk"]
        context['carusel'] = DogImages.objects.filter(subject__pk=pk_d)
        dog = Dog.objects.get(pk=pk_d)
        dog.views += 1
        print(dog.views)
        dog.save()
        #context['dog_count'] = f"общее количество dog ->>{DogImages.objects.all().count()}"
        return context


class DogListView(ListView):
    model = Dog
    template_name = 'admin_panel.html'

from .filters import DogFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

class DogTableView(SingleTableMixin, FilterView):
    table_class = DogTable
    #queryset = Dog.objects.all()
    queryset = Dog.objects.filter(reverse_adrow__surname='Приют').distinct()
    template_name = "admin_panel2.html"
    filterset_class = DogFilter
    paginate_by = 5
    #paginator_class= LazyPaginator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dog_all = Dog.objects.all()
        h = 0
        p = 0
        s = 0
        d = 0
        dv = 0
        dw = 0

        for dog in dog_all:
            if ( dog.health.reverse_h.last().health == 'H'):
                h+=1
            if ( dog.health.reverse_h.last().health == 'S'):
                s+=1
            if ( dog.health.reverse_h.last().health == 'D'):
                d+=1
            if ( dog.reverse_adrow.last().surname == 'Приют'):
                p+=1
            if ( dog.reverse_adrow.last().surname == 'Приют' and dog.health.dog_vaccination() >= 365):
                dv+=1
            if ( dog.reverse_adrow.last().surname == 'Приют' and dog.health.dog_worms() >= 365):
                dw+=1
        context['dog_summa'] = Dog.objects.all().count()
        context['dog_priut'] = p
        #context['dog_health'] = Dog.objects.filter(health__reverse_h__health='H').count()
        context['dog_h'] = h
        context['dog_s'] = s
        context['dog_d'] = d
        context['dog_vaccinat'] = dv
        context['dog_worm'] = dw
        context['mess_kol'] = Message.objects.all().count()
        return context


#DogTableView.table_pagination = False

class DogUpdateView(UpdateView):
    model = Dog  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'dog_update.html'  # название шаблона будет product.html
    form_class = DogFormUpdate
    context_object_name = 'form'
    #success_url = reverse_lazy('index')

    # def get_object(self, **kwargs):
    #     id = self.kwargs.get('pk')
    #     return Dog.objects.get(pk=id)
    #
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.save()
    #     return redirect('dog_list', self.object.pk )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('dog_list', self.kwargs.get('pk') )



class HealthUpdateView(UpdateView):
    model = Health  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'нealth_update.html'  # название шаблона будет product.html
    form_class = HealthFormUpdate
    context_object_name = 'form'
    #success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('dog_list', self.kwargs.get('pk') )



class DiseaseCreateView(CreateView):
    model = Disease_Vid  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'disease_create.html'  # название шаблона будет product.html
    form_class = DiseaseFormCreate
    context_object_name = 'form'
    #success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        pk_p = self.kwargs.get('pk')
        dog_p = Dog.objects.get(pk=pk_p)
        self.object.pacient = dog_p.health
        self.object.save()
        return redirect('dog_list', pk_p )


class Adress_FindCreateView(CreateView):
    model = Adress_Find  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'adress_find_create.html'  # название шаблона будет product.html
    form_class = Adress_FindFormCreate
    context_object_name = 'form'
    #success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        pk_p = self.kwargs.get('pk')
        dog_p = Dog.objects.get(pk=pk_p)
        self.object.subject = dog_p
        self.object.save()
        return redirect('dog_list', pk_p )

Adress_Owner

class Adress_OwnerCreateView(CreateView):
    model = Adress_Owner  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'adress_owner_create.html'  # название шаблона будет product.html
    form_class = Adress_OwnerFormCreate
    context_object_name = 'form'
    #success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        pk_p = self.kwargs.get('pk')
        dog_p = Dog.objects.get(pk=pk_p)
        self.object.subject = dog_p
        self.object.save()
        return redirect('dog_list', pk_p )


class DogImageUpdateView(UpdateView):
    model = Dog
    #form_class = DogFormCreate
    template_name = 'foto_dog_update.html'
    fields = ['image',]
    #success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(DogImageUpdateView, self).get_context_data(**kwargs)
        current_object = self.object
        context['image_form'] = ImagesFormSet(instance=current_object)
        return context

    def post(self, request, **kwargs):
        request.POST = request.POST
        #print('+++++++++', request.POST)
        current_object = Dog.objects.get(id=request.POST['dogimages_set-0-subject'])
        deleted_ids = []
        for i in range(int(request.POST['dogimages_set-TOTAL_FORMS'])):  # удаление всех по галочкам
            field_delete = f'dogimages_set-{i}-DELETE'
            field_image_id = f'dogimages_set-{i}-id'
            if field_delete in request.POST and request.POST[field_delete] == 'on':
                if request.POST[field_image_id]:
                    image = DogImages.objects.get(id=request.POST[field_image_id])
                    image.delete()
                    deleted_ids.append(field_image_id)

        for i in range(int(request.POST['dogimages_set-TOTAL_FORMS'])):  # удаление всех по галочкам
            field_replace = f'dogimages_set-{i}-image'  # должен быть в request.FILES
            field_image_id = f'dogimages_set-{i}-id'  # этот файл мы заменим
            if field_replace in request.FILES and request.POST[
                field_image_id] != '' and field_image_id not in deleted_ids:
                image = DogImages.objects.get(id=request.POST[field_image_id])  #
                image.delete()  # удаляем старый файл
                for img in request.FILES.getlist(field_replace):  # новый добавили
                    DogImages.objects.create(subject=current_object, image=img)
                del request.FILES[field_replace]  # удаляем использованный файл
        if request.FILES:  # Добавление нового изображения
            #print('!!!!!', request.FILES)
            #print('LLLL', request.FILES, len(request.FILES))
            for input_name in request.FILES:
                #print('sss', input_name)
                #print('ddd',request.FILES[input_name] )
                if input_name == 'image':
                    current_object.image=request.FILES[input_name]
                    current_object.save()
                else:
                    DogImages.objects.create(subject=current_object, image=request.FILES[input_name])
        return redirect('dog_list', self.kwargs.get('pk'))

class PostCreateView( CreateView):
     form_class = PostForm
     context_object_name = 'form'
     template_name = 'post_create.html'

     def post(self, request, **kwargs):
          request.POST = request.POST
          print(request.POST)
          Post.objects.create(category=request.POST['category'], title=request.POST['title'], content=request.POST['content'])
          print(request.FILES)
          if request.FILES:  # Добавление нового изображения
              for input_name in request.FILES:
                  for img in request.FILES.getlist(input_name):
                      PostImages.objects.create(image=img, post=Post.objects.last())
          return redirect('admin_panel2')


class MessageCreateView(BSModalCreateView):
        model = Message
        form_class = MessageForm
        template_name = 'message_create.html'
        success_message = 'Success: Book was created.'
        success_url = reverse_lazy('index')



class MessageView(ListView):
        model = Message
        template_name = 'message_view.html'
        context_object_name = 'messages'
        # queryset = Post.objects.order_by('-dateCreation') # выводим статьи в обратном порядке
        ordering = ['-datecreation']


class MessageDeleteView(BSModalDeleteView):
        model = Message
        template_name = 'message_delete.html'
        queryset = Message.objects.all()
        success_message = 'Success: Message deleted'
        success_url = reverse_lazy('message_view')


class PostListView(ListView):
        model = Post
        template_name = 'post_list.html'
        context_object_name = 'posts'
        # queryset = Post.objects.order_by('-dateCreation') # выводим статьи в обратном порядке
        ordering = ['-datecreation']

        def get_context_data(self, **kwargs):
            context = super(PostListView, self).get_context_data(**kwargs)
            #current_object = self.object
            context['post_image'] = PostImages.objects.all()
            return context



