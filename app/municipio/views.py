from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


from app.municipio.forms import MunicipioForm
from app.municipio.models import Municipio


class MunicipioList(ListView):
	model = Municipio
	template_name = 'municipio/municipio_list.html'

class MunicipioCreate(CreateView):
	model = Municipio
	form_class = MunicipioForm
	template_name = 'municipio/municipio_form.html'
	success_url = reverse_lazy('municipio:municipio_listar')

class MunicipioUpdate(UpdateView):
	model = Municipio
	form_class = MunicipioForm
	template_name = 'municipio/municipio_form.html'
	success_url = reverse_lazy('municipio:municipio_listar')

class MunicipioDelete(DeleteView):
	model = Municipio
	template_name = 'municipio/municipio_delete.html'
	success_url = reverse_lazy('municipio:municipio_listar')
