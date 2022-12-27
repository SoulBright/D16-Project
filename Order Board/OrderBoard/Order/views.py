from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Order, Comments
from .filters import CommentFilter
from .forms import OrderForm, CommentForm, MineCommentForm


class OrderList(ListView):
    model = Order
    form_class = OrderForm
    template_name = 'order_list.html'
    context_object_name = 'order_list'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class MineOrderList(LoginRequiredMixin, ListView):
    model = Comments
    form_class = MineCommentForm
    template_name = 'mine_order_list.html'
    context_object_name = 'mine_order_list'
    ordering = ['-id']
    success_url = '/mine/'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CommentFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['filterset'] = self.filterset
        return context


class OrderDetail(DetailView, FormMixin):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order_detail'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments_orders.all
        context['user'] = self.request.user
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('order_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.commentOrder = self.get_object()
        obj.commentUser = self.request.user
        obj.save()
        return super().form_valid(form)


def accept_response(request, pk):
    obj = Comments.objects.get(pk=pk)
    obj.status = True
    obj.save()
    return redirect('/mine/')


class OrderCreate(CreateView):
    template_name = 'order_create.html'
    form_class = OrderForm
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        return super().form_valid(form)


class OrderUpdate(UpdateView):
    template_name = 'order_create.html'
    form_class = OrderForm
    success_url = '/'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return Order.objects.get(pk=pk)


class OrderDelete(DeleteView):
    template_name = 'order_delete.html'
    context_object_name = 'order_delete'
    queryset = Order.objects.all()
    success_url = '/'


class CommentDelete(DeleteView):
    template_name = 'comment_delete.html'
    context_object_name = 'comment_delete'
    queryset = Comments.objects.all()
    success_url = '/mine/'
