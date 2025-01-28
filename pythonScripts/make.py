import graph_maker
import page_builder_new
import json


class Make:
    def __init__(self):
        self.json_path = (
            "/Users/lord/programming/snushub.github.io/usefulFiles/snus_data.json"
        )
        self.data = []  # all the content from snus_data.json

    def get_json_data(self):
        with open(self.json_path, "r") as file:
            self.data = json.load(file)

    def print_data(self):
        # how to access data
        d = self.data[1]
        print(d["name"])

    def create_graph(self):
        pass

    def create_page(self):
        pass


if __name__ == "__main__":
    m = Make()
    m.get_json_data()
    m.print_data()
