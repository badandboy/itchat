#-*-coding:utf8-*-

import itchat


#登录时打印login in
def login_in():
    print("login in")


#退出时打印login out
def login_out():
    print("login out")


#发送文本信息，参数文本内容，发送给谁
def send_msg(msg,to_user_name=None):
    return itchat.send(msg, toUserName=to_user_name)


#发送图片，参数图片地址，发送给谁
def send_image(image_url, to_user_name=None):
    return itchat.send_image(image_url, toUserName=to_user_name)


#发送文件，参数文件地址，发送给谁
def send_file(file_url,to_user_name=None):
    return itchat.send_file(file_url, toUserName=to_user_name)


#发送视频，参数视频地址，发送给谁
def send_video(video_url, to_user_name=None):
    return itchat.send_video(video_url, toUserName=to_user_name)


itchat.auto_login(loginCallback=login_in(), exitCallback=login_out(), hotReload=True)
# itchat.auto_login(loginCallback=login_in(), exitCallback=login_out(), hotReload=True,enableCmdQR=2)


#查询需要发送的好友，搜索的为微信备注，不是好友的昵称
def send_news():
    to_user_name = "李狗蛋"
    itchat_user_name = itchat.search_friends(name=to_user_name)

    print(itchat_user_name)

    if len(itchat_user_name) > 0:
        itchat_user_name = itchat_user_name[0]['UserName']
        for i in range(0,10):
            print(send_msg("txt content",itchat_user_name))
            print(send_file("1.txt",itchat_user_name))
            print(send_image("1.jpg",itchat_user_name))
            print(send_video("Sugar - Maroon 5.mp4",itchat_user_name))
    else:
        print("not find the userName")


def main():
    send_news()


if __name__ == '__main__':
    main()
