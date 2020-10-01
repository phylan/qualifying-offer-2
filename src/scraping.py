from bs4 import BeautifulSoup
from bs4.element import Tag
from .configuration import ScraperConfig
from .exceptions import ScrapingException
from .players import Player
from typing import List
import requests
import logging

class Scraper(object):
	def __init__(self, scraper_config: ScraperConfig):
		self.scraper_config = scraper_config

	def get_players(self):
		html = self._get_html()
		return self._parse_html(html)

	def _get_html(self) -> str:
		try:
			resp = requests.get(self.scraper_config.url)
			return resp.text
		except requests.exceptions.RequestException as ex:
			logger = logging.getLogger()
			logger.exception()
			raise

	def _parse_row(self, row:Tag) -> Player:
		name = row.select(f'.{self.scraper_config.player_name_class}')[0].text
		year = row.select(f'.{self.scraper_config.player_year_class}')[0].text
		level = row.select(f'.{self.scraper_config.player_level_class}')[0].text
		raw_salary = row.select(f'.{self.scraper_config.player_salary_class}')[0].text

		try:
			filtered_salary = ''.join(char for char in raw_salary if char.isdigit() or char == '.')
			salary = float(filtered_salary)
		except ValueError:
			salary = None

		return Player(name, level, year, raw_salary, salary)


	def _parse_html(self, html:str) -> List[Player]:
		try:
			document = BeautifulSoup(html, features="html.parser")
			rows = document.select(f"#{self.scraper_config.table_id} tr")
			return [self._parse_row(row) for row in rows]
		except Exception as ex:
			logger = logging.getLogger()
			logger.exception()
			raise ScrapingException(ex)
