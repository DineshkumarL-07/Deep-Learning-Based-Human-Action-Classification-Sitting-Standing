import os

def UserModelInput():
    while True:
        try:
            user_input1 = int(input("\nChoose the YOLO(You Only Look Once) Model Version that You want to Train on Your Data,\n\nThese are the Models Currently Available Choose Wisely\n1) YOLO 8 for efficiency and scalability\n2) YOLO 11 for accuracy and faster processing speed(Recommended)\n\nEnter the Model Version Number, or Option: "))
        except:
            print("\nInvalid Input! Try to provide the integer value\n")
            continue
            
        if user_input1 == 8 or user_input1 == 1:
            return "yolov8n.pt"
        
        elif user_input1 == 11:
            return "yolo11n.pt"

def getFilePathsForTraining():
    print("\nBe ready with the Train and Validation Dataset Folder Paths!!!")
    train_dir_path = input("\nEnter the Training Images and Labels Directory Path: ")
    val_dir_path = input("\nEnter the Validation Images and Labels Directory Path: ")
    user_input2 = input("\nDo You Want to Provide the Test Dataset Folder path|(It's Optional)(Yes/No): ").capitalize()
    test_dir_path = None
    if user_input2 == "Yes":
        test_dir_path = input("\nEnter the Test Images and Labels Directory Path: ")
    
    return [train_dir_path, val_dir_path, test_dir_path]

def getClassNames():
    no_of_classes = int(input("\nEnter the number of Class Names: "))
    class_names =  []
    for i in range(no_of_classes):
        c_name = input(f"Enter Class Name {i+1}: ")
        class_names.append(c_name)
    
    return class_names

def getTestImages():

    user_input3 = int(input("\nDo You Want Perform Test On,\n1) Single Image\n2) Multiple Images\nEnter the Option: "))
    if user_input3 == 1:
        img_path = input("\nEnter the Single Image File Path: ")
        return img_path
    
    elif user_input3 == 2:
        img_path = input("Enter the Images Folder Path: ")
        test_images = [os.path.join(img_path,f) for f in os.listdir(img_path) if f.endswith((".jpg",".png"))]
        return test_images

    else:
        print("\nInvalid option!!!, Try to give 1 or 2")
        return getTestImages()