from django.shortcuts import render
from .models import (
    Profile,
    BioParagraph,
    Research,
    Project,
    Teaching,
    SocialLink,
    ContactInfo,
)


def home(request):
    profile = Profile.objects.filter(is_active=True).first()
    bio_paragraphs = BioParagraph.objects.filter(is_active=True).order_by('display_order')
    researches = Research.objects.filter(is_active=True).prefetch_related('team_members').order_by('display_order')
    projects = Project.objects.filter(is_active=True).prefetch_related('team_members').order_by('display_order')
    teaching_items = Teaching.objects.filter(is_active=True).order_by('display_order')
    social_links = SocialLink.objects.filter(is_active=True).order_by('display_order')
    contact_infos = ContactInfo.objects.filter(is_active=True).order_by('display_order')

    context = {
        'profile': profile,
        'bio_paragraphs': bio_paragraphs,
        'researches': researches,
        'projects': projects,
        'teaching_items': teaching_items,
        'social_links': social_links,
        'contact_infos': contact_infos,
    }
    return render(request, 'main/index.html', context)
