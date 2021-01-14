from django.db import models

# Create your models here.


class Subord(models.Model):
    reporter_category = {
        ('J', 'Junior'),
        ('M', 'Middle'),
        ('S', 'Senior')
    }
    categories_employee = models.CharField(max_length=1, choices=reporter_category)


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    reporter_id = models.AutoField(primary_key=True)
    experience = models.TextField()
    profile_pic = models.ImageField(blank=True, upload_to="images/")
    employee_category = models.ForeignKey(Subord, on_delete=models.CASCADE)


class Article(models.Model):
    news_id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=200)
    content = models.TextField()
    time_of_action = models.DateTimeField(auto_now_add=True)
    images_to_upload = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=30)
    reporter_name = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return ("{} {} {}".format(self.headline, self.content, self.reporter_name))







