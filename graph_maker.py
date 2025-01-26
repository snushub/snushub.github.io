import cairo
import sys


class GraphMaker:
    def __init__(self, line_t, file_n):
        self.white = (1.0, 1.0, 1.0)  # Scaled to [0, 1]
        self.black = (0.0, 0.0, 0.0)
        self.w = 600
        self.h = 400
        self.line_t = line_t
        self.line_c = (139 / 255.0, 0 / 255.0, 139 / 255.0)  # Scaled to [0, 1]
        self.fn = "assets/graphs/" + file_n
        self.start_pos = (10, 390)
        self.START = (10, 390)  # Do not overwrite
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
        self.context.set_source_rgb(81 / 255.0, 81 / 255.0, 81 / 255.0)
        ht = int(self.line_t / 2)
        self.context.move_to(self.min_x - ht, self.min_y + ht)
        self.context.line_to(self.min_x - ht, self.max_y + ht)
        self.context.line_to(self.max_x + ht, self.max_y + ht)
        self.context.stroke()

    def draw_curve(self, x1, y1, x2, y2, x3, y3):
        self.context.curve_to(x1, y1, x2, y2, x3, y3)

    def draw_line(self, x, y):
        self.context.move_to(*self.start_pos)  # Ensure valid start point
        self.context.line_to(x, y)

    def convert_y(self, y):
        return int(((10 - y) / 10) * 380 + 10)

    def set_points_and_draw(self, l, c):
        self.context.set_source_rgb(c[0] / 255.0, c[1] / 255.0, c[2] / 255.0)
        y = [self.convert_y(i) for i in l]
        coordinates = []
        x = int((self.lim_x - self.min_x) / (len(l) - 1))
        if len(l) - 1 == 1:
            self.lim_x = 250
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

    def exec(self, l: list, colors: list):
        if len(l) != len(colors):
            raise ValueError(
                "The length of the data list must match the length of the colors list."
            )
        self.setup()
        self.prep()
        for i, x in enumerate(l):
            self.start_pos = self.START
            self.set_points_and_draw(x, colors[i])
        self.export()


if __name__ == "__main__":
    gm = GraphMaker(8, "test.svg")
    y1 = [2, 4, 9, 2]
    y2 = [4, 10, 4]
    y3 = [3, 5, 8, 2]
    ll = [y1, y2, y3]
    royalblue = (65, 105, 225)
    sgi_chartreuse = (113, 198, 113)
    purple = (128, 0, 128)
    colors = [royalblue, purple, sgi_chartreuse]
    # gm.exec(ll, colors)
    gm.exec([[9, 2]], [purple])
    sys.exit()
