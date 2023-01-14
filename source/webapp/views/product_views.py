from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product, Review
from webapp.forms import ProductForm
from django.urls import reverse, reverse_lazy


class ProductList(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'

class ProductView(DetailView):
    model = Product
    template_name = 'product/product_view.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.image:
            self.object.image = 'product/no-image.png'
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        reviews = self.object.reviews.all()
        paginator = Paginator(reviews, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = super().get_context_data(**kwargs)
        context['page_obj'] = page_obj
        context['is_paginated'] = page_obj.has_other_pages()
        context['reviews'] = page_obj.object_list
        return context


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = 'product_view'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'
    success_url = 'product_view'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('index')
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('webapp:index')