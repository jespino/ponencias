from django.db import models

class Post(models.Model):
	title = models.CharField(maxlength=128)
	text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)


	class Admin: pass
#		list_display = ('title','pub_date')
#		list_filter = ('title','pub_date')
#		ordering = ('title','pub_date')
#		search_fields = ('title','text')

