"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application`` and ``app``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()

# Alias for Vercel Serverless Function WSGI entry point
app = application
