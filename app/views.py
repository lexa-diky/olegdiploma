from django.forms import ModelForm
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from app.forms import FormForm
from app.models import AdminFormModel, MySuperModel


class FormListView(ListView):
    model = AdminFormModel
    template_name = 'list.html'


class FormFormView(FormView):
    template_name = 'builder.html'
    form_class = FormForm
    success_url = "/list"

    def form_valid(self, form):
        title = form.cleaned_data["title"]
        fields = ';'.join(form.cleaned_data['fields'])
        AdminFormModel(title=title, fields=fields).save()
        return super().form_valid(form)

def user_form(request, id):
    modell = AdminFormModel.objects.filter(id__exact=id).first()

    class MyForm(ModelForm):
        class Meta:
            model = MySuperModel
            fields = modell.fields.split(';')

    return render(request, "user.html", {'form': MyForm()})
