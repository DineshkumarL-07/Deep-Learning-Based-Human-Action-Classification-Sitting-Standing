import yaml
import os

def createYamlFile(file_paths, class_names):

    data = {}

    if file_paths[-1] == None:
        data = {
            "train" : file_paths[0],
            "val" : file_paths[1]
        }
    else:
        data = {
            "train" : file_paths[0],
            "val" : file_paths[1],
            "test" : file_paths[2]
        }
    
    data["nc"] = len(class_names)
    data["names"] = class_names

    yaml_filename = "data.yaml"
    with open(yaml_filename, "w") as file:
        yaml.dump(data, file, default_flow_style=False)

    yaml_path = os.path.abspath(yaml_filename)
    
    return [yaml_filename, yaml_path]
