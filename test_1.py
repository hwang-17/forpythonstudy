def save_file(boy, girl, count):
    file_name_boy = "boy_" + str(count) + ".txt"
    file_name_girl = "girl_" + str(count) + ".txt"

    boy_file = open(file_name_boy, "w")
    girl_file = open(file_name_girl, "w")

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()
def split_file (file_name):
    f=open(file_name, encoding="gbk")

    # 创建两个列表分别储存两个人的对话
    boy = []
    girl = []
    count=1
    for each_line in f:
        if each_line[:6] != "======":
            # 我们在这里进行字符分割操作
            (role, line_spoken)=each_line.split(":", 1)
            if role == "小甲鱼":
                boy.append(line_spoken)
            if role == "小客服":
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)

            boy=[]
            girl=[]
            count += 1

    save_file(boy,girl,count)

    f.close()

split_file("record.txt")
#         文件的分别保存操作
