class PageBuilderNew:
    def __init__(
        self,
        snus_name,
        img_filename,
        svg_filename,
        filename,
        overall,
        nicotine,
        quantity,
        price,
        hit_s,
        hit_q,
        taste,
        smell,
        drip_taste,
        design,
        pouch_size,
        reusability,
        aura,
        recommendation,
    ):
        self.filename = str(filename)
        self.snus_name = str(snus_name)
        self.page_title = self.snus_name.lower().replace(" ", "-")
        self.img_filename = str(img_filename)
        self.img_filename_svg = str(svg_filename)
        self.overall_rating = str(overall)
        self.i_p = str(float(self.overall_rating) * 10)
        self.overlay_w = str(100 - float(self.i_p))
        self.nicotine = str(nicotine)
        self.quantity = str(quantity)
        self.price = str(price)
        self.hit_s = str(float(hit_s) * 10)
        self.taste = str(float(taste) * 10)
        self.smell = str(float(smell) * 10)
        self.hit_q = str(float(hit_q) * 10)
        self.drip_t = str(float(drip_taste) * 10)
        self.design = str(float(design) * 10)
        self.pouch_size = pouch_size
        self.reusability = str(reusability)
        self.aura = str(aura)
        self.recommendation = str(recommendation)

        self.data = dict(
            page_title=self.page_title,
            snus_name=self.snus_name,
            img_filename=self.img_filename,
            img_filename_svg=self.img_filename_svg,
            indicator_percentage=self.i_p,
            overlay_width=self.overlay_w,
            nicotine=self.nicotine,
            quantity=self.quantity,
            price=self.price,
            hit_strength=self.hit_s,
            taste=self.taste,
            smell=self.smell,
            hit_quality=self.hit_q,
            drip_taste=self.drip_t,
            design=self.design,
            pouch_size=self.pouch_size,
            reusability=self.reusability,
            aura=self.aura,
            recommendation=self.recommendation,
        )

    def load_and_replace_template(self):
        with open(
            "/Users/lord/programming/snushub.github.io/assets/templates/first_template.txt",
            "r",
        ) as file:
            template = file.read()
        # Inject the content into the template
        html_content = template.format(**self.data)

        # Save the result to a new HTML file
        self.output_file = (
            "/Users/lord/programming/snushub.github.io/snusRatingPages/" + self.filename
        )
        with open(self.output_file, "w") as file:
            file.write(html_content)

        print(f"Page has been created successfully!")

    def add_link_to_page_index(self):
        injection = (
            '<a href="'
            + "snusRatingPages/"
            + self.filename
            + '" class="link-wrapper"> <div class="snus-box-main">'
        )
        injection += "<h3>" + self.snus_name + "</h3>"
        injection += (
            '<img src="'
            + "assets/tegel/"
            + self.img_filename
            + '" class="fullscreen-image"></div> </a>'
        )

        with open(
            "/Users/lord/programming/snushub.github.io/index.html",
            "r",
            encoding="utf-8",
        ) as file:
            self.index_html_content = file.read()

        home_page = self.index_html_content.find('class="home-page">') + len(
            'class="home-page">'
        )

        new_html_content = (
            self.index_html_content[:home_page]
            + injection
            + self.index_html_content[home_page:]
        )
        with open(
            "/Users/lord/programming/snushub.github.io/index.html",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(new_html_content)


if __name__ == "__main__":
    xs = PageBuilderNew()
    xs.load_and_replace_template()
    xs.add_link_to_page_index()
