from django.db import models


class Favorite(models.Model):
    id = models.IntegerField(primary_key=True)
    m = models.ForeignKey('Member', models.DO_NOTHING, blank=True, null=True)
    r = models.ForeignKey('Restaurant', models.DO_NOTHING,
                          blank=True, null=True)

    class Meta:
        db_table = 'favorite'


class Img(models.Model):
    img = models.CharField(max_length=200, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    r = models.ForeignKey('Restaurant', models.DO_NOTHING,
                          blank=True, null=True)

    class Meta:
        db_table = 'img'


class LikeDislike(models.Model):
    like_dislike = models.IntegerField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)
    r = models.ForeignKey('Restaurant', models.DO_NOTHING,
                          blank=True, null=True)
    m = models.ForeignKey('Member', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'like_dislike'


class Member(models.Model):
    m_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    pi = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'member'


class Menu(models.Model):
    menu_name = models.CharField(max_length=200, blank=True, null=True)
    r = models.ForeignKey('Restaurant', models.DO_NOTHING,
                          blank=True, null=True)

    class Meta:
        db_table = 'menu'


class Recommend(models.Model):
    m = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
    r = models.ForeignKey('Restaurant', models.DO_NOTHING,
                          blank=True, null=True)

    class Meta:
        db_table = 'recommend'


class Restaurant(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_name = models.CharField(max_length=200, blank=True, null=True)
    r_kind = models.CharField(max_length=100, blank=True, null=True)
    des = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    address_road = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    closetime = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    r_img = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'restaurant'


class Review(models.Model):
    comment = models.CharField(max_length=200, blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    r = models.ForeignKey(Restaurant, models.DO_NOTHING, blank=True, null=True)
    m = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'review'


class Setting(models.Model):
    m = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'setting'
