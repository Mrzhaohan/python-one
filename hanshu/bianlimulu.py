import os
def blfp(path):
    file_name_list=os.listdir(path)
    for file_name in file_name_list:
        file_path_name=os.path.join(path,file_name)
        if os.path.isfile(file_path_name):
            print(file_path_name)
        else:
            blfp(file_path_name)
    return None

if __name__=='__main__':
    blfp('/root/python')
