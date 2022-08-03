import random
import requests
import re
import os


class FourkBiZhi:
    def __init__(self):
        self.nametype = self.choicestype()  # 图片类型
        self.page = self.pagetxt()  # 页码 第一页为空 后面为html_x.html的形式表示
        self.url_orig = "https://www.4kbizhi.com/" + self.nametype + self.page
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/76.0.3809.100 Safari/537.36"}

    def request(self):  # 获取原始页面，找到图片地址
        responce = requests.get(url=self.url_orig, headers=self.headers)
        print(self.url_orig)
        # print(responce.text)
        return responce.text

    def filtration(self):  # 过滤出想要的图片地址fil_url
        fil = self.request()
        fil_url = re.findall("d/[a-zA-z]+[^\s]*.jpg", fil)
        print(fil_url)
        return fil_url

    def get_imgs(self):  # 返回真正想要下载图片的URL地址
        getimg = self.filtration()
        # print(getimg)
        for i in getimg:
            tru_url = "https://www.4kbizhi.com/" + i
            print("-----.>！！下载完成！！<.------")
            responces = requests.get(url=tru_url, headers=self.headers)
            img = responces.content  # 下载我们需要的图片
            # 给图片编号
            w = str(i[34:44])
            with open(r'D:\爬取的图片\pic' + w + ".jpg", "wb") as f:
                f.write(img)
            print(f)
            print("已全部保存在你的文件中")

    def choicestype(self):  # 选择图片分类
        nametype = input("""
                    请输入抓取图片的类型
                      1.动漫
                      2.风景
                      3.跑车
                      4.萌物
                      5.系统
                      6.游戏
                      7.影视
                      8.美女
    你可以输入相对应的数字或名字：
                      """)
        if nametype == "动漫" or nametype == "1":
            nametype = "donman"
        elif nametype == "风景" or nametype == "2":
            nametype = "fengjing"
        elif nametype == "跑车" or nametype == "3":
            nametype = "paoche"
        elif nametype == "萌物" or nametype == "4":
            nametype = "mengwu"
        elif nametype == "系统" or nametype == "5":
            nametype = "xitong"
        elif nametype == "游戏" or nametype == "6":
            nametype = "youxi"
        elif nametype == "影视" or nametype == "7":
            nametype = "yingshi"
        elif nametype == "美女" or nametype == "8":
            nametype = "meinv"
        else:
            nametype = ""
        return nametype

    def pagetxt(self):  # 手动获取页码
        page = input("请输入页码数字：")
        html = "/index_" + page + ".html"
        if page == "1":
            html = ""
        return html

    def again(self):
        aga = input("你还要爬取图片吗？yes / no？")
        while True:
            if aga == "yes":
                picdown = FourkBiZhi()
                picdown.main()
            elif aga == "no":

                a = input("按q键退出！！！")
                if a == "q":
                    exit()
                else:
                    print("你是来找茬的是吧？")
                    self.again()
            else:
                print("你的输入不对")
                self.again()

    def main(self):
        try:
            os.mkdir("D:/爬取的图片")
            self.get_imgs()
            self.again()
        except  Exception:
            print("文件夹存在")
            self.get_imgs()
            self.again()


if __name__ == '__main__':
    try:
        picdown = FourkBiZhi()
        picdown.main()
    except Exception as err:
        print(err)
