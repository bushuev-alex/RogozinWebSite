from django.shortcuts import render, redirect
from prose.models import ProjitoeNeUgasaet, ThoughtAboutLived, PagesOfHistory
from django.views.generic import DetailView, ListView, TemplateView
# from prose.filters import ProseFilter
from prose.forms import PageRequestForm


class Prose(TemplateView):
    template_name = 'prose.html'
    context_object_name = 'prose'


# LIVED
class LivedDetail(DetailView):
    model = ProjitoeNeUgasaet
    template_name = 'prose_by_id.html'
    context_object_name = 'prose'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.model.objects.get(pk=self.kwargs["pk"]).text.split("\n")
        context['pk'] = self.kwargs["pk"]
        if context['pk'] == self.model.objects.latest('id').__dict__.get("id"):
            context['pk_next'] = None
        else:
            context['pk_next'] = self.kwargs["pk"] + 1
        if context['pk'] == 1:
            context['pk_previous'] = None
        else:
            context['pk_previous'] = self.kwargs["pk"] - 1
        context['form'] = PageRequestForm
        context['model_name'] = "lived"
        context['full_name'] = "Прожитое не угасает"
        return context

    def post(self, request, *args, **kwargs):
        page_number = request.POST.get("description")
        return redirect(f"/prose/lived/{page_number}/")


# THOUGHTS
class ThoughtsDetail(DetailView):
    model = ThoughtAboutLived
    template_name = 'prose_by_id.html'
    context_object_name = 'thoughts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.model.objects.get(pk=self.kwargs["pk"]).text.split("\n")
        context['pk'] = self.kwargs["pk"]
        context['pk_next'] = self.kwargs["pk"] + 1
        context['pk_previous'] = self.kwargs["pk"] - 1
        context['form'] = PageRequestForm
        context['model_name'] = "thoughts"
        context['full_name'] = "Думы о прожитом"
        return context

    def post(self, request, *args, **kwargs):
        page_number = request.POST.get("description")
        return redirect(f"/prose/thoughts/{page_number}/")


# PAGES
class PagesDetail(DetailView):
    model = PagesOfHistory
    template_name = 'prose_by_id.html'
    context_object_name = 'pages'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = self.model.objects.get(pk=self.kwargs["pk"]).text.split("\n")
        context['pk'] = self.kwargs["pk"]
        context['pk_next'] = self.kwargs["pk"] + 1
        context['pk_previous'] = self.kwargs["pk"] - 1
        context['form'] = PageRequestForm
        context['model_name'] = "pages"
        context['full_name'] = "Странички истории"
        return context

    def post(self, request, *args, **kwargs):
        page_number = request.POST.get("description")
        return redirect(f"/prose/pages/{page_number}/")


def redirect_to_prose(request, **kwargs):
    return redirect(f"/prose/")


def get_about_info(request):
    return render(request, 'flatpages/about.html')


def main_page(request):
    return render(request, 'flatpages/main_page.html')
