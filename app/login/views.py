from flask import request
from app.login import login

@login.route('/userLogin', methods=['GET'])  # 只允许get请求
def login():
    print(request.args.to_dict())
    # request.args.get('name') # 获取get请求参数

    return 'Hello World'  #response