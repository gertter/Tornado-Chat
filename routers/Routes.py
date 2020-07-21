from tornado import web

from controller.Chat import Chat
from controller.Login import Login

patterns=[
    (r'/',Login),
    (r'/chat/',Chat)
]
