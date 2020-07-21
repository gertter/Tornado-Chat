import tornado.web
import tornado.websocket


class Login(tornado.web.RequestHandler):

    def get(self):
        error = ''
        self.render('login.html', error=error)

    async def post(self):
        # 获取登录用户信息
        username = self.get_argument('username')
        password = self.get_argument('password')
        # self.get_body_argument()
        # 模拟登陆，校验功能
        if username in ['coco', 'vincent', '大大'] and password == '123456':
            # self.set_cookie('username', username)
            self.set_secure_cookie('username', username)
            await self.render('chat.html', username=username)
        else:
            error = '账号或者密码错误'
            await self.render('login.html', error=error)
