# from django.conf.urls import url
# from django.urls import path
#
# from channels.http import AsgiHandler
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
#
# # from chat.consumers import AdminChatConsumer, PublicChatConsumer
# # from aprs_news.consumers import APRSNewsConsumer
#
# # from django.urls import re_path
# # from channels.auth import AuthMiddlewareStack
# # from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
#
# from smm.consumers import ChatConsumer
#

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
# application = ProtocolTypeRouter({
#     # Empty for now (http->django views is added by default)
# })

# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 [
#                     url("/", ChatConsumer),
#                 ]
#             )
#         )
#     ),
# })




# from channels.staticfiles import StaticFilesConsumer
# from . import consumers
#
# channel_routing = {
#     # This makes Django serve static files from settings.STATIC_URL, similar
#     # to django.views.static.serve. This isn't ideal (not exactly production
#     # quality) but it works for a minimal example.
#     'http.request': StaticFilesConsumer(),
#     # Wire up websocket channels to our consumers:
#    'websocket.connect': consumers.ws_connect,
#    'websocket.receive': consumers.ws_receive,
#    'websocket.disconnect': consumers.ws_disconnect,
# }

#************************
#
#
# application = ProtocolTypeRouter({
#     ...
#     "channel": ChannelNameRouter({
#         "thumbnails-generate": consumers.GenerateConsumer,
#         "thumbnails-delete": consumers.DeleteConsumer,
#     }),
# })
#
#
# #************************






# import chat.routing
#
# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter(chat.routing.websocket_urlpatterns)
#     ),
# })


# application = ProtocolTypeRouter({
#     "http": URLRouter([
#         url("^", DjangoViewSystem),
#     ]),
#     "websocket": URLRouter([
#         url("^chat/$", AsyncChatConsumer),
#     ]),
#     "mqtt": MqttTemperatureConsumer,
#     "email": EmailToRouter([
#         regex("@support.org", SupportTicketHandler),
#     ]),
#     "sms": SMSFromRouter([
#         phone("+1", USTextHandler),
#     ]),
# })


############################
# import judge.routing
#
# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 judge.routing.websocket_urlpatterns
#             )
#         )
#     ),
# })

# Добавить routing.py?

# from . import consumers
#
# websocket_urlpatterns = [
#     re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
# ]
