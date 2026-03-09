from django.contrib import admin

from .models import Achievement, AchievementCat, Cat


class AchievementCatInline(admin.TabularInline):
    model = AchievementCat
    extra = 0


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'birth_year', 'owner')
    list_filter = ('color', 'birth_year')
    search_fields = ('name', 'owner__username')
    inlines = [AchievementCatInline]


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(AchievementCat)
class AchievementCatAdmin(admin.ModelAdmin):
    list_display = ('cat', 'achievement')
    list_filter = ('achievement',)
