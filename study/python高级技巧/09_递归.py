"""
演示Python递归操作
需求：通过递归，找出一个指定文件夹的全部内容，如果是文件就收集到list
如果是文件夹，就递归调用自己，再次判断
"""
import os


def ostest_os():
    """演示os模块的三个基础功能"""
    print(os.listdir('F:/pythonProject/data_development/data_input'))                   # 列出路径下的文件夹,返回一个list
    print(os.path.isdir('F:/pythonProject/data_development/data_input/Spark案例'))       # 判断路径是不是文件夹
    print(os.path.exists('F:/pythonProject/data_development/data_input/数据分析案例'))     # 判断指定路径是否存在

def get_files_from_dir(path):
    """
    从指定的文件夹中使用递归的方式，获取全部的文件列表
    :param path: 被判断的文件夹
    :return: list，包含全部的文件，如果目录不存在或者无文件就返回一个空list
    """
    file_list=[]
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path=path + '/' + f
            if os.path.isdir(new_path):
                file_list+=get_files_from_dir(new_path)
            else:
                file_list.append(new_path)

    else:
        print(f'指定目录：{path}不存在')
        return []

    return file_list



if __name__=='__main__':
    # ostest_os()
    print(get_files_from_dir('F:/pythonProject/data_development/data_input'))