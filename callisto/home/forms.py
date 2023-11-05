from django import forms
from .models import History

class ChatForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Enter a Question about 🖥️OperatingSystems",
                "class": "textinput",
            }
        ),
        label="",
    )

    class Meta:
        model = History
        exclude = ("user", )