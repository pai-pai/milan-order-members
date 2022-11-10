"""Module contains MilanoSpider.

"""
import pathlib
import scrapy


DOMAIN = "consulentidellavoro.mi.it"

RESULT_FILE = pathlib.Path('ConsulentiDelLavoro.csv')
FIELDS = ['Nome', 'Numero', 'Codice fiscale', 'PEC', 'Status', 'Indirizzo', 'Città', 'Provincia']


class MilanoSpider(scrapy.Spider):
    """This spider gets required data:
    - Nome
    - Numero
    - Codice fiscale
    - PEC
    - Status
    - Indirizzo
    - Città
    - Provincia

    """
    name = "milano-spider"
    domain = DOMAIN
    allowed_domains = [domain]
    custom_settings = {
        'FEEDS': {
            RESULT_FILE: {
                'format': 'csv',
                'overwrite': True,
                'fields': FIELDS,
            }
        }
    }
    start_urls = ['https://consulentidellavoro.mi.it/ordine/gli-iscritti-allordine/']

    def parse(self, response, **kwargs):
        items = response.xpath('//div[contains(@class, "userMeta")]')
        for item in items:
            details = item.xpath('div/table')
            address = details.xpath('tr[2]/td[2]/text()').getall()
            city_state = address[1].split('-')
            yield {
                'Nome': item.xpath('text()').get().strip(),
                'Numero': item.xpath('small[1]/text()').get().replace('Numero di iscrizione: ', ''),
                'Codice fiscale': item.xpath(
                    'small[2]/text()').get().replace('Codice fiscale: ', ''),
                'PEC': details.xpath('tr[3]/td[2]/text()').get(),
                'Status': details.xpath('tr[1]//small/text()').get(),
                'Indirizzo': address[0].strip(),
                'Città': city_state[0].strip(),
                'Provincia': city_state[1].strip(),
            }
        next_page_url = response.css('a.next.page-numbers').xpath('@href').get()
        if next_page_url is not None:
            yield scrapy.Request(url=f'{next_page_url}', callback=self.parse)
