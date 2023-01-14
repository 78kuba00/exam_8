from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Product
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

class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = 'product_view'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse(self.success_url, kwargs={'pk': self.object.pk})

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'
    success_url = 'product_view'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse(self.success_url, kwargs={'pk': self.object.pk})

class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('index')
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('index')