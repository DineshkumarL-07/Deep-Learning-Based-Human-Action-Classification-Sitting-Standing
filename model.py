from user_view_utility import UserModelInput,getFilePathsForTraining,getClassNames,getTestImages
from create_yaml import createYamlFile
from ultralytics import YOLO
import cv2
import os

class ModelState:
    instance = None

    @staticmethod
    def checkStatus():
        if not ModelState.instance:
            ModelState.instance = ModelState()
        return ModelState.instance

    def __init__(self):
        self.isModelTrained: bool = False

class Model:

    def __init__(self,model_version):
        obj = ModelState.checkStatus()
        obj.isModelTrained = True
        self.status = obj.isModelTrained
        self.version: str = model_version
        self.model = YOLO(model_version)
        self.class_names = []
    
    def trainModel(self,file_paths, class_names):
        self.class_names = class_names
        self.yaml_status: list = createYamlFile(file_paths, class_names)

        print(f"\nYAML File Named {self.yaml_status[0]} Created Successfully at {self.yaml_status[1]}")
        self.epoch = int(input(f"\nEnter the Number of Epochs, You want to perform for this model -> {self.version}: "))

        print("\n Model is Started Training !!")
        self.model_filename = input("Enter the model filename to save the model (like: detection): ")

        self.model.train(data=self.yaml_status[1], epochs = self.epoch, imgsz = 640)
        self.model.save(f"{self.model_filename}.pt")

        print(f"Model is Trained Successfully and Saved at {os.path.abspath(self.model_filename + '.pt')}")

    def testModel(self,test_images):
        for img in test_images:
            image = cv2.imread(img)
            model = YOLO(r"D:\Anomaly programs\Model_4_Sitting_and_Standing_Detection\Deep-Learning-Based-Human-Action-Classification-Sitting-Standing\model_yolo11n_sit_stand.pt")
            self.results = model(image)

            for result in self.results:
                for box in result.boxes:
                    cls = int(box.cls[0])
                    label = self.model.names[cls]

                    if label in self.class_names:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        conf = float(box.conf[0])

                        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cv2.putText(image, f"{label} ({conf:.2f}", 
                            (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                            0.5, (0, 0, 255), 2)
                        
            cv2.imshow("Detected Output", image)
            cv2.waitKey(0)  
            cv2.destroyAllWindows()
        
        print("\nYour Test Detections are Completed.")

    def fineTuneModel(self):
        pass

    def returnModel(self):
        return Model.model



if __name__ == "__main__":

    print("\t\t\t\tWelcome To Human Action Detection\n")
    while True:

        try:
            first_input = int(input("There are the Operation Available:\n1) Train the YOLO Model\n2) Test the YOLO model using Test data\n3) Check Model Status\n4) Fine Tuning the model/ Re-Train Using the Other dataset\n5) Exit\nEnter the Operation You Want to Perform: "))
        except ValueError:
            print("Invalid Input! Try to provide the integer value\n")
            continue

        model_obj = None
        if first_input == 1:
            if not ModelState.checkStatus().isModelTrained:
                model_version = UserModelInput()
                file_paths = getFilePathsForTraining()
                class_names = getClassNames()
                model_obj = Model(model_version)
                model_obj.trainModel(file_paths, class_names)
                continue
            else:
                print("\nModel is already trained! Try to use other operation")
                continue

        elif first_input == 2:
            test_images = getTestImages()
            Model.testModel(model_obj,test_images)
            continue

        elif first_input == 3:
            if not model_obj.status:
                print("Model is Not Trained Yet!, Try to Go with Option 1")
            else:
                print("Model is Already Trained")

        elif first_input == 4:
            if not ModelState.getStatus():
                print("Model is Not Trained Yet!, Try to Go with Option 1")
            else:
                print("\nOkay you can go to training process")
                continue

        elif first_input == 5:
            break

        else:
            toContinue = input("Invalid Operation!, Do you Want to Continue? (Yes/No): ").capitalize()
            if toContinue == 'Yes':
                continue
            else:
                break