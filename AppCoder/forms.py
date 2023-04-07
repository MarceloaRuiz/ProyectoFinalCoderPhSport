from django import forms
from AppCoder.models import Plan_Medicina_Deportiva, Plan_Kinesiologia_Fisioterapia, Plan_Nutricion, \
    Plan_Preparacion_Fisica, Plan_Psicologia_Deportiva, ComentarioMedicina, ComentarioKinesiologia, ComentarioNutricion, \
    ComentarioPreparacionFisica, ComentarioPsicologia


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


class FormularioComentarioMedicina(forms.ModelForm):
    class Meta:
        model = ComentarioMedicina
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }


class FormularioComentarioKinesiologia(forms.ModelForm):
    class Meta:
        model = ComentarioKinesiologia
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }


class FormularioComentarioNutricion(forms.ModelForm):
    class Meta:
        model = ComentarioNutricion
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }


class FormularioComentarioPreparacionFisica(forms.ModelForm):
    class Meta:
        model = ComentarioPreparacionFisica
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }


class FormularioComentarioPsicologia(forms.ModelForm):
    class Meta:
        model = ComentarioPsicologia
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }
