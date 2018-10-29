from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=128)
    book_author = models.CharField(max_length=64)
    book_publish = models.CharField(max_length=128)
    publish_time = models.DateTimeField( null=True)
    revision = models.IntegerField(null=True)
    book_isbn = models.CharField(max_length=64,null=True)
    word_count = models.IntegerField(null=True)
    page_count = models.IntegerField(null=True)
    open_type = models.CharField(max_length=20,null=True)
    book_paper = models.CharField(max_length=30,null=True)
    book_wrapper = models.CharField(max_length=64,null=True)
    book_category = models.ForeignKey('Category', models.DO_NOTHING, db_column='book_category',null=True)
    book_price = models.FloatField(null=True)
    book_dprice = models.FloatField(null=True)
    editor_recommendation = models.TextField(null=True)
    content_introduction = models.TextField(null=True)
    author_introduction = models.TextField(null=True)
    menu = models.TextField(null=True)
    media_review = models.TextField(null=True)
    digest_image_path = models.TextField(null=True)
    product_image_path = models.CharField(max_length=128,null=True)
    series_name = models.CharField(max_length=128,null=True)
    printing_time = models.DateTimeField(null=True)
    impression = models.CharField(max_length=64,null=True)
    stock = models.IntegerField(null=True)
    shelves_date = models.DateTimeField(null=True)
    customer_socre = models.DecimalField(max_digits=4, decimal_places=1,null=True)
    book_status = models.IntegerField(null=True)
    sales = models.IntegerField(null=True)

    class Meta:
        db_table = 't_book'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=20)
    book_counts = models.IntegerField( null=True)
    category_pid = models.IntegerField(null=True)

    class Meta:
        db_table = 't_category'