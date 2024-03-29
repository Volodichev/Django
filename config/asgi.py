"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import channels
from channels.layers import get_channel_layer
from django.core.asgi import get_asgi_application

# from https://channels.readthedocs.io/en/latest/deploying.html#run-protocol-servers
import django
from channels.routing import get_default_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# application = get_asgi_application()
# from https://channels.readthedocs.io/en/latest/deploying.html#run-protocol-servers
django.setup()
application = get_default_application()

channel_layer = get_channel_layer()

