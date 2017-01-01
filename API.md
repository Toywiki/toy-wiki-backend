## 1. 词条部分

1.1 上传图片  
URL:  
```
http://119.29.161.184:8000/uploadimage  
```
Params：  
```
FILE
```
Response：  
```
success:  
{
    'url': '/media/5f7a124e-3989-4438-b8c1-8e58c1102e6a.png',
    'statuscode': 0
}

fail:
{
    statuscode: 1
}
```
#### 1.3 查看词条
URL:
```
http://119.29.161.184:8000/wiki/viewwiki?id=xxx  
```  
Response：
```
success:
{
    'Title': "词条名字",
    "Introduction": "词条简介",
    "Content": "词条内容",
    "img": "词条URL",
    "statuscode": 0
}

fail:
{
    "statuscode": -1
}
```


## 2. 用户部分
### 2.1 用户注册
URL:(POST)
```
/user/register
```
Params:
```
{
    'account':xxx,
    'pwd':xxx
}
```

Response:
success:
```
{
    'statuscode':0
}
```
fail:
```
{
    'statuscode':-1(被占用)，-2(其他)
}
```
### 2.2 用户登录
URL:(POST)
```
/user/login
```
Params:
```
{
    'account':xxx
    'pwd':xxx
}
```

Response:
success:
```
{
    'statuscode':0
}
```
fail:
```
{
    'statuscode':-1,
    'data':密码不正确/用户不存在
}
```

### 2.3 返回三个大V
URL:(GET)
```
/user/celebrity
```
Response:
{
    'statuscode':0,
    'data':[
        {
            'account':xxx,
            'port
        }
    ]
}
```


