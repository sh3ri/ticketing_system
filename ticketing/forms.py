from django import forms


class TicketCreationForm(forms.Form):
    title = forms.CharField(max_length=100)
    priority = forms.ChoiceField(choices=((3, 'important'), (2, 'normal'), (1, 'unimportant')))
    text = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)


class MessageCreationForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)
