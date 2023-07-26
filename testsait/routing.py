from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
#import chat.routing #закаментированной т.к. еше не создан чат


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            #chat.routing.websocket_urlpatterns
        )
    ),
})