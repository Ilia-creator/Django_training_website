from django.db import models


# Create your models here.

class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Status name')

    def __str__(self):
        return self.status_name


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now= True)
    order_name = models.CharField(max_length= 200, verbose_name= 'Name')
    order_phone = models.CharField(max_length=200, verbose_name= 'Phone number')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Status")

    def __str__(self):
        return self.order_name

class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Bid')
    comment_text = models.TextField(verbose_name='Comment text')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Comment creating date')

    def __str__(self):
        return self.comment_text
