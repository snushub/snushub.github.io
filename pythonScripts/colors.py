import random


class Colors:
    def __init__(self):
        self.colors = [
            (220, 20, 60),  # crimson_red
            (0, 191, 255),  # deep_sky_blue
            (50, 205, 50),  # lime_green
            (255, 215, 0),  # gold
            (255, 105, 180),  # hot_pink
            (255, 140, 0),  # dark_orange
            (147, 112, 219),  # medium_purple
            (0, 255, 255),  # cyan
            (127, 255, 0),  # chartreuse
            (255, 0, 255),  # magenta
            (255, 20, 147),  # deep_pink
            (255, 69, 0),  # orange_red
            (30, 144, 255),  # dodger_blue
            (0, 255, 127),  # spring_green
            (255, 255, 0),  # yellow
            (218, 112, 214),  # orchid
            (255, 99, 71),  # tomato
            (64, 224, 208),  # turquoise
            (60, 179, 113),  # medium_sea_green
            (244, 164, 96),  # sandy_brown
            (240, 248, 255),  # alice_blue
            (250, 235, 215),  # antique_white
            (127, 255, 212),  # aquamarine
            (240, 255, 255),  # azure
            (245, 245, 220),  # beige
            (255, 228, 196),  # bisque
            (0, 0, 0),  # black
            (255, 235, 205),  # blanched_almond
            (0, 0, 255),  # blue
            (138, 43, 226),  # blue_violet
            (165, 42, 42),  # brown
            (222, 184, 135),  # burly_wood
            (95, 158, 160),  # cadet_blue
            (210, 105, 30),  # chocolate
            (255, 127, 80),  # coral
            (100, 149, 237),  # cornflower_blue
            (255, 248, 220),  # cornsilk
            (0, 0, 139),  # dark_blue
            (0, 139, 139),  # dark_cyan
            (184, 134, 11),  # dark_goldenrod
            (169, 169, 169),  # dark_gray
            (0, 100, 0),  # dark_green
            (189, 183, 107),  # dark_khaki
            (139, 0, 139),  # dark_magenta
            (85, 107, 47),  # dark_olive_green
            (153, 50, 204),  # dark_orchid
            (139, 0, 0),  # dark_red
            (233, 150, 122),  # dark_salmon
            (143, 188, 143),  # dark_sea_green
            (72, 61, 139),  # dark_slate_blue
            (47, 79, 79),  # dark_slate_gray
            (0, 206, 209),  # dark_turquoise
            (148, 0, 211),  # dark_violet
            (105, 105, 105),  # dim_gray
            (178, 34, 34),  # firebrick
            (255, 250, 240),  # floral_white
            (34, 139, 34),  # forest_green
            (255, 0, 255),  # fuchsia
            (220, 220, 220),  # gainsboro
            (248, 248, 255),  # ghost_white
            (218, 165, 32),  # goldenrod
            (128, 128, 128),  # gray
            (0, 128, 0),  # green
            (173, 255, 47),  # green_yellow
            (240, 255, 240),  # honeydew
            (205, 92, 92),  # indian_red
            (75, 0, 130),  # indigo
            (255, 255, 240),  # ivory
            (240, 230, 140),  # khaki
            (230, 230, 250),  # lavender
        ]

        random.seed(42)

    def get_color_at_index(self, i):
        return self.colros[i]

    def get_random_color(self):
        return random.choice(self.colors)
