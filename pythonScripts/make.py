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

    def make(self, color, h_range):
        self.color = color
        self.h_range = h_range
        for snus in self.snus_data:
            # call create_graph
            self.create_graph(snus)
            # call create_page

            self.create_page(snus)

    def create_graph(self, sn):
        gm = graph_maker.GraphMaker(8, sn.get("graph_path"), sn.get("name"))
        gm.exec([sn.get("graph_data")], [self.color], [self.h_range])

    def create_page(self, sn):
        xs = page_builder_new.PageBuilderNew(
            sn.get("name"),
            sn.get("image_path"),
            xs.get("graph_path"),
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
    crimson_red = (220, 20, 60)
    deep_sky_blue = (0, 191, 255)
    lime_green = (50, 205, 50)
    gold = (255, 215, 0)
    hot_pink = (255, 105, 180)
    dark_orange = (255, 140, 0)
    medium_purple = (147, 112, 219)
    cyan = (0, 255, 255)
    chartreuse = (127, 255, 0)
    magenta = (255, 0, 255)
    deep_pink = (255, 20, 147)
    orange_red = (255, 69, 0)
    dodger_blue = (30, 144, 255)
    spring_green = (0, 255, 127)
    yellow = (255, 255, 0)
    orchid = (218, 112, 214)
    tomato = (255, 99, 71)
    turquoise = (64, 224, 208)
    medium_sea_green = (60, 179, 113)
    sandy_brown = (244, 164, 96)

    alice_blue = (240, 248, 255)
    antique_white = (250, 235, 215)
    aquamarine = (127, 255, 212)
    azure = (240, 255, 255)
    beige = (245, 245, 220)
    bisque = (255, 228, 196)
    black = (0, 0, 0)
    blanched_almond = (255, 235, 205)
    blue = (0, 0, 255)
    blue_violet = (138, 43, 226)
    brown = (165, 42, 42)
    burly_wood = (222, 184, 135)
    cadet_blue = (95, 158, 160)
    chocolate = (210, 105, 30)
    coral = (255, 127, 80)
    cornflower_blue = (100, 149, 237)
    cornsilk = (255, 248, 220)
    dark_blue = (0, 0, 139)
    dark_cyan = (0, 139, 139)
    dark_goldenrod = (184, 134, 11)
    dark_gray = (169, 169, 169)
    dark_green = (0, 100, 0)
    dark_khaki = (189, 183, 107)
    dark_magenta = (139, 0, 139)
    dark_olive_green = (85, 107, 47)
    dark_orchid = (153, 50, 204)
    dark_red = (139, 0, 0)
    dark_salmon = (233, 150, 122)
    dark_sea_green = (143, 188, 143)
    dark_slate_blue = (72, 61, 139)
    dark_slate_gray = (47, 79, 79)
    dark_turquoise = (0, 206, 209)
    dark_violet = (148, 0, 211)
    dim_gray = (105, 105, 105)
    firebrick = (178, 34, 34)
    floral_white = (255, 250, 240)
    forest_green = (34, 139, 34)
    fuchsia = (255, 0, 255)
    gainsboro = (220, 220, 220)
    ghost_white = (248, 248, 255)
    goldenrod = (218, 165, 32)
    gray = (128, 128, 128)
    green = (0, 128, 0)
    green_yellow = (173, 255, 47)
    honeydew = (240, 255, 240)
    indian_red = (205, 92, 92)
    indigo = (75, 0, 130)
    ivory = (255, 255, 240)
    khaki = (240, 230, 140)
    lavender = (230, 230, 250)
    m = Make()
    m.get_json_data()
    m.make(honeydew, 5)
