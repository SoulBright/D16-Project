from django.forms import ModelForm, Textarea


from .models import Order, Comments


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['category', 'title', 'text', 'upload']


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]


class MineCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['commentOrder', 'commentUser', 'text', 'status']
