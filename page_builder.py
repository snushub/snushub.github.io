
class PageBuilder():
    def __init__(self):
        self.full_html_content = """
            <!DOCTYPE html>
            <html lang="de">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Snus Bewertungen</title>
                <link rel="stylesheet" href="../styles.css">
            </head>

            <body>

                <header>
                    <a class="link-wrapper" href="../index.html">
                        <img src="../assets/logos/snus_hub_logo.JPG" class="fullscreen-image">
                    </a>
                </header>
                
                <main>

            """
        self.output_file = "snus_rating_pages/" + str(input("Filename -> "))
        self.snus_name = str(input("Snus Name -> "))
        self.image_path = "assets/tegel/" + str(input("Image path -> "))
        self.criteria = ["Taste", "Nicotine hit", "Drip taste", "Design", "Smell", "Pouch Size", 
                    "Quantity", "Price", "Aura", "Hit diagram", "Recommendation"]
        
        self.snus_box_builder()
        self.add_page_bottom()
        self.create_file()
        self.add_link_to_page_index()

    def snus_box_builder(self):
        output = ""
        output += '<div class="snus-box">'
        output += "<h3>" + self.snus_name + "</h3>"
        output += '<img src="../' + self.image_path + '" class="fullscreen-image">'
        self.overall_rating = str(input("Overall rating: "))
        output += "<p>Overall rating: " + self.overall_rating + "</p><hr>"
        for crit in self.criteria: 
            val = str(input(crit + " -> "))
            output += "<p>" + crit + ": " + val + "</p>"
        output += "</div>"
        self.full_html_content += output
    
    def add_page_bottom(self):
        self.full_html_content += """
            </main>

                <footer>
                    <a class="link-wrapper" href="../about.html">About</a>
                    <p>&copy; 2024 Snus Bewertungen</p>
                </footer>

            </body>

            </html>
            """
    def create_file(self):
        with open(self.output_file, "w") as file:
            file.write(self.full_html_content)
            
    def add_link_to_page_index(self):
        template = """
        <a href="snus_rating_pages/killa_cold_mint.html" class="link-wrapper">
            <div class="snus-box">
                <h3>Killa Cold Mint</h3>
                <img src="assets/tegel/killa_cold_mint.png" class="fullscreen-image">
                <p>Overall rating: 3/5</p>
            </div>
        </a>
            """
        
        injection = '<a href="'+ self.output_file + '" class="link-wrapper"> <div class="snus-box">'
        injection += "<h3>" + self.snus_name + "</h3>"
        injection += '<img src="' + self.image_path + '" class="fullscreen-image">'
        injection += "<p>Overall rating: "+ self.overall_rating + "</p> </div> <a>"
        
        
        with open("index.html", 'r', encoding='utf-8') as file:
            self.index_html_content = file.read()

        main_index = self.index_html_content.find("<main>") + len("<main>")

        new_html_content = self.index_html_content[:main_index] + injection + self.index_html_content[main_index:]
        with open("index.html", 'w', encoding='utf-8') as file:
            file.write(new_html_content)

PageBuilder()


print("File has been generated")

