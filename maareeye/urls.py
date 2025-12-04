from django.urls import path
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
            a { color: #0066cc; text-decoration: none; margin: 10px 0; display: block; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>Hospital Management System - Maareeye</h1>
        <p>Welcome to the Hospital Management System</p>
        <p>Application is ready for deployment</p>
    </body>
    </html>
    '''
    return HttpResponse(html)

urlpatterns = [
    path('', home_view, name='home'),
]
