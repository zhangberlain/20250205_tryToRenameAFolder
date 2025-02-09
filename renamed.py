import os 
def rename_images():
    #得到文件夹路径
    folder_path = input('请输入图片文件夹').strip()
    
    #验证路径有效性
    if not os.path.isdir(folder_path):
        print('文件夹路径输入有误')
        return 

    files = [fi for fi in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,fi))]
    if not files:
        print('无文件')
        return
    
    new_names = []
    counter = 1001
    conflict_files = []   

    # 预检查目标文件名冲突
    new_names = []
    counter = 1001
    conflict_files = []
    
    for file in files:
        _, ext = os.path.splitext(file)
        new_name = f"{counter}{ext}"
        new_path = os.path.join(folder_path, new_name)
        
        if os.path.exists(new_path):
            conflict_files.append(new_name)
        
        new_names.append(new_name)
        counter += 1

    if conflict_files:
        print("发现以下目标文件名已存在，请处理后重试：")
        for name in conflict_files:
            print(f"• {name}")
        return
    
    # 用户确认
    print(f"找到 {len(files)} 个文件，将按以下顺序重命名：")
    for old, new in zip(files, new_names):
        print(f"{old} → {new}")
    
    confirm = input("\n是否继续？(y/n): ").lower()
    if confirm != 'y':
        print("操作已取消。")
        return
    
    # 执行重命名操作
    for old_file, new_name in zip(files, new_names):
        old_path = os.path.join(folder_path, old_file)
        new_path = os.path.join(folder_path, new_name)
        
        try:
            os.rename(old_path, new_path)
            print(f"成功：{old_file} → {new_name}")
        except Exception as e:
            print(f"错误：重命名 {old_file} 失败 - {str(e)}")
            return
        
if __name__ == "__main__":
    rename_images()