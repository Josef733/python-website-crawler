import scrapy

class MainSpider(scrapy.Spider):
    name = "main"

    num = int(input("How many URLs would you like to insert?"))

    urls = []

    for i in range(num):
        userurl = input("Enter URL #" + str(i + 1) + ":")
        urls.append(userurl)

    print("BEFORE")
    print(urls)

    start_urls = urls

    print("AFTER")
    print(start_urls)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'main-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


        