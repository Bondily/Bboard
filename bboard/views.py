from django.http import HttpResponse
from .models import Bb, Rubric
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BbForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


class BbCreateView(CreateView, LoginRequiredMixin):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDetailView(DetailView, LoginRequiredMixin):
    model = Bb

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbEditView(UpdateView, LoginRequiredMixin):
    model = Bb
    form_class = BbForm
    success_url = reverse_lazy('index')
    template_name = 'bboard/bb_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbDeleteView(DeleteView, LoginRequiredMixin):
    model = Bb
    template_name = 'bboard/bb_delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    paginator = Paginator(bbs,3)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'bbs' : page.object_list, 'rubrics' : rubrics, 'page' : page }
    return render(request,'bboard/index.html',context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs' : bbs, 'rubrics' : rubrics, 'current_rubric' : current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

#def bbs(request, rubric_id):
#    BbsFormSet = inlineformset_factory(Rubric, Bb, form=BbForm, extra=1)
#    rubric = Rubric.objects.get(pk=rubric_id)
#    if request.method == 'POST':
#        formset = BbsFormSet(request.Post, instance=rubric)
#        if formset.is_valid():
#            formset.save()
#            return redirect('bboard:index')
#    else:
#        formset = BbsFormSet(instance=rubric)
#    context = {'formset':formset, 'current_rubric':rubric}
#    return render(request, 'bboard/bbs.html',context)
# Create your views here.
