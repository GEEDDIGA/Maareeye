from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hospital Management System - Maareeye</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            h1 { color: #333; }
            p { color: #666; }
            a { color: #0066cc; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>Hospital Management System - Maareeye</h1>
        <p>Welcome to the Hospital Management System</p>
        <p><a href="/admin/">Admin Panel</a></p>
        <p><a href="/hospital/">Hospital App</a></p>
    </body>
    </html>
    '''
    return HttpResponse(html)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
#     path('hospital/', include('hospital.urls')),
]
