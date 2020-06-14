from flask import Flask


app = Flask(__name__)


# 路由：处理URL和函数之间的程序叫做路由
@app.route('/')
def index():  # 视图函数
    return '<h1>Hello world!</h1>'


# 动态路由
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


if __name__ == '__main__':
    app.run()