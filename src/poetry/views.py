from django.shortcuts import render, redirect
from poetry.models import ChildPoetry
from django.views.generic import DetailView, ListView
from poetry.filters import PoetryFilter


class PoetryList(ListView):
    model = ChildPoetry  # Указываем модель, объекты которой мы будем выводить
    ordering = 'id'  # Поле, которое будет использоваться для сортировки объектов
    template_name = 'poetry.html'  # Указываем имя шаблона, в котором будут все инструкции о том, # как именно пользователю должны быть показаны наши объекты
    context_object_name = 'poetry'  # Это имя списка, в котором будут лежать все объекты. # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.


class PoetryDetail(DetailView):
    model = ChildPoetry
    template_name = 'poetry_by_id.html'
    context_object_name = 'poetry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stih'] = self.model.objects.get(pk=self.kwargs["pk"])
        context['text'] = context.get("stih").text.split("\n")
        context['pk'] = self.kwargs["pk"]
        if context['pk'] == self.model.objects.latest('id').__dict__.get("id"):
            context['pk_next'] = None
        else:
            context['pk_next'] = self.kwargs["pk"] + 1
        if context['pk'] == 1:
            context['pk_previous'] = None
        else:
            context['pk_previous'] = self.kwargs["pk"] - 1
        return context

