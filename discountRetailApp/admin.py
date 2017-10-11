# #encoding:utf-8
# from django.contrib import admin
# # Register your models here.
# from .models import Blog
# from  .models import  Person
# from  datetime import  datetime
#
# #可以显示的字段,在列表页显示，详情页的一些字段不会显示
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('name','age','address')
# admin.site.register(Person,PersonAdmin)
#
# # ================================================================================
# # ================================================================================
# # ================================================================================
# # ================================================================================
# # ================================================================================
#
#
# class BlogAdmin(admin.ModelAdmin):
#      # 可以显示的字段
#     list_display = ('title','content','auth','email')
#     search_fields =('auth',)
#     def get_search_results(self, request, queryset, search_term):
#         queryset,use_distinct = super(BlogAdmin,self).get_search_results(request,queryset,search_term)
#         try:
#             # name__contains or name__like 都可以
#             queryset |= self.model.objects.filter(name__contains=search_term)
#         except:
#             pass
#
#         return queryset,use_distinct
#
#
#     # obj 是blog 对象，这里可以直接更新blog 信息
#     def save_model(self, request, obj, form, change):
#         obj.auth = str(request.user)
#         obj.update_time = str(datetime.today())
#         obj.save()
#
#     # 重写delete 方法
#     def delete_model(self, request, obj):
#         obj.delete()
#
#     def get_queryset(self, request):
#         qs = super(BlogAdmin,self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         else:
#             return qs.filter(auth=request.user)
#
#
# admin.site.register(Blog,BlogAdmin)