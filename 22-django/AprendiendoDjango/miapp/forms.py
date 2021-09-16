from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField(
        label = 'Titulo',
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Titulo',
                'class' : 'titulo_form_article'
            }
        ),
        # validators =[
        #     validators.MaxLengthValidator(4, 'El titulo es demasiado corto'),
        #     validators.RegexValidator('^[A-Za-z0-9]*$', "El titulo esta mal formado", 'invalid_title')
        # ]
    )
    content = forms.CharField(
        label = "Contenido",
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Contenido'
            }
        ),
        required=True
    )

    content.widget.attrs.update({
        'placeholder': 'Contenido actualizado',
        'class' : 'titulo_form_article',
        'id' : 'id_article'
    })

    public_options = [
        ('', "Seleccionar"),
        (1, "Si"),
        (0, "No")
    ]
    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options,
        required=True
    )