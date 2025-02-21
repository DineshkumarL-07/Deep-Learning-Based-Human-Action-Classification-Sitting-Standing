import os
import yaml

def createYamlFile(file_paths):

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

    yaml_filename = "data.yaml"
    with open(yaml_filename, "w") as file:
        yaml.dump(data, file, default_flow_style=False)

    yaml_path = os.path.abspath(yaml_filename)
    
    return [yaml_filename, yaml_path]

path = ["1", "2", None]
print(createYamlFile(path))

