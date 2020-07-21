
import tornado

from tornado.websocket import WebSocketHandler
class Chat(tornado.websocket.WebSocketHandler):
    # 用于存放连接的对象
    user_online = []

    def open(self, *args, **kwargs):
        self.user_online.append(self)
        print(self)
        for user in self.user_online:
            # 当进入chat.html页面时，会主动触发该函数
            username = self.get_secure_cookie('username').decode('utf-8')
            # username = self.get_cookie('username')
            user.write_message('系统提示:【%s已进入聊天室】' % username)

    def on_message(self, message):
        # 接收前端传的数据
        username = self.get_cookie('username')
        for user in self.user_online:
            user.write_message('%s:%s' % (username, message))

    def on_close(self):
        # 移除连接对象
        self.user_online.remove(self)
        for user in self.user_online:
            username = self.get_cookie('username')
            user.write_message('系统提示:【%s已退出聊天室】' % username)
