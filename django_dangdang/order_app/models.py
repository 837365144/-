from django.db import models
# Create your models here.
from user_app.models import User
from home_page_app.models import Book
class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    detail_address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    telphone = models.CharField(max_length=20,null=True)
    addr_mobile = models.CharField(max_length=20,null=True)
    user_id = models.ForeignKey(User, models.DO_NOTHING,db_column='user_id')
    class Meta:
        db_table = 't_address'

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    num = models.IntegerField(null=True)
    create_date = models.DateTimeField(null=True)
    price = models.FloatField(null=True)
    order_addrid = models.ForeignKey(Address, models.DO_NOTHING, db_column='order_addrid')
    order_uid = models.ForeignKey(User, models.DO_NOTHING, db_column='order_uid')
    status = models.IntegerField(null=True)

    class Meta:
        db_table = 't_order'


class Orderiterm(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    shop_bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='shop_bookid')
    shop_ordid = models.ForeignKey(Order, models.DO_NOTHING, db_column='shop_ordid')
    shop_num = models.IntegerField()
    total_price = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        db_table = 't_orderiterm'