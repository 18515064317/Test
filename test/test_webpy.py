import web
import mysql.connector


## 模板文件读取，定义 头  templates为目录名称，可以是相对的 也可以是绝对的
render = web.template.render('templates')
urls = (
    '/index', 'index',
    '/blog/\d', 'blog',
    '/tiaozhuan', 'tiao',
    '/login/(.*)', 'login',
    '/article', 'article',
    '/(.*)', 'hello'
)

# class blog1:
#     def GET(self):
#         ## 请求头的读取
#         # web.header('Content-type', 'text/html;charset=utf-8')
#         # return open('hello22.html')
#         return render.hello21()

class login:
    def GET(self, name):
        return render.hello22(name)

class article:
    def GET(self):
        conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'test')
        cur = conn.cursor()
        cur.execute('select * from user')
        r = cur.fetchall()
        cur.close()
        conn.close()
        print(r)
        a = []
        for i in r:
            d = list(i)
            a.append(d)
        print(a)
        return render.article(a)

class blog1:
    def GET(self, name):
        ## 请求头的读取
        # web.header('Content-type', 'text/html;charset=utf-8')
        # return open('hello22.html')
        return render.hello22(name)
    def POST(self):
        return render.hello21()

class blog:
    def POST(self):
        data = web.input()
        return data
    def GET(self):
        ## 请求头的读取
        # return web.ctx.env
        return render.hello21()
class index:
    def GET(self):
        qurey = web.input()
        return qurey

class tiao:
    def GET(self):
        ##seeother 实现跳转 url
        return web.seeother('https://www.baidu.com/')

class hello:
    def GET(self, name):
        return 'hello  ' + name

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()