from django import forms
from .models import Clients, Directors


class ClientWithDirectorForm(forms.Form):
    tszh_name = forms.CharField(label="Название ТСЖ", max_length=50)
    inn = forms.CharField(label="ИНН", max_length=20)
    city = forms.CharField(label="Город", max_length=50, required=False)
    street_address = forms.CharField(label="Адрес", max_length=120, required=False)

    director_name = forms.CharField(label="ФИО директора", max_length=150)
    director_phone = forms.CharField(label="Телефон директора", max_length=50, required=False)
    director_email = forms.EmailField(label="Email директора", max_length=100, required=False)

    def save(self) -> Clients:
        director = Directors.objects.create(
            name=self.cleaned_data["director_name"],
            phone=self.cleaned_data.get("director_phone") or None,
            email=self.cleaned_data.get("director_email") or None,
        )

        client = Clients.objects.create(
            tszh_name=self.cleaned_data["tszh_name"],
            inn=self.cleaned_data["inn"],
            city=self.cleaned_data.get("city") or None,
            street_address=self.cleaned_data.get("street_address") or None,
            director=director,
        )
        return client








