import os

try:
    folders = []
    real_path = str(input("Enter File Path:  "))
    root_path = real_path.replace("\\", "/")

    print("[1] Number Series\n[2] Manual")
    choice = int(input("Enter Your Choice:  "))

    if choice == 1:
        i = int(input("Enter Starting Number of Folders:  "))
        num = int(input("Enter Last Number of Folders:  "))
        prifix = str(input("Enter folder prefix:  "))

        if prifix == "":
            suffix = str(input("Enter Suffix:  "))
            if suffix == "":
                while i != num+1:
                    folders.append(str(i))
                    i += 1
                for folder in folders:
                    os.mkdir(os.path.join(root_path,folder))
            else:
                while i != num+1:
                    folders.append(f"{str(i)} {suffix}")
                    i += 1
                for folder in folders:
                    os.mkdir(os.path.join(root_path,folder))
        else:
            while i != num+1:
                folders.append(f"{prifix} {str(i)}")
                i += 1
            for folder in folders:
                os.mkdir(os.path.join(root_path,folder))

    elif choice == 2:
        folder_name = input("Enter Folder Name:  ")
        folders.append(folder_name)
        while folder_name != "":
            folder_name = input("Enter Folder Name:  ")
            folders.append(folder_name)
        
        folders = folders[0:int(len(folders)-1)]
        for folder in folders:
            os.mkdir(os.path.join(root_path,folder))
    else:
        print("Wrong Input")
except Exception as e:
    print("Wrong File Path")
