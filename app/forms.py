from django import forms
from .models import Villa

class VillaCreateForm(forms.ModelForm):

    class Meta:
        model = Villa
        fields = (
            'address',
            'category',
            'description',
            'logo',
            'price',
            'bedroom',
            'bathroom',
            'floor',
            'area',
            'parking',
            'room_count',
        )
class VillaUpdateForm(forms.ModelForm):

    class Meta:
        model = Villa
        fields = (
            'address',
            'category',
            'description',
            'logo',
            'price',
            'bedroom',
            'bathroom',
            'floor',
            'area',
            'parking',
            'room_count',
        )