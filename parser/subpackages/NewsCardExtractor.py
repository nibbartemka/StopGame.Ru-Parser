import datetime
from typing import List, TypeAlias

from bs4 import BeautifulSoup as bs, ResultSet

from .DataParser import DataParser
from .settings import WEBSITE_URL

date: TypeAlias = datetime.date


class NewsCardExtractor(object):
    """Class for extracting news cards from HTML and data from them."""
    @staticmethod
    def get_news_cards(page: bs) -> ResultSet:
        return page.find_all('div', class_="_card_1vlem_1")

    @staticmethod
    def get_dates_from_news_cards(news_cards: ResultSet) -> List[date]:
        dates = []
        for news_card in news_cards:
            date_div = news_card.find('div', class_='_info-row_1vlem_121')
            date_value = date_div.find('span').text

            dates.append(DataParser.process_date(date_value))

        return dates

    @staticmethod
    def get_hrefs_from_news_cards(news_cards: ResultSet) -> List[str]:
        hrefs = []
        for news_card in news_cards:
            href_a = news_card.find('a', class_='_title_1vlem_60')
            href_value = href_a.attrs["href"]

            hrefs.append(f'{WEBSITE_URL}{href_value}')

        return hrefs

    @staticmethod
    def get_tags_from_news_cards(news_cards: ResultSet) -> List[str]:
        tags = []
        for news_card in news_cards:
            tags_div = news_card.find('div', class_='_tags_1vlem_100')
            tags_value = [item.text for item in tags_div.find_all('a')]

            tags.append(', '.join(tags_value))

        return tags

    @staticmethod
    def get_titles_of_news_cards(news_cards: ResultSet) -> List[str]:
        titles = []
        for news_card in news_cards:
            title_a = news_card.find('a', class_='_title_1vlem_60')
            title_value = title_a.text

            titles.append(title_value)

        return titles
