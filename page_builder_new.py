class PageBuilderNew:
    def __init__(self):
        self.full_page_content = """
        <!DOCTYPE html>
        <html lang="de">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Snus-Hub</title>
            <link rel="stylesheet" href="../styles.css">
        </head>

        <body>

            <header>
                <a class="link-wrapper" href="../index.html">
                    <img src="../assets/logos/snus_hub_logo.JPG" class="fullscreen-image">
                </a>
            </header>

            <main>

                <div class="snus-box">
                    <h3>Candys Watermelon</h3><img src="../assets/tegel/candys_watermelon.png" class="fullscreen-image">
                    <div class="progress-bar-container">
                        <h4 class="">Overall Rating</h4>
                        <div class="progress-bar-color">
                            <div class="indicator" style="left: 50%;">
                                <font color="white">5</font>
                            </div>
                            <div class="progress-overlay" style="width:50%; margin-left: 50%;"></div>
                        </div>
                        <div class="progress-bar-labels">
                            <span>poor</span>
                            <span>mid</span>
                            <span>good</span>
                        </div>
                    </div>
                    <br>
                    <hr>
                    <div class="rating-box" id="first">
                        <div>
                            <p>Nicotine</p>
                            <p>32mg</p>
                        </div>
                        <div>
                            <p>Quantity</p>
                            <p>20</p>
                        </div>
                        <div>
                            <p>Price</p>
                            <p>4.89€</p>
                        </div>
                        <!-- <p>Nicotine: 32mg / pouch</p>
                        <p>Quantity: 20</p>
                        <p>Price: 4.89€</p> -->
                    </div>
                    <hr>
                    <br>
                    <div class="rating-box">
                        <div class="progress-container">
                            <div class="progress-item">
                                <label>Hit Strength</label>
                                <div class="progress-bar">
                                    <div class="progress" style="width: 70%;"></div>
                                </div>
                            </div>
                            <div class="progress-item">
                                <label>Taste</label>
                                <div class="progress-bar">
                                    <div class="progress" style="width: 60%;"></div>
                                </div>
                            </div>
                            <div class="progress-item">
                                <label>Smell</label>
                                <div class="progress-bar">
                                    <div class="progress" style="width: 70%;"></div>
                                </div>
                            </div>
                        </div>

                        <div class="progress-container">
                            <div class="progress-item">
                                <label>Hit Quality</label>
                                <div class="progress-bar">
                                    <div class="progress" style="width: 50%;"></div>
                                </div>
                            </div>
                            <div class="progress-item">
                                <label>Drip Taste</label>
                                <div class="progress-bar">
                                    <div class="progress" style="width: 35%;"></div>
                                </div>
                            </div>
                            <div class="progress-item">
                                <label>Design</label>
                                <div class="progress-bar">
                                    <div class="progress" style="width: 75%;"></div>
                                </div>
                            </div>
                        </div>
                        <!-- <p>Hit strength: 7</p>
                        <p>Hit quality: 5</p>
                        <p>Taste: 6</p>
                        <p>Drip taste: 3.5</p>
                        <p>Smell: 7</p>
                        <p>Design: 7.5</p> -->

                    </div>



                    <p>Hit diagram: </p>
                    <br>
                    <br>
                    <br>
                    <br>

                    <!-- Further information -->
                    <!-- <p>Pouch Size: a bit longer than standard</p>
                    <p>Reusability: The re-use is not recommended as the taste is awful.</p>
                    <p>Aura: generally unknown</p>
                    <p>Recommendation: There are much better alternatives out there. If you seek an out-of-the-ordinary
                        experience this might be the one.</p> -->


                    <div class="toggle-list">
                        <div class="toggle-header" onclick="toggleList(this)">
                            <span>Further Information</span>
                            <span class="toggle-icon">+</span>
                        </div>
                        <div class="toggle-content">
                            <ul>
                                <li>Pouch Size: a bit longer than standard</li>
                                <li>Reusability: The re-use is not recommended as the taste is awful.</li>
                                <li>Aura: generally unknown</li>
                                <li>Recommendation: There are much better alternatives out there. If you seek an
                                    out-of-the-ordinary
                                    experience this might be the one.</li>
                            </ul>
                        </div>
                    </div>
                    <script src="../toggle_list.js"></script>
                </div>
            </main>

            <footer>
                <a class="link-wrapper" href="../about.html">About</a>
                <p>&copy; 2024 Snus Bewertungen</p>
            </footer>

        </body>

        </html>
        """
        self.output_file = "snus_rating_pages/" + str(input("Filename -> "))
        self.snus_name = str(input("Snus Name -> "))
        self.image_path = "assets/tegel/" + str(input("Image path -> "))
        self.criteria = [
            "Nicotine",
            "Quantity",
            "Hit Strength",
            "Hit Quality",
            "Drip Taste",
            "Reusability",
            "Design",
            "Smell",
            "Pouch Size",
            "Quantity",
            "Price",
            "Aura",
            "Recommendation",
        ]

    def add_link_to_page_index(self):
        injection = (
            '<a href="'
            + self.output_file
            + '" class="link-wrapper"> <div class="snus-box">'
        )
        injection += "<h3>" + self.snus_name + "</h3>"
        injection += '<img src="' + self.image_path + '" class="fullscreen-image">'
        injection += "<p>Overall rating: " + self.overall_rating + "</p> </div> <a>"

        with open("index.html", "r", encoding="utf-8") as file:
            self.index_html_content = file.read()

        main_index = self.index_html_content.find("<main>") + len("<main>")

        new_html_content = (
            self.index_html_content[:main_index]
            + injection
            + self.index_html_content[main_index:]
        )
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(new_html_content)
