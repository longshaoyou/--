import json
import requests
import pandas as pd
from wsgiref.simple_server import make_server 
def getCourse(username,password):
    url="http://ecampus.nfu.edu.cn:2929/jw-privilegei/User/r-login"
    headers={
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload={
        'username':username,
        'password':password
    }
    res=requests.post(url=url,data=payload,headers=headers)
    # res=res.text
    res=res.json()
    # print(res)
    token=res['msg']
    id=res['user']['actualId']
    if token==False:
        return False
    else: 
        data={
            'id': id,
            'jwloginToken':token
        }
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'ecampus.nfu.edu.cn:2929',
            'Origin': 'http://ecampus.nfu.edu.cn',
            'Referer': 'http://ecampus.nfu.edu.cn/',
        }
        res=requests.post("http://ecampus.nfu.edu.cn:2929/jw-cmsi/CmsKczkc/r-listByXsid",data=data,headers=headers)  
        injson=res.json()
        print(injson)
        xfjg=injson["msg"]["xfjg"]
        oldCourse=injson["msg"]["yxKccjs"]
        nowCourse=injson["msg"]["zxKczkcs"]
        oldCourseData={'课程名称':[],'课程性质':[],'学分':[],'成绩':[]}
        for course in oldCourse:
            oldCourseData['课程名称'].append(course['kcmc'])
            oldCourseData['课程性质'].append(course['kcxz'])
            oldCourseData['学分'].append(course['kcxf'])
            oldCourseData['成绩'].append(course['zpcj'])
            
        nowCourseData={'课程名称':[],'课程性质':[],'学分':[]}    
        for course in nowCourse:
            nowCourseData['课程名称'].append(course['cmsYjkc']['kcmc'])
            nowCourseData['课程性质'].append(course['cmsKcz']['cmsKcz3lbq']['kcz3lbqmc'])
            nowCourseData['学分'].append(course['kcxf'])

        xfjgData={'课程性质':[],'需修学分':[]}    
        for course in xfjg:
            xfjgData['课程性质'].append(course['l3mc'])
            xfjgData['需修学分'].append(course['xf'])
        writer= pd.ExcelWriter(f"D:/code/files/{username}.xlsx",engine='xlsxwriter') 
        dataframe=pd.DataFrame(oldCourseData)   
        dataframe.to_excel(writer,sheet_name='已修课程',index=False)
        worksheet=writer.sheets['已修课程']
        worksheet.set_column("A:Z",20)

        dataframe=pd.DataFrame(nowCourseData)   
        dataframe.to_excel(writer,sheet_name='在修课程',index=False)
        worksheet=writer.sheets['在修课程']
        worksheet.set_column("A:Z",20)

        dataframe=pd.DataFrame(xfjgData)   
        dataframe.to_excel(writer,sheet_name='学分结构',index=False)
        worksheet=writer.sheets['学分结构']
        worksheet.set_column("A:Z",20)
        writer.save()
        return  True  


#wsgi
def handle_request(env, res): 
    method=env['REQUEST_METHOD']
    SCRIPT_NAME=env['SCRIPT_NAME']
    path=env['PATH_INFO']
    
    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = env['wsgi.input'].read(request_body_size).decode()

    if method=='POST':
        x=json.loads(request_body)
        username=x['username']
        password=x['password']
        print(username,password)
        file=getCourse(username,password)
        if file==False:
            res("200 OK",[("Content-Type","application/json")]) 
            body = '{"code":400,"msg":"获取失败，请检查账号密码"}'
        else:
            res("200 OK",[("Content-Type","application/json")]) 
            body = f'{{"code":200,"data":"/files/{username}.xlsx","msg":"获取成功"}}'
        # body = f"<h1>username:{username},password:{password}</h1>"
        return [body.encode("utf-8")]
    else:  
        res("404 Not Find",[("Content-Type","text/html")]) 
        body = "<h1>404</h1>"
        return [body.encode("utf-8")]   
         
  
if __name__ == "__main__": 
  httpd = make_server("",8899,handle_request) 
  print("Serving http on port 8899") 
  httpd.serve_forever()      