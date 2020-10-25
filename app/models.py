from django.db import models
from django.contrib.auth.models import User
from .models import *
# Create your models here.

# user
class Customer(models.Model):
    GRADE = (
        ('MVG','MVG'),
        ('VIP','VIP'),
        ('GOLD','GOLD'),
        ('ACE','ACE'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) # 아이디
    name = models.CharField(max_length=200, null=True) # 이름
    email = models.EmailField(max_length=200, null=True) # 이메일 
    # date_created = models.DateTimeField(auto_now_add=True, null=True) # 아이디 생성시간
    rank = models.IntegerField(max_length=None, null=True) # 순위
    grade = models.CharField(max_length=200, null=True, choices=GRADE) # 등급
    like = models.IntegerField(max_length=None, null=True) # 좋아요수
    sales = models.IntegerField(max_length=None, null=True) # 판매량
    zzim_list = models.CharField(max_length=200, null=True)
    
    
    def __str__(self):
        return self.name

# 상품
class Item(models.Model):
    #customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL) #id
    name = models.CharField(max_length=200, null=True) # 상품명
    #hastag = models.CharField(max_length=200, null=True) # 해시태그
    price = models.IntegerField(max_length=None, null=True) # 상품가격
    image = models. ImageField(upload_to='app/static/img/', blank=True, null=True) # 이미지
    # save = models.IntegerField(max_length=None, null=True) # 상품 찜 / 하트눌러서 찜하면 1, 안하면 0
    
    def __str__(self):
        return self.name


# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     # pub_date = models.DateTimeField('date published')
#     content = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
#     def __str__(self):
#         return self.title

# class Photo(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)