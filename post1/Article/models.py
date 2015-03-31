from django.db import models
from time import time
from django.core.files import File
from django.core.files.storage import FileSystemStorage 

def get_upload_file_name(instance,filename):
	return 'assets/uploaded_files/%s_%s' %(str(time()).replace('.','_'),filename)

class MyUser(models.Model) : 
	id = models.AutoField(primary_key = True)
	user_name = models.CharField(max_length = 25)
	user_password = models.CharField(max_length = 25)
	user_permission = models.IntegerField(default=2)
	posts = models.IntegerField(default=10)
	user_email = models.CharField(max_length = 30 , blank=False, null=False)
	user_college = models.CharField(max_length = 50 , blank=False, null=False)
	photo = models.FileField(upload_to = get_upload_file_name,default="himanshu.jpeg")
	security_question = models.IntegerField(default=0)
	security_answer = models.CharField(max_length=50, blank=False, null=False, default="yes")

# Create your models here.
class Article(models.Model):
	id = models.AutoField(primary_key=True, blank=False, null=False)	
	title = models.CharField(max_length=30, blank=False, null=False)
	key = models.BooleanField(blank=False, null=False, default=True)
	body = models.TextField()
	tag = models.CharField(max_length=30, help_text="Max. Characters = 30", blank=True, null=True)
	#pub_date = models.DateTimeField('date published')
	#likes = models.IntegerField(default=0)
	#all_stored_comments = None
	author = models.CharField(default="himanshu",max_length=50)
	likes = models.IntegerField(default=0)
	doc = models.FileField("Attachment", upload_to=get_upload_file_name, blank=True, null=True)
	def add_comments(comments):					#get a instance of comment class to be associated with this Article 
		all_stored_comments.append(comments)			#append / add instance of Comments in all_stored_comments list	

	def __unicode__self(self):
		return self.title

	def get_absolute_url(self):
		return "/load/%i/" % self.id
	

class Comments(models.Model):						#Class Comments to be added as child for each post
	comment = models.TextField()					#Text associsted with Comments
	id = models.AutoField(primary_key=True)
	parent_article_id = models.CharField(max_length = 50,default = "")
	
	def __unicode__self(self):
			return self.comment
