import scrapy


class Lipsumspider(scrapy.Spider):
    name = "Lipsum"
    start_urls = ["https://www.lipsum.com"]

    def parse(self, response):
        # create a dictionnary with the form values
        return scrapy.FormRequest.from_response(
            response, formdata={"amount": "10"}, callback=self.parse_paragraph
        )

    def parse_paragraph(self, response):
        # parse the main page after the spider has generated 10 paragraph
        self.logger.info(
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Début des logs XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n"
        )

        print(
            "============================== Itérations sur les 10 paragraphes de la page ==============================\n\n"
        )
        para = response.xpath("//p")
        for p in para:
            print(f"{p.get()}\n\n")

        print(
            f"============================== Quatrième paragraphe : ==============================\n{response.xpath('//p')[3].get()}\n"
        )

        print(
            f"============================== Dernière phrase du quatrième paragraphe : ==============================\n{response.xpath('//p')[3].get().split('.')[-2]}\n\n"
        )
