from app.register import register
from flask import request

@register.route('/userRegister', methods=['POST'])  # 只允许get请求
def register():

    request.form.get('name') # 获取POST请求参数
    return 'Hello World'  #response