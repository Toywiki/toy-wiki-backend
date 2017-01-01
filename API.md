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
{"Title": "词条名字"}
```
Response：
```
success:

若存在相关词条:  
{
    existing:[
        {
            "Title":"词条1名字",
            "ID": "词条1ID",
            "Introduction": "简介1",
            "img": "图片1URL"
        },
        {
            "Title":"词条2名字",
            "ID": "词条2ID",
            "Introduction": "简介2",
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




















