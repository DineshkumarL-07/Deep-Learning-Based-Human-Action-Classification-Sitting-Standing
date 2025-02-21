from user_view_utility import UserModelInput,getFilePathsForTraining,getClassNames
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
        self.isModelTrained = False
    
    def changeStatus(self):
        self.isModelTrained = True
        return self.isModelTrained


class Model:
    model = None
    
    def trainModel(self):
        pass

    def fineTuneModel(self):
        pass

    def returnModel(self):
        return Model.model



if __name__ == '__main__':

    print("\t\t\t\tWelcome To Sporada Secure\n")
    while True:

        try:
            first_input = int(input("There are the Operation Available:\n1) Train the YOLO Model\n2) Test the YOLO model use Test data\n3) Check Model Status\n4) Fine Tuning the model/ Re-Train Using the Other dataset\n5)Exit\nEnter the Operation You Want to Perform: "))
        except ValueError:
            print("Invalid Input! Try to provide the integer value\n")
            continue

        if first_input == 1:
            if not ModelState.checkStatus().isModelTrained:
                model_version = UserModelInput()
                file_paths = getFilePathsForTraining()
                class_names = getClassNames()
                continue
            else:
                print("\nModel is already trained! Try to use other operation")
                continue

        elif first_input == 2:
            pass
            continue


        elif first_input == 3:
            pass
            continue

        elif first_input == 4:
            if not ModelState.checkStatus().isModelTrained:
                print("Model is not trained Yet")
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