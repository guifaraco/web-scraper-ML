from scraper.spiders.olx_spider import OlxSpider

def save_data_to_db(data, collection_name):
    print(f"Salvando {len(data)} registros na coleção '{collection_name}'...")
    print("Dados salvos com sucesso (simulação).")


def main():
    spiders_to_run = [
        OlxSpider()
    ]

    for spider in spiders_to_run:
        scraped_data = spider.scrape()

        if scraped_data:
            save_data_to_db(scraped_data, spider.name)

if __name__ == "__main__":
    main()