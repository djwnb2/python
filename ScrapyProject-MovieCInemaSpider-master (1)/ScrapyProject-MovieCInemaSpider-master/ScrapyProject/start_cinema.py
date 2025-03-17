from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    # 获取项目的设置
    settings = get_project_settings()

    # 设置 Cinema 爬虫专属 FEEDS 配置
    settings['FEEDS'] = {
        r'A:\pythoncode\ScrapyProject-MovieCInemaSpider-master (1)\Database\cinema.json': {
            'format': 'json',
            'overwrite': True,
            'item_classes': ['ScrapyProject.items.CinemaItem']
        },
        r'A:\pythoncode\ScrapyProject-MovieCInemaSpider-master (1)\Database\screeningRoom.json': {
            'format': 'json',
            'overwrite': True,
            'item_classes': ['ScrapyProject.items.ScreeningRoomItem']
        },
        r'A:\pythoncode\ScrapyProject-MovieCInemaSpider-master (1)\Database\screening.json': {
            'format': 'json',
            'overwrite': True,
            'item_classes': ['ScrapyProject.items.ScreeningItem']
        }
    }

    # 创建 CrawlerProcess 实例
    process = CrawlerProcess(settings)

    # 添加要启动的爬虫
    process.crawl('cinema')

    # 启动爬虫
    process.start()

if __name__ == '__main__':
    main()
