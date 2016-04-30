from django.db import models

class Documents(models.Model):
	doc1 = models.TextField("Document 1",max_length=200)
	doc2 = models.TextField("Document 2",max_length=200)
