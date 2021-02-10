import os
import pathlib
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


class Mail():
    def send_mail(self,send_user, send_pw, send_smtp, send_port, receive_user):
        flag = True
        try:
            msg = MIMEMultipart()
            # 构建正文
            mail_text = MIMEText('第一财经App1.0Android测试报告，请查收。', 'plain', 'utf-8')
            # 把正文加到邮件体里面去
            msg.attach(mail_text)
            path = os.getcwd() + '\\report'
            print(path)
            lists = os.listdir(path)  # 列出目录的下所有文件和文件夹保存到lists
            lists.sort(key=lambda fn: os.path.getctime(path + "\\" + fn), reverse=True)  # 创建时间升序
            file = os.getcwd() + '\\report\\' + lists[0]  # 取最新的文件并加上路径
            mail_file = MIMEApplication(open(file, 'rb').read())  # 打开附件
            mail_file.add_header('Content-Disposition', 'attachment', filename=pathlib.Path(file).name)  # 为附件命名
            msg.attach(mail_file)  # 添加附件

            # 发件人邮箱昵称、发件人邮箱账号
            msg['From'] = formataddr(["测试部门刘燚", send_user])
            # 收件人邮箱昵称、收件人邮箱账号
            msg['To'] = formataddr(["刘经理", receive_user])
            # 邮件的主题
            msg['Subject'] = "第一财经App1.0Android测试报告"

            # 发送邮箱按smtp配置
            server = smtplib.SMTP_SSL(send_smtp, send_port)
            # 登录服务器，括号中对应的是发件人邮箱账号、邮箱密码
            server.login(send_user, send_pw)
            # 发送邮件，括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.sendmail(send_user, [receive_user, ], msg.as_string())
            # 关闭连接
            server.quit()
            # 如果 try 中的语句没有执行，则会执行下面的 flag=False
        except Exception:
            flag = False
        return flag