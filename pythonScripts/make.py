import graph_maker
import page_builder_new
import json


class Make:
    def __init__(self):
        self.json_path = (
            "/Users/lord/programming/snushub.github.io/usefulFiles/snus_data.json"
        )
        self.data = []  # all the content from snus_data.json
        self.color_list = {}

    def get_json_data(self):
        with open(self.json_path, "r") as file:
            self.snus_data = json.load(file)

    def make(self):
        for snus in self.snus_data:
            self.snus_name = snus.get("name")
            self.graph_data = snus.get("graph_data")
            # call create_graph

            # call create_page

    def create_graph(self, fn):
        pass

    def create_page(self):
        pass


if __name__ == "__main__":
    m = Make()
    m.get_json_data()
    m.make()
