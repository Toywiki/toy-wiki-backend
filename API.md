## 1. 词条部分

#### 1.1 上传图片  
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
    statuscode: -1
}
```

#### 1.2 创建词条
URL:
```
http://119.29.161.184:8000/wiki/createwiki  
```  
Params：
```
{"title": "词条名字"}
```
Response：
```
success:

若存在相关词条:  
{
    existing:[
        {
            "title":"词条1名字",
            "id": "词条1ID",
            "introduction": "简介1",
            "img": "图片1URL"
        },
        {
            "title":"词条2名字",
            "id": "词条2ID",
            "introduction": "简介2",
            "img": "图片2URL"
        },
    ]
    statuscode: 1
}

若不存在相关词条:
{
    statuscode: 0
}

fail:

{
    statuscode: -1
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
    'title': "词条名字",
    "introduction": "词条简介",
    "content": "词条内容",
    "img": "词条URL",
    "statuscode": 0
}

fail:
{
    "statuscode": -1
}
```

#### 1.4 保存新词条
URL:
```  
http://119.29.161.184:8000/wiki/savewiki    
```  
Params：  
```  
{ 
    "account": "用户ID",
    "title": "词条名字",
    "introduction": "词条简介",
    "content": "词条内容",
    "category": "词条类别",
    "img": "图片URL"
}
```  
Response：
```
success:
{
    "statuscode": 0
}

fail:
{
    "statuscode": -1
}
```

#### 1.5 编辑词条
URL:
```  
http://119.29.161.184:8000/wiki/editwiki    
```  
Params：  
```  
{ 
    "account": "用户ID",
    "wiki_id": "词条ID",
    "introduction": "词条简介",
    "content": "词条内容",
    "category": "词条类别",
    "img": "图片URL"
}
```  
Response：
```
success:
{
    "statuscode": 0
}

fail:
{
    "statuscode": -1
}
```

#### 1.6 讨论
URL:
```
http://119.29.161.184:8000/wiki/comment    
```
Params：
```
{
    "account": "用户ID",
    "wiki_id": "词条ID",
    "content": "评论内容"
}
```
Response：
```
success:
{
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

### 2.3 用户头像
URL:(GET，获取用户头像URL地址)
```
/user/portrait?account=xxx
```
Response:
```
{
    'statuscode':0,
    'portrait':xxx
}
```

URL:(POST，更新用户头像地址)
```
/user/portrait
```
Params:
```
{
    'account':xxx,
    'portrait_url':xxx,
}
```
Response:
success
```
{
    'statuscode':0
}
```
fail:
```
{
    'statuscode':-1(用户不存在)
}
```

### 2.4 查看用户简介
URL:(GET)
```
/user/profile?account=xxx
```
Response:
```
{
    'statuscode':0,
    '1':[(用户创建、并且通过审核的词条，参照浩杰的状态码)
        {
            'wiki_id':xxx,
            'title':xxx,
            'status':xxx
        },...
    ],
    '0':[(用户创建的，处于审核状态的词条)
        {
            'wiki_id':xxx,
            'title':xxx,
            'status':xxx,
        },...
    ],
    '-1':[(用户创建的、审核不通过的词条)
        {
            ...
        }
    ]
}
```


### 2.5 返回三个大V
URL:(GET)
```
/user/celebrity
```
Response:
```
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

<<<<<<< HEAD
#### 1.4 保存新词条
URL:
```  
http://119.29.161.184:8000/wiki/savewiki    
```  
Params：  
```  
{ 
    "account": "用户ID",
    "Title": "词条名字",
    "Introduction": "词条简介",
    "Content": "词条内容",
    "img": "图片URL"
}
```  
Response：
```
success:
{
    "statuscode": 0
}

fail:
{
    "statuscode": -1
}
```



















=======
>>>>>>> 92322b2331613302e73aa4032f20a27d5e962802

