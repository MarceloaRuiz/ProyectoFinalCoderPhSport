from django import forms
from AppCoder.models import Plan_Medicina_Deportiva, Plan_Kinesiologia_Fisioterapia, Plan_Nutricion, Plan_Preparacion_Fisica, Plan_Psicologia_Deportiva

class Plan_Medicina_DeportivaForm(forms.ModelForm):

    class Meta:
        model = Plan_Medicina_Deportiva
        fields = "__all__"

class Plan_Kinesiologia_FisioterapiaForm(forms.ModelForm):

    class Meta:
        model = Plan_Kinesiologia_Fisioterapia
        fields = "__all__"


class Plan_NutricionForm(forms.ModelForm):

    class Meta:
        model = Plan_Nutricion
        fields = "__all__"

class Plan_Preparacion_FisicaForm(forms.ModelForm):

    class Meta:
        model = Plan_Preparacion_Fisica
        fields = "__all__"


class Plan_Psicologia_DeportivaForm(forms.ModelForm):

    class Meta:
        model = Plan_Psicologia_Deportiva
        fields = "__all__"