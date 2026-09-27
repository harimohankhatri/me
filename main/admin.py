from django.contrib import admin
from .models import (
    Profile,
    BioParagraph,
    Research,
    ResearchTeamMember,
    Project,
    ProjectTeamMember,
    Teaching,
    SocialLink,
    ContactInfo,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'phone', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'role', 'email')


@admin.register(BioParagraph)
class BioParagraphAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_content', 'display_order', 'is_active')
    list_display_links = ('id', 'short_content')
    list_editable = ('display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('content',)
    ordering = ('display_order',)

    def short_content(self, obj):
        return obj.content[:75] + '...' if len(obj.content) > 75 else obj.content
    short_content.short_description = "Content Preview"


class ResearchTeamMemberInline(admin.TabularInline):
    model = ResearchTeamMember
    extra = 1
    fields = ('name', 'role', 'email', 'display_order')


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'status', 'is_active')
    list_display_links = ('title',)
    list_editable = ('display_order', 'status', 'is_active')
    list_filter = ('status', 'is_active')
    search_fields = ('title', 'description')
    ordering = ('display_order',)
    inlines = [ResearchTeamMemberInline]


class ProjectTeamMemberInline(admin.TabularInline):
    model = ProjectTeamMember
    extra = 1
    fields = ('name', 'role', 'email', 'display_order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'status', 'collaborate_email', 'is_active')
    list_display_links = ('title',)
    list_editable = ('display_order', 'status', 'is_active')
    list_filter = ('status', 'is_active')
    search_fields = ('title', 'description')
    ordering = ('display_order',)
    inlines = [ProjectTeamMemberInline]


@admin.register(Teaching)
class TeachingAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'display_order', 'is_active_semester', 'is_active')
    list_display_links = ('course_name',)
    list_editable = ('display_order', 'is_active_semester', 'is_active')
    list_filter = ('is_active_semester', 'is_active')
    search_fields = ('course_name',)
    ordering = ('display_order',)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'display_order', 'url', 'is_active')
    list_display_links = ('platform',)
    list_editable = ('display_order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('platform', 'url')
    ordering = ('display_order',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'display_order', 'contact_type', 'is_active')
    list_display_links = ('label', 'value')
    list_editable = ('display_order', 'is_active')
    list_filter = ('contact_type', 'is_active')
    search_fields = ('label', 'value', 'link_url')
    ordering = ('display_order',)
