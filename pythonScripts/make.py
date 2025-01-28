import graph_maker
import page_builder_new
import json


class Make:
    def __init__(self):
        self.json_path = (
            "Users/lord/programming/snushub.github.io/usefulFiles/snus_data.json"
        )

    def parse_json(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            print(data)
            print(data["key"])


if __name__ == "__main__":
    m = Make()
