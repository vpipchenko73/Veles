#import django_tables2 as tables
from django_tables2 import Table, Column, LinkColumn, TemplateColumn
from .models import Dog
from django_tables2.utils import A  # alias for Accessor


class DogTable(Table):

    dog_health = Column( accessor='health__reverse_h__last__get_health_display', default='нет данных', order_by= 'health__reverse_h__health', verbose_name="Состояние")
    dog_sterilizacion = Column(accessor='health__sterilization', default='нет данных')
    views = Column(verbose_name="Кол-во просмотров")
    #views = Column(verbose_name="Кол-во просмотров", attrs={"th": {"style": "color: red; font-size: 20px;"}}) # пример использования стилей
    # views = Column(verbose_name="Кол-во просмотров", attrs={"td": {"class": "my-class"}}) # пример использования стилей
    dog_name = LinkColumn( "dog_list", args=[A("pk")], accessor='name', verbose_name="Кличка" )
    dog_vaccination = Column( accessor='health__dog_vaccination_str', default='нет данных',order_by= 'health__date_vaccination', verbose_name="Прививка")
    dog_worms = Column( accessor='health__dog_worms_str', default='нет данных',order_by= 'health__date_worms', verbose_name="Прием глистогонного")
    dog_age = Column( accessor='dog_age', default='нет данных',order_by= 'date_of_birth', verbose_name="Возраст")
    dog_personality = Column(accessor='get_personality_display', default='нет данных', order_by= 'personality', verbose_name="Характер")
    dog_fenotip = Column(accessor='fenotip', default='нет данных', order_by= 'fenotip', verbose_name="Порода")
    #acciones = TemplateColumn(template_code='<a href="{% url "dog_create" %}" class="btn btn-success">Test</a>') # кнопка ссылка пример

    def id_dog(self, **kwargs):
        return kwargs['id']

    class Meta:
        model = Dog
        fields = ['dog_name', 'dog_fenotip', 'dog_age', 'gender', 'dog_health', 'dog_sterilizacion','dog_vaccination', 'dog_worms','dog_personality', 'views']
        attrs = {'class': 'table table-hover',
                 'style':"text-align: center; "}





