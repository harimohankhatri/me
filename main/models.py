from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Harimohan Khatri")
    role = models.CharField(max_length=100, default="Educator and Researcher", help_text="e.g., Educator and Researcher")
    focus_area = models.CharField(max_length=200, default="Learning Models and Visual Computing", help_text="e.g., Learning Models and Visual Computing")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField(default="khatriharimohan@gmail.com")
    work_email = models.EmailField(default="harimohank@nec.edu.np", blank=True, null=True)
    phone = models.CharField(max_length=50, default="+977 9866108477", blank=True, null=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class BioParagraph(models.Model):
    content = models.TextField(help_text="Paragraph content for About Me section")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']
        verbose_name = "Bio Paragraph"
        verbose_name_plural = "Bio Paragraphs"

    def __str__(self):
        return f"Paragraph {self.display_order}: {self.content[:50]}..."


class Research(models.Model):
    STATUS_CHOICES = (
        ('idea', 'Idea'),
        ('working', 'Working'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(help_text="Detailed info text shown when toggling Info")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='working')
    publication_url = models.URLField(blank=True, null=True, help_text="Optional link to publication")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order']
        verbose_name = "Research"
        verbose_name_plural = "Research Items"

    def __str__(self):
        return self.title


class ResearchTeamMember(models.Model):
    research = models.ForeignKey(Research, on_delete=models.CASCADE, related_name='team_members')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.name} ({self.role})"


class Project(models.Model):
    STATUS_CHOICES = (
        ('idea', 'Idea'),
        ('working', 'Working'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(help_text="Detailed info text shown when toggling Info")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='working')
    collaborate_email = models.EmailField(blank=True, null=True, help_text="Email for collaborate button if applicable")
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class ProjectTeamMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='team_members')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.name} ({self.role})"


class Teaching(models.Model):
    course_name = models.CharField(max_length=200)
    is_active_semester = models.BooleanField(default=False, help_text="Active this semester (shows glow dot and classroom link)")
    materials_url = models.URLField(blank=True, null=True, help_text="Link to Course Materials")
    classroom_url = models.URLField(blank=True, null=True, help_text="Link to Google Classroom")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']
        verbose_name = "Teaching Course"
        verbose_name_plural = "Teaching Courses"

    def __str__(self):
        return self.course_name


class SocialLink(models.Model):
    platform = models.CharField(max_length=100, help_text="e.g. LinkedIn, Google Scholar, GitHub, ORCID")
    url = models.URLField()
    icon = models.FileField(upload_to='social_icons/', blank=True, null=True, help_text="SVG icon file")
    icon_static_name = models.CharField(max_length=100, blank=True, help_text="Fallback static SVG filename like linkedin.svg")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.platform


class ContactInfo(models.Model):
    CONTACT_TYPE_CHOICES = (
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('other', 'Other'),
    )
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPE_CHOICES, default='email')
    label = models.CharField(max_length=100, blank=True, help_text="e.g. Personal Email, Work Email, Mobile")
    value = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255, help_text="e.g. mailto:khatriharimohan@gmail.com or tel:+9779866108477")
    lucide_icon = models.CharField(max_length=50, default="mail", help_text="Lucide icon name e.g. mail, phone")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info Items"

    def __str__(self):
        return f"{self.value} ({self.contact_type})"
