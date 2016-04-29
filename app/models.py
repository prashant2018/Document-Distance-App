from django.db import models

class Documents(models.Model):
	doc1 = models.TextField(max_length=200)
	doc2 = models.TextField(max_length=200)
