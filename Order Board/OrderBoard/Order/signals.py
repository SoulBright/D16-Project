from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Comments
from OrderBoard.settings import DEFAULT_FROM_EMAIL


@receiver(signal=post_save, sender=Comments)
def new_response_created(sender, instance, created, **kwargs):
    if created:
        order = instance.commentOrder.title
        author = instance.commentOrder.author
        subject = f'New response to your order {order}'

        send_mail(
            subject=subject,
            message=f'{instance.commentUser} has left a new response to your order {order}\npreview: {instance.text}',
            recipient_list={author.email},
            from_email=DEFAULT_FROM_EMAIL
        )
    else:
        """ По скольку возможность редактирования откликов не предусмотренна ТЗ, считаю данную реализацию вполне приемлемой!"""
        order = instance.commentOrder.title
        author = instance.commentOrder.author
        subject = f'Your order response has been accepted!'
        send_mail(
            subject=subject,
            message=f'Your order response {order} has been accepted by the author {author}!',
            recipient_list={instance.commentUser.email},
            from_email=DEFAULT_FROM_EMAIL
        )
