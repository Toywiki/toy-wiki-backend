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

## 2. 用户部分
### 2.1 用户注册
URL:
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

