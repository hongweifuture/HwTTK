> 基于`Python`的邮件发送模块封装

## 说明
- 支持`Python2`和`Python3`，自动兼容，无需设置
- 支持`参数化配置`，如需其他文本配置文件请自行修改
- 支持文字、音频、文本、图片、应用程序及其他类型文件的`附件发送`
- 支持一次性发送`多个附件`
- 支持不同的邮箱
- 支持向多用户邮箱发送邮件
- 支持中文命名的邮件发送
- 支持邮件内容自定义
- 无需安装其他依赖，标准库即可运行

## 使用
```python
python HwSendEmail.py
```

```ini

;login_username : 登陆发件人用户名

;login_password : 登陆发件人密码

;host:port : 发件人邮箱对应的host和端口，如：smtp.163.com:25 和 smtp.qq.com:465

;receiver : 收件人，支持多方发送，格式（注意英文逗号）： 123456789@163.com,zxcvbnm@qq.com


[SMTP]
login_username = johnny@163.com

login_password = johnny

host = smtp.163.com

port = 25

receiver = johnny1@qq.com,johnny2@163.com,johnny3@gmail.com
```
