from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinLengthValidator, MaxLengthValidator

#from django.forms import IntegerField



# Create your models here.

class Dog(models.Model):

    objects = None
    gender_choices =  (('M', 'Кобель'),
                      ('F', 'Сука'),
                      ('N/A', 'Не определен'))

    personality_choices = (('A', 'агрессивный'),
                      ('S', 'охранник'),
                      ('N', 'спокойный'),
                      ('G', 'добродушный'),
                      ('C', 'милашка'),
                      ('T', 'пугливый'))

    fenotip = models.ForeignKey('Poroda', on_delete=models.CASCADE, verbose_name='Порода собаки')
    gender = models.CharField(choices=gender_choices, max_length=20, default='N/A', verbose_name='Пол собаки')
    name = models.CharField(max_length=20, default='Нет данных', verbose_name='Кличка собаки ')
    date_of_birth = models.DateField(default=datetime.now, verbose_name='Дата рождения')
    personality = models.CharField(choices=personality_choices, max_length=20, default='N', verbose_name='Характер собаки')
    color = models.CharField(max_length=150, verbose_name='Окрас собаки', blank=True)
    image = models.ImageField(upload_to='dog_images/', verbose_name='Фотография животного')
    features =  models.TextField(default='Без особенностей', verbose_name='Особенности собаки')
    datecreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания карточки')
    views = models.IntegerField(default=0,null=True, blank=True, verbose_name='Количество просмотров питомца')

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'

    def __str__(self):
        return f" {self.name} / {self.fenotip} / {self.get_gender_display()} / Возраст- {self.dog_age()}" # a.get_gender_display()

    def dog_age (self):
        age = datetime.now().year - self.date_of_birth.year
        return age


class Poroda(models.Model):
    objects = None
    poroda = models.CharField(max_length=100, default='Беспопородная')

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

    def __str__(self):
        return f"{self.poroda}"


class Adress_Find(models.Model):
    subject = models.ForeignKey( Dog, related_name="reverse_adfnd", on_delete=models.CASCADE, verbose_name='Животное')
    sity = models.CharField(max_length=100, default='Ханты-Мансийск',verbose_name='Город обнаружения')
    street = models.CharField(max_length=100, blank=True, verbose_name='Улица ')
    home = models.IntegerField(null=True, blank=True, verbose_name='Номер дома ' )
    notes = models.CharField(max_length=300, default='Нет дополнительной информации о месте обнаружения',verbose_name='Дополнительная информация')
    date_find = models.DateTimeField(default=datetime.now(), verbose_name='Дата обнаружения')

    class Meta:
        verbose_name = 'Адрес обнаружения животного'
        verbose_name_plural = 'Адреса обнаружения животного'

    def __str__(self):
        return f"Город {self.sity} / Дата обнаружения {self.date_find}"

class Adress_Owner(models.Model):
    subject = models.ForeignKey( Dog, related_name="reverse_adrow", on_delete=models.CASCADE, verbose_name='Животное')
    sity = models.CharField(max_length=100, default='Ханты-Мансийск', verbose_name='Город ')
    street = models.CharField(max_length=100, blank=True, verbose_name='Улица ')
    home = models.IntegerField(null=True, blank=True, verbose_name='Номер дома владельца' )
    apartment = models.IntegerField(null=True, blank=True, verbose_name='Номер квартиры владельца' )
    surname = models.CharField(max_length=100, blank=True, default='Приют', verbose_name='Фамилия')
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, blank=True, verbose_name='Отчество' )
    phone_number = PhoneNumberField(blank=True, verbose_name='Номер телефона')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    date_location = models.DateField(default=datetime.now(), verbose_name='Дата передачи владельцу')

    class Meta:
        verbose_name = 'Адрес нахождения животного'
        verbose_name_plural = 'Адреса нахождения животного'

    def __str__(self):
        return f"Владелец {self.surname} / Город {self.sity} / Дата передачи {self.date_location}"

    def time_of_stay (self):
        delta = relativedelta( datetime.now(), self.date_location)

        return f" {delta.years} г {delta.days} дн"

class Health (models.Model):
    objects = None
    sterilization_choices = (('Y', 'Стерлизован(а)'),
                             ('N', 'Нет'),
                             ('N/Y', 'Нет данных'))

    subject = models.OneToOneField(Dog, on_delete=models.CASCADE, verbose_name='Данные животного')
    weight = models.IntegerField(verbose_name='Вес собаки')
    sterilization = models.CharField(choices=sterilization_choices, max_length=20, default='N/Y',
                                     verbose_name='Статус стерилизации')
    date_vaccination = models.DateField(default=datetime.now() - relativedelta(weeks=53), verbose_name='Дата прививки')
    date_worms = models.DateField(default=datetime.now() - relativedelta(weeks=53),
                                  verbose_name='Дата приема глистогонного')

    class Meta:
        verbose_name = 'Состояние животного'
        verbose_name_plural = 'Состояние животного'

    def __str__(self):
        return f"Субъект {self.subject.name} / вес {self.weight} / прививка {self.date_vaccination} / глистогонное {self.date_worms}"

    def dog_vaccination (self):
        delta = relativedelta( datetime.now(), self.date_vaccination)
        return delta.years*365 + delta.days

    def dog_vaccination_str (self):
        delta = relativedelta( datetime.now(), self.date_vaccination)
        if ((delta.years*365 + delta.days)-365 > 0 ):
            return f" просрочена на {delta.years*365 + delta.days-365} дн"
        else:
            return f" привит(а)"

    def dog_worms (self):
        delta = relativedelta( datetime.now(), self.date_worms)
        return delta.years*365 + delta.days

    def dog_worms_str (self):
        delta = relativedelta( datetime.now(), self.date_worms)
        if ((delta.years * 365 + delta.days) - 365 > 0):
            return f" просрочена на {delta.years * 365 + delta.days - 365} дн"
        else:
            return f" проглистогонен(а) "


class Disease_Vid (models.Model):
    objects = None
    health_choices = (('H', 'Здорова(а)'),
                     ('S', 'Болен(а)'),
                     ('D', 'Умер(ла)'))

    pacient = models.ForeignKey(Health, related_name="reverse_h", on_delete=models.CASCADE, verbose_name='Болезнь собаки')
    health = models.CharField(choices=health_choices, max_length=20, default='H', verbose_name='Состояние собаки')
    #disease = models.CharField(max_length=100,default='Здорова', verbose_name='Диагноз', blank=True)
    description = models.TextField(blank=True, default='Без патологий', verbose_name='Диагноз')
    datecreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи ')

    class Meta:
        verbose_name = 'Заболевание'
        verbose_name_plural = 'Заболевания'

    def __str__(self):
        return f"Состояние собаки {self.get_health_display()} / Диагноз {self.description[0:128]}{'...'} "


class DogImages(models.Model):
    subject = models.ForeignKey(Dog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='carusel_images/', verbose_name='Иллюстрации к карусели')

    class Meta:
        verbose_name = 'Иллюстрация к карусели'
        verbose_name_plural = 'Иллюстрации к карусели'


class Post(models.Model):
    objects = None
    health_categories = (('H', 'Уже дома'),
                         ('R', 'Обычная'))

    category = models.CharField(choices=health_categories, max_length=20, default='R', verbose_name='Категория новости')
    datecreation = models.DateField(default=datetime.now(), verbose_name='Дата создания новости')
    title = models.CharField(max_length=200, verbose_name='Название новости')
    content = models.TextField(verbose_name='Содержание новости')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f"Дата создания {self.datecreation} / Название {self.title} / Содержание {self.content}"

class PostImages(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название иллюстрации', blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Новость')
    image = models.ImageField(upload_to='post_images/', verbose_name='Иллюстрации к новости')

    class Meta:
        verbose_name = 'Иллюстрация'
        verbose_name_plural = 'Иллюстрации'

    def __str__(self):
        return f"Название иллюстрации {self.title} / Иллюстрация к новости {self.post.title} / Иллюстрация {self.image}"


class Message(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор сообщения')
    phone_number = PhoneNumberField(blank=True, verbose_name='Номер телефона для связи')
    email = models.EmailField(blank=True, null=True, verbose_name='Email для связи')
    theme = models.CharField(max_length=100, verbose_name='Тема сообщения')
    text = models.TextField(verbose_name='Текст сообщения')
    datecreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания сообщения ')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'



