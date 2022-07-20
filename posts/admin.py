from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title",]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "updated_at"]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "selary", "user"]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["title",]


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ["title", "region"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "company_name", "years"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ["user","title", "university", "department", "degree", "years"]