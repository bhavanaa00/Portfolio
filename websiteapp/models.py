from django.db import models

# Create your models here.
class formdata(models.Model):
  name = models.CharField(max_length = 50, default='null')
  email = models.EmailField(max_length = 50, default='null')
  message = models.TextField(max_length = 500)

  def __str__(self):
    return self.name

class home(models.Model):
  description = models.TextField(max_length = 500)

  def __str__(self):
    return self.description

class skills(models.Model):
  icon = models.TextField()
  name = models.TextField()

  def __str__(self):
    return self.name

class project(models.Model):
  image = models.ImageField(upload_to='images/')
  title = models.TextField()
  description = models.TextField(max_length = 150)
  link = models.TextField()

  def __str__(self):
    return self.title

class work(models.Model):
  heading = models.TextField()
  status = models.TextField()
  description = models.TextField()

  def __str__(self):
    return self.heading

class about(models.Model):
  p1 = models.TextField()
  p2 = models.TextField(default='null')
  p3 = models.TextField(default='null')

  def __str__(self):
    return self.p1

class contact(models.Model):
  heading = models.TextField()
  description = models.TextField()
  email = models.EmailField()
  number = models.IntegerField()

  def __str__(self):
    return self.heading