import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.socket_io import sio
from routes.ws_no_prefix import NoPrefixNamespace
from core.config import origins

app = FastAPI()

sio.register_namespace(NoPrefixNamespace('/'))
sio_asgi_app = socketio.ASGIApp(socketio_server=sio, other_asgi_app=app)

app.add_route('/sockte.io/', route=sio_asgi_app, methods=['GET', 'POST'])
app.add_websocket_route('/socket.io/', sio_asgi_app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
