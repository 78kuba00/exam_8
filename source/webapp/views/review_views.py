from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Review, Product
from webapp.forms import ReviewForm
from django.urls import reverse, reverse_lazy

class ReviewList(ListView):
    model = Review
    template_name = 'review/review_index.html'
    context_object_name = 'reviews'

class ReviewView(DetailView):
    model = Review
    template_name = 'review/review_view.html'
    context_object_name = 'review'

class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = 'review_view'
    context_object_name = 'reviews'

    def form_valid(self, form):
        print(self.kwargs.get('pk'))
        form.instance.product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.kwargs.get('pk')})

class ReviewUpdate(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_update.html'
    success_url = 'review_view'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse(self.success_url, kwargs={'pk': self.object.pk})

class ReviewDelete(DeleteView):
    model = Review
    template_name = 'review/review_confirm_delete.html'
    success_url = reverse_lazy('review_index')
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('review_index')