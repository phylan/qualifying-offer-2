from typing import List, Dict
from .players import Player
from .configuration import ScraperConfig, OfferRulesConfig
from .scraping import Scraper
from .calculation import OfferCalculator

class QualifyingOfferInfo(object):
	def __init__(self, offer_amount: float, top_players: List[Player], excluded_players: List[Player]):
		self.offer_amount = offer_amount
		self.top_players = top_players
		self.excluded_players = excluded_players

	def to_dict(self) -> Dict:
		return {
			'offer_amount': self.offer_amount,
			'top_players': [player.to_dict() for player in self.top_players],
			'excluded_players': [player.to_dict() for player in self.excluded_players]
		}

	@classmethod
	def build_offer_info(cls, scraper_config: ScraperConfig, offer_config: OfferRulesConfig) -> 'QualifyingOfferInfo':
		scraper = Scraper(scraper_config)
		players = scraper.get_players()
		calculator = OfferCalculator(players, offer_config)

		offer_amount = calculator.calculate_qualifying_offer()
		top_players = calculator.get_top_players()
		excluded_players = calculator.get_excluded_players()

		return cls(offer_amount, top_players, excluded_players)