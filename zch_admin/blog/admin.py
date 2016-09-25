from django.contrib import admin
from .models import Article
from .models import Person
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','pub_date','update_time',)

class MyModelAdmin(admin.ModelAdmin):
	def get_queryset(self,request):
		qs=super(MyModelAdmin,self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		else:	
			return qs.filter(author=request.user)

class PersonAdmin(admin.ModelAdmin):
	list_display=('name','age',)
	search_fields=('name',)
	
	def get_search_results(self,request,queryset,search_term):
		queryset, use_distinct=super(PersonAdmin,self).get_search_results(request,queryset,search_term)
		try:
			search_term_as_int=int(search_term)
			queryset |=self.model.objects.filter(age=search_term_as_int)
		except:
			pass
		return queryset, use_distinct
	
admin.site.register( Person, PersonAdmin)
admin.site.register(Article,ArticleAdmin)
