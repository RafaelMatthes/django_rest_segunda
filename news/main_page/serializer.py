from rest_framework import serializers
from .models import MainPage
import datetime

CURRENCY_LIST = ["USD", "CAD", "EUR", "JPY"]

from .business_logic import CurrencyRate

class MainPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainPage
        fields = "__all__"

    def to_representation(self, instance):
        main_page_dict = super().to_representation(instance)
        main_page_dict['today'] = datetime.date.today()
        main_page_dict['cotacoes'] = [
            {item: CurrencyRate.get_price(item) }
            for item in CURRENCY_LIST
        ]

        return main_page_dict
