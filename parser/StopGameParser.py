import datetime
from string import Template
from typing import TypeAlias, Tuple, List
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup as bs

from .subpackages import NewsCardExtractor as nce

date: TypeAlias = datetime.date


class StopGameParser(object):
    """Class for parsing news by date and tags from StopGame.ru"""
    NEWS_URL_TEMPLATE = Template("https://stopgame.ru/news/all/p$number")

    def __init__(self, dates: Tuple[date, date]) -> None:
        self.dates = dates
        self.parsed_pages = []

    def parse(self) -> None:
        '''Parse pages with news into list of data

        Args:

        Returns:
            None

        Raises:
            Exception: If an error is received while retrieving
            the results of threads execution
        '''

        lastest_news_page_number = self.__get_page_number_by_date(self.dates[1])
        erliest_news_page_number = self.__get_page_number_by_date(self.dates[0],
                                                                  lastest_news_page_number)
        with ThreadPoolExecutor() as executor:
            futures = {
                    executor.submit(self.__get_page, page_number): page_number
                    for page_number in range(lastest_news_page_number,
                                             erliest_news_page_number + 1)
                }
            for future in as_completed(futures):
                page_number = futures[future]
                try:
                    page = future.result()
                    page_news = nce.NewsCardExtractor.get_news_cards(page)

                    titles = nce.NewsCardExtractor.get_titles_of_news_cards(page_news)
                    dates = nce.NewsCardExtractor.get_dates_from_news_cards(page_news)
                    tags = nce.NewsCardExtractor.get_tags_from_news_cards(page_news)
                    hrefs = nce.NewsCardExtractor.get_hrefs_from_news_cards(page_news)

                    self.__add_to_parsed_pages(titles, dates, tags, hrefs)
                except Exception as e:
                    print(f"Error processing page {page_number}: {e}")

    def __get_page_number_by_date(self, date_from: date,
                                  min_page_number: int = 1) -> int:
        page_number = min_page_number

        while True:
            page = self.__get_page(page_number)
            page_news = nce.NewsCardExtractor.get_news_cards(page)

            if not page_news:
                return page_number - 1

            news_dates = nce.NewsCardExtractor.get_dates_from_news_cards(page_news)

            if any(map(
                    lambda news_date: news_date == date_from,
                    news_dates)):
                return page_number

            page_number += 1

    @classmethod
    def __get_page(cls, page_number: int) -> bs:
        response = requests.get(
                    cls.NEWS_URL_TEMPLATE.substitute({'number': page_number}))
        soup = bs(response.text, 'html.parser')
        return soup

    def __add_to_parsed_pages(self, titles: List[str], dates: List[date],
                              tags: List[str], hrefs: List[str]) -> None:
        page_data = [
            {
                'title': title,
                'date': date,
                'tag': tag,
                'href': href
            }
            for title, date, tag, href in zip(titles, dates, tags, hrefs)
        ]

        self.parsed_pages.extend(page_data)


