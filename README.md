# Dynamic Portfolio - Django & SQLite

This project converts the static personal portfolio website into a dynamic **Django application** backed by **SQLite** and **Django ORM**, while preserving 100% of the existing UI/UX, responsive layout, animations, Lucide icons, and visual design.

---

## Features

- **Dynamic Content Management**: Edit profile bio, research projects, software projects, teaching courses, social links, and contact info via Django Admin.
- **Identical UI/UX & Design**: Uses exact CSS styling, Lucide icons, responsive breakpoints, blur background overlays, circular nav indicator, and section transitions.
- **Single-Page Portfolio Application**: Kept as a single-page view (`main/index.html`) using Django templates and context processors.
- **SQLite & Django ORM**: Simple and portable relational database setup with normalized models.
- **Media & Static Asset Handling**: Configured `MEDIA_ROOT` for uploaded profile images, CV files, and social icons, and `STATIC_URL` for site assets.
- **Custom Admin Interface**: Configured with `list_display`, `list_editable`, `list_filter`, `search_fields`, and tabular inlines for team members.

---

## Project Structure

```
me/
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django CLI management utility
├── requirements.txt           # Project Python dependencies
├── README.md                  # Project documentation
├── portfolio/                 # Django project package
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Main settings (APPS, STATIC, MEDIA, DB)
│   ├── urls.py                # Root URL router
│   └── wsgi.py
├── main/                      # Core Django portfolio app
│   ├── admin.py               # Django Admin configuration & inlines
│   ├── apps.py
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py   # Seeding command matching static site data
│   ├── migrations/            # Django database migrations
│   ├── models.py              # Models: Profile, BioParagraph, Research, Project, Teaching, etc.
│   ├── static/                # Static assets (main/css, main/js, main/images)
│   │   └── main/
│   │       └── images/        # himalayas.jpg, profile.png, SVGs
│   ├── templates/
│   │   └── main/
│   │       └── index.html     # Dynamic portfolio template
│   ├── urls.py                # App URL routing
│   └── views.py               # Home view fetching models from ORM
└── media/                     # Uploaded user files (Profile picture, CV PDF, icons)
    ├── cv/
    ├── profile/
    └── social_icons/
```

---

## Installation & Setup

1. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Seed initial portfolio data**:
   ```bash
   python manage.py seed_data
   ```

5. **Create a superuser for Admin access**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the local development server**:
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` in your browser to view the dynamic portfolio.

---

## Django Admin Interface

Access the admin dashboard at:
`http://127.0.0.1:8000/admin/`

From the Admin panel, you can manage:
- **Profile**: Name, role, focus area, profile picture, CV file download, contact emails.
- **Bio Paragraphs**: Order and edit paragraphs in the About Me section.
- **Research Items**: Add/edit research papers, toggle status (`Idea`, `Working`, `Published`), add team members, and toggle visibility.
- **Projects**: Add/edit software projects, set collaboration emails, manage team members.
- **Teaching Courses**: Manage taught subjects, toggle active semester indicator (blue glow dot), course material links, and Google Classroom links.
- **Social Links & Contact Info**: Update social profile URLs, email addresses, and phone numbers.

---

## Media and Static Files

- **Static Files** (`main/static/main/images/`): Stores template assets such as background wallpaper (`himalayas.jpg`) and standard icons.
- **Media Files** (`media/`): User-uploaded assets managed via Django models (profile picture, uploaded CV PDF, custom social icons).
