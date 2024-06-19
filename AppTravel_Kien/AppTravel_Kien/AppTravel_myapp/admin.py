from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Category, Tour, User, News, Tag, Ticket, Booking, Rating, Payment, PaymentMethod, Comment
from .dao import count_tour_by_cat


# Register your models here.


class TravelAppAdminSite(admin.AdminSite):
    site_header = "Hệ thống quản lý du lịch"

    def get_urls(self):
        return [
            path('tour-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        stats = count_tour_by_cat()
        return TemplateResponse(request, 'admin/stats_view.html', context={
            'stats': stats
        })

class TourTagInlineAdmin(admin.TabularInline):
    model = Tour.tags.through


class TourForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Tour
        fields = '__all__'


class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = News
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'tour_name', 'description', 'category_id']
    search_fields = ['tour_name']
    list_filter = ['id', 'tour_name']
    readonly_fields = ['img']
    inlines = [TourTagInlineAdmin]
    form = TourForm
    def img(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="200" />' \
                    .format(url=obj.image.name)
            )



    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    search_fields = ['title']
    form = NewsForm


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    search_fields = ['title', 'price']
    list_filter = ['price']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'adult_quantity', 'child_quantity', 'total_price', 'user_id', 'ticket_id']


admin_site = TravelAppAdminSite(name="myapp")


admin_site.register(Category, CategoryAdmin)
admin_site.register(User)
admin_site.register(Tour, TourAdmin)
admin_site.register(Tag)
admin_site.register(Ticket, TicketAdmin)
admin_site.register(News, NewsAdmin)
admin_site.register(Payment)
admin_site.register(PaymentMethod)
admin_site.register(Booking, BookingAdmin)
admin_site.register(Comment)
admin_site.register(Rating)
