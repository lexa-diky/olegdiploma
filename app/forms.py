from django import forms


class FormForm(forms.Form):
    title = forms.CharField()
    fields = forms.MultipleChoiceField(choices=(("field1", "Field 1"), ("field2", "Filed 2"), ("field3", "Field 3")))
