from django import forms
from .models import FormData



class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = [
            'first_name',
            'surname',
            'fathername',
            'birth_year',
            'death_year',
            'place1_x',
            'place1_y',
            'place1_radius',
            'place1_start_year',
            'place1_end_year',
            'place2_x',
            'place2_y',
            'place2_radius',
            'place2_start_year',
            'place2_end_year',
            'place3_x',
            'place3_y',
            'place3_radius',
            'place3_start_year',
            'place3_end_year',
            ]
