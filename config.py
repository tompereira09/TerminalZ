import json

contents = open("manifest.json", "r").read()

jc = json.loads(contents)

class Config:
    def get_path(self):
        std_path = jc["std_path"]
        return std_path

    def get_version(self):
        version = jc["version"]
        return version
