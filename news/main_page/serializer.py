from rest_framework import serializers
from .models import MainPage
import datetime


class MainPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainPage
        fields = "__all__"

    def to_representation(self, instance):
        main_page_dict = super().to_representation(instance)
        main_page_dict['today'] = datetime.date.today()

        # TODO: Adicionar cotação Dólar/ Euro / CAD
        # main_page_dict['cotacoes'] =

        # usar a biblioteca resquests


        return main_page_dict
