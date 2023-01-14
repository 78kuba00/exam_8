from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Review, Product
from webapp.forms import ReviewForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class ReviewList(ListView):
    model = Review
    template_name = 'review/review_index.html'
    context_object_name = 'reviews'

class ReviewView(DetailView):
    model = Review
    template_name = 'review/review_view.html'
    context_object_name = 'review'


class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = 'review_view'
    context_object_name = 'reviews'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product = get_object_or_404(Product, pk=self.kwargs['pk'])
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.kwargs.get('pk')})

class ReviewUpdate(PermissionRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_update.html'
    success_url = 'review_view'
    context_object_name = 'form'
    permission_required = 'webapp:change_review'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().review.users.all()

    def get_success_url(self):
        return reverse(self.success_url, kwargs={'pk': self.object.pk})

class ReviewDelete(DeleteView):
    model = Review
    template_name = 'review/review_confirm_delete.html'
    success_url = reverse_lazy('review_index')
    context_object_name = 'review'
    permission_required = 'webapp:change_review'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().review.users.all()

    def get_success_url(self):
        return reverse('review_index')