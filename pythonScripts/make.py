import graph_maker
import page_builder_new
import json
import colors as c


class Make:
    def __init__(self):
        self.json_path = (
            "/Users/lord/programming/snushub.github.io/usefulFiles/snus_data.json"
        )
        self.data = []  # all the content from snus_data.json
        self.color_list = {}
        self.color_picker = c.Colors()

    def get_json_data(self):
        with open(self.json_path, "r") as file:
            self.snus_data = json.load(file)

    def make(self):
        for snus in self.snus_data:
            # call create_graph
            color = self.color_picker.get_random_color()
            self.create_graph(snus, color)
            # call create_page

            self.create_page(snus)

    def create_graph(self, sn, c):
        gm = graph_maker.GraphMaker(8, sn.get("graph_path"), sn.get("name"))
        gm.exec([sn.get("graph_data")], [c], [sn.get("h_range")])

    def create_page(self, sn):
        xs = page_builder_new.PageBuilderNew(
            sn.get("name"),
            sn.get("image_path"),
            sn.get("graph_path"),
            sn.get("page_path"),
            sn.get("overall_rating"),
            sn.get("nicotine"),
            sn.get("quantity"),
            sn.get("price"),
            sn.get("hit_strength"),
            sn.get("hit_quality"),
            sn.get("taste"),
            sn.get("smell"),
            sn.get("drip_taste"),
            sn.get("design"),
            sn.get("pouch_size"),
            sn.get("reusability"),
            sn.get("aura"),
            sn.get("recommendation"),
        )
        xs.load_and_replace_template()
        xs.add_link_to_page_index()


if __name__ == "__main__":

    m = Make()
    m.get_json_data()
    m.make()
