import os
import json


class Storage:
    def __init__(self):
        pass

    # check file exist
    def check_file_exist(self, file_path):
        return os.path.exists(file_path)
    
    # read json file and return the content
    def read_json_file(self, file_path):
        if not self.check_file_exist(file_path):
            print(f"The file {file_path} does not exist.")
            return None
        # check is json file
        if not file_path.endswith('.json'):
            print(f"The file {file_path} is not a JSON file.")
            return None
        
        with open(file_path, 'r') as file:
            return json.load(file)
    
    # write data to json file
    def write_json_file(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file)

    # get system message from config
    def get_system_message(self):
        data = self.read_json_file("config/system.json")
        if data is None:
            return []
        return data["system_init"]
    
    # get history message from tmp/history.json
    def get_history_message(self):
        data = self.read_json_file("tmp/history.json")
        if data is None:
            return []
        return data["history_messages"]
    
    # save history message to tmp/history.json
    def save_history_message(self, history_messages):
        data = {
            "history_messages": history_messages
        }
        self.write_json_file("tmp/history.json", data)

# Example usage
if __name__ == "__main__":
    file_handle = Storage()
    file_path = "test.json"
    data = {
        "name": "John",
        "age": 30
    }
    file_handle.write_json_file(file_path, data)
    print(file_handle.read_json_file(file_path))