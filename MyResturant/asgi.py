"""
ASGI config for MyResturant project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
# import django
# from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyResturant.settings')
# z
application = get_asgi_application()

# from channels.auth import AuthMiddleware
# from notification_app.routing import websocket_urlpatterns
# application=ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket":AuthMiddleware(
#         URLRouter(
#             websocket_urlpatterns 
#         )
#     )
# })

