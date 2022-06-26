<div align=center><img src="https://t9.baidu.com/it/u=3434446313,2548240890&fm=85&app=131&size=f242,150&n=0&f=PNG?s=51B4A5778AB55882085C66E403007023&sec=1656349200&t=ac5da2c0626a693576283cbf71bcd0c2" width="125" height="85" /></div>
<div align=center>这是一个广州南方学院课程信息导出项目</div> 
<p>项目的技术栈：前端使用vue、后端使用python,并且需要nginx来做反向代理</p>
<p>使用流程： 下载graduation_credits中的dist文件夹，把文件夹中的文件放到nginx的html中，修改nginx的nginx.conf并运行nginx和index.py输入正确的校园网账号密码 文件就会导出，浏览器会自动下载下来</p>
<h2>导出的信息</h2>
  <li>excal的xlsx格式</li>
  <li>
    分为3个表
      <p>      
        <span>第一个表是已经修完的成绩，包括课程名称、课程性质、学分、成绩</span>
        <div align=center><img src="https://user-images.githubusercontent.com/61024898/175808596-2b658bba-4b30-4ca7-9510-a27029aa6957.png" /></div> 
      </p>
      <p>
        <span>第二个表是已经修完的成绩，包括课程名称、课程性质、学分</span>
        <div align=center><img src="https://user-images.githubusercontent.com/61024898/175808644-8aac49a1-ad55-4675-a94b-de7ca14756db.png" />
        </div>
      </p>
      <p>
        <span>第三个表是学分结构，包括课程性质、需修学分<br></span>
        <div align=center> <img src="https://user-images.githubusercontent.com/61024898/175808668-8f8ee40e-d091-4acd-9892-99afe2ec030d.png" /></div> 
      </p>
