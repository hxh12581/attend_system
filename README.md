# 基于Django的员工考勤管理系统
## 项目技术架构
- **技术选型**
```
Django(3.2.9)+Msql(8.0.29)
```
- **文件目录**
```
├── account # 账户管理模块
│ ├── models.py # 账户表模型
│ ├── urls.py # URL 配置文件
│ └── views.py # 视图处理逻辑

├── attend # 考勤管理模块
│ ├── models.py # 考勤表模型
│ ├── urls.py # URL 配置文件
│ └── views.py # 视图处理逻辑

├── attend_system # 项目根文件
│ ├── settings.py # 项目设置
│ └── urls.py # 根路由配置

├── employ_message # 员工信息管理模块
│ ├── models.py # 员工信息表模型
│ ├── urls.py # URL 配置文件
│ └── views.py # 视图处理逻辑

├── leave # 请假管理模块
│ ├── models.py # 请假表模型
│ ├── urls.py # URL 配置文件
│ └── views.py # 视图处理逻辑

├── static # 静态资源文件夹

├── templates # 模板文件夹
│ ├── account
│ │ ├── login.html # 登录页面模板
│ │ └── regist.html # 注册页面模板
│ ├── attend
│ │ ├── attend_message.html # 查看考勤信息页面模板
│ │ ├── attend_sgin_in.html # 签到页面模板
│ │ └── attend_sgin_out.html # 签退页面模板
│ ├── employee
│ │ ├── employ_message.html # 显示员工信息页面模板
│ │ └── employ_message_update.html # 更改员工信息页面模板
│ └── leave
│ ├── leave_add_show.html # 请假页面模板
│ ├── leave_message.html # 显示请假信息页面模板
│ └── leave_update_show.html # 修改请假页面模板
│ ├── head.html # 导航栏模板
│ └── index.html # 首页模板

├── README.md # 项目说明文档
└── requirements.txt # 依赖包列表
```
## 页面设计
- **员工注册页面**
![](/素材/员工注册页面.jpg)
- **员工登录页面**
![](/素材/员工登录页面.jpg)
- **首页**
![](/素材/首页.jpg)
- **编辑个人信息**
![](/素材/编辑个人信息.jpg)
- **考勤页面**
![](/素材/考勤页面.jpg)
- **请假页面**
- ![](/素材/请假页面.jpg)
- **账号管理**
- ![](/素材/账号管理.jpg)
## 功能设计
- **初始功能**
  - 登录账户功能
  - 注册账户功能
  - 退出系统功能
- **员工考勤功能**
  - 签到功能
  - 签退功能
  - 查看考勤表功能
- **员工请假功能**
  - 查看请假信息
  - 修改请假信息
  - 增加请假信息
  - 删除请假信息(销假)
- **员工账号信息管理功能**
  - 查阅员工账户信息
  - 修改员工账户信息
  - 注销员工账户
## 数据库设计(ORM)
**员工账号表**
```python
class account(models.Model):
    employ_id = models.CharField(max_length=10, primary_key=True)
    employ_name = models.CharField(max_length=10, null=True)
    employ_pwd = models.CharField(max_length=10, null=True)
```
**员工考勤表**
```python
class attend(models.Model):
    attend_id = models.CharField(max_length=10, null=True)
    attend_name = models.CharField(max_length=10, null=True)
    statu_choices = (
        ('已签到', 'Option 1'),
        ('已签退', 'Option 2'),
    )
    attend_statu = models.CharField(max_length=10, choices=statu_choices, null=True)
    attend_stime = models.DateTimeField(null=True)
    attend_etime = models.DateTimeField(null=True)
```
**员工信息表**
```python
class employee(models.Model):
    employ_id = models.CharField(max_length=10, primary_key=True)
    employ_name = models.CharField(max_length=10, null=True)
    employ_age = models.IntegerField(null=True)
    employ_gender = models.CharField(max_length=255, null=True)
    employ_Phone = models.CharField(max_length=11, null=True)
```
**员工请假表**
```python
class leave(models.Model):
    leave_id = models.CharField(max_length=10, null=True)
    leave_name = models.CharField(max_length=10, null=True)
    statu_choices = (('因私请假', 'Option 1'), ('因公请假', 'Option 2'))
    leave_statu_reason = models.CharField(choices=statu_choices, null=True, max_length=10)
    statu_choices1 = (('已请假', 'Option 1'), ('已销假', 'Option 2'))
    leave_statu = models.CharField(choices=statu_choices1, null=True, max_length=10)
    leave_reason = models.CharField(max_length=255, null=True)
    leave_stime = models.DateTimeField(null=True)
    leave_etime = models.DateTimeField(null=True)
```