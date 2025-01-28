import cairo
import sys
import os


class GraphMaker:
    def __init__(self, line_t, file_n, snus_name):
        self.white = (1.0, 1.0, 1.0)  # Scaled to [0, 1]
        self.black = (0.0, 0.0, 0.0)
        self.gray = (51 / 255.0, 51 / 255.0, 51 / 255.0)
        self.w = 600
        self.h = 400
        self.line_t = line_t
        self.line_c = (139 / 255.0, 0 / 255.0, 139 / 255.0)  # Scaled to [0, 1]
        self.fn = "/Users/lord/programming/snushub.github.io/assets/graphs/" + file_n
        self.snus_name = snus_name
        self.start_pos = (10, 390)
        self.START = (13, 387)  # Do not overwrite
        self.min_x = 10
        self.max_x = self.w - 10
        self.min_y = 10
        self.max_y = self.h - 10
        self.lim_x = 410

    def export(self):
        self.surface.finish()
        print("Written to " + self.fn)

    def setup(self):
        self.surface = cairo.SVGSurface(self.fn, self.w, self.h)
        self.context = cairo.Context(self.surface)

        self.context.set_source_rgb(*self.white)  # Background
        self.context.paint()
        self.context.set_source_rgb(*self.line_c)
        self.context.set_line_width(self.line_t)
        self.context.set_line_join(cairo.LINE_JOIN_ROUND)
        self.context.set_antialias(cairo.ANTIALIAS_BEST)

    def prep(self):
        self.context.set_source_rgb(*self.gray)
        ht = -2
        self.context.move_to(self.min_x - ht, self.min_y + ht)
        self.context.line_to(self.min_x - ht, self.max_y + ht)  # Y-axis
        self.context.line_to(self.max_x + ht, self.max_y + ht)  # X-axis
        self.context.stroke()

        # Add arrow for the Y-axis
        arrow_size = 10
        self.context.move_to(self.min_x - ht - arrow_size, self.min_y + ht + arrow_size)
        self.context.line_to(self.min_x - ht, self.min_y + ht)  # Arrowhead
        self.context.line_to(self.min_x - ht + arrow_size, self.min_y + ht + arrow_size)
        self.context.stroke()

        # Add arrow for the X-axis
        self.context.move_to(self.max_x + ht - arrow_size, self.max_y + ht - arrow_size)
        self.context.line_to(self.max_x + ht, self.max_y + ht)  # Arrowhead
        self.context.line_to(self.max_x + ht - arrow_size, self.max_y + ht + arrow_size)
        self.context.stroke()

        # Add text labels for axes
        self.context.select_font_face(
            "Poppins", cairo.FontSlant.NORMAL, cairo.FontWeight.NORMAL
        )
        self.context.set_font_size(16)
        self.context.set_source_rgb(*self.gray)

        # Add "hit" next to the Y-arrow
        y_label = "hit"
        y_extents = self.context.text_extents(y_label)
        y_x_pos = self.min_x + y_extents.width  # Slightly offset to the right
        y_y_pos = self.min_y + arrow_size + 5  # Below the Y-arrow tip
        self.context.move_to(y_x_pos, y_y_pos)
        self.context.show_text(y_label)

        # Add "time" above the X-arrow
        x_label = "time"
        x_extents = self.context.text_extents(x_label)
        x_x_pos = self.max_x - x_extents.width - 5  # Slightly offset to the left
        x_y_pos = self.max_y - arrow_size - 10  # Above the X-arrow tip
        self.context.move_to(x_x_pos, x_y_pos)
        self.context.show_text(x_label)

    def draw_curve(self, x1, y1, x2, y2, x3, y3):
        self.context.curve_to(x1, y1, x2, y2, x3, y3)

    def draw_line(self, x, y):
        self.context.move_to(*self.start_pos)  # Ensure valid start point
        self.context.line_to(x, y)

    def convert_y(self, y):
        return int(((10 - y) / 10) * 380 + 10)

    def set_points_and_draw(self, l, c, hr):
        self.context.set_source_rgb(c[0] / 255.0, c[1] / 255.0, c[2] / 255.0)
        y = [self.convert_y(i) for i in l]
        coordinates = []

        x = int((self.lim_x - self.min_x) / (len(l) - 1))

        if len(l) - 1 == 1:
            self.lim_x = 250
        elif len(l) - 1 == 2:
            self.lim_x = 310
        if hr != 0:
            self.lim_x = hr

        xoff = self.min_x
        for i in y[:-1]:
            offset = int(x / 2)
            px = xoff + offset
            coordinates.append((px, i))
            xoff += x

        coordinates.append((int((self.max_x - self.lim_x) / 2) + self.lim_x, y[-1]))

        self.context.move_to(*self.start_pos)

        for c in coordinates:
            x3, y3 = c
            x0, y0 = self.start_pos
            mid_x = int((x3 - x0) / 2)
            if y0 > y3:
                y1 = y3 + int(abs(y0 - y3) * 0.95)
                y2 = y3 + int(abs(y0 - y3) * 0.05)
                x1 = mid_x + x0 + int(mid_x / 2)
                x2 = mid_x + x0 - int(mid_x / 2)
            else:
                y1 = y0 + int(abs(y0 - y3) * 0.05)
                y2 = y0 + int(abs(y0 - y3) * 0.95)
                x1 = mid_x + x0 + int(mid_x / 2)
                x2 = mid_x + x0 - int(mid_x / 2)

            self.context.curve_to(x1, y1, x2, y2, x3, y3)
            self.start_pos = (x3, y3)

        line_y = max(self.min_y, min(self.max_y, int(coordinates[-1][1] * 1.02)))
        self.draw_line(self.max_x - 10, line_y)

        self.context.stroke()

    def add_snus_name(self):
        self.context.select_font_face(
            "Poppins", cairo.FontSlant.NORMAL, cairo.FontWeight.NORMAL
        )
        self.context.set_font_size(17)
        self.context.set_source_rgb(*self.gray)
        text = self.snus_name
        right_boundary = self.max_x - 5
        extents = self.context.text_extents(text)
        text_width = extents.width
        x_pos = right_boundary - text_width

        self.context.move_to(x_pos, self.min_y * 5)
        self.context.show_text(self.snus_name)

    def exec(self, l: list, colors: list, h_range: list):
        if len(l) != len(colors) != len(h_range):
            raise ValueError(
                "The length of the data list must match the length of the colors list."
            )
        self.setup()

        if len(l) == 1:
            self.add_snus_name()
        for i, x in enumerate(l):
            self.start_pos = self.START
            self.set_points_and_draw(x, colors[i], h_range[i])

        self.prep()
        self.export()


if __name__ == "__main__":
    ### Usage for multiple graphs: #######
    # y1 = [2, 4, 9, 2]
    # y2 = [4, 10, 4]
    # y3 = [3, 5, 8, 2]
    # ll = [y1, y2, y3]
    # royalblue = (65, 105, 225)
    # sgi_chartreuse = (113, 198, 113)
    # purple = (128, 0, 128)
    # colors = [royalblue, purple, sgi_chartreuse]
    # gm.exec(ll, colors)
    #######################################
    ## Single graph: #############
    # gm.exec([[9, 2]], [purple])
    ##############################
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

    gm = GraphMaker(8, "nois_extreme_cool.svg", "Nois Extreme Cool")
    y = [4.5, 3]
    # self.lim_x = 410
    # If you do not want to change the range, then hr => 0
    gm.exec([y], [dodger_blue], [5])

    sys.exit()
