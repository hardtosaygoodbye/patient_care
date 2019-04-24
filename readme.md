url_header: http://127.0.0.1:8000/api/v1/

# 用户注册
url:user/user/
method: post
param: {
    "username":"17621220087",
    "password":"smksb"
}
response: {
    "code": 0,
    "user": {
        "id": 16,
        "username": "smkhhh",
        "password": "smksb"
    },
    "token": "81e8293a-0176-4821-a2de-027468273d9f"
}

# 用户重置密码
url:user/user/
method: put
param: {
	"token": "bc0eb769-ab6e-4549-8c8d-b72253fc61dd",
	"old_password": "smksb",
	"new_password": "smksb1"
}
response: {
    "code": 0,
    "user": {
        "id": 17,
        "username": "smk1997",
        "password": "smksb1"
    }
}

# 登录
url: user/login/
method: post
param: {
    "username": "smk1997",
    "password": "smksb1"
}
response: {
    "code": 0,
    "user": {
        "id": 17,
        "username": "smk1997",
        "password": "smksb1"
    },
    "token": "759dfdce-4119-4f1f-9593-1990e7acda1b"
}

# 医院列表
url: user/hospital/
method: get
param:
response: {
    "code": 0,
    "hospitals": [
        {
            "id": 1,
            "name": "上海仁济医院"
        }
    ]
}

# 护工列表
url: user/carer/
method: get
param: hospital_id=1
response: {
    "code": 0,
    "carers": [
        {
            "id": 1,
            "name": "孙妙凯",
            "hospital_score": "0.00",
            "hospital_num": 0,
            "patient_score": "0.00",
            "patient_num": 0,
            "family_score": "0.00",
            "family_num": 0,
            "total_score": "0.00",
            "hospital": 1
        }
    ]
}

# 建议
url: user/suggestion/
method: post
param: {
	"token": "bc0eb769ab6e45498c8db72253fc61dd",
	"msg": "评价信息有误"
}
response: {
    "code": 0,
    "detail": "反馈成功"
}

# 评价
