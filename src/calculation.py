from .configuration import OfferRulesConfig
from .players import Player
from typing import List
import statistics

def _sort_players_by_salary(players: List[Player]) -> List[Player]:
	return sorted(players, key=lambda player: player.salary, reverse=True)

class OfferCalculator(object):
	def __init__(self, players: List[Player], offer_rules_config: OfferRulesConfig):
		self.config = offer_rules_config
		self._players_with_salary = [player for player in players if player.salary is not None]
		self._players_without_salary = [player for player in players if player.salary is None]

	def calculate_qualifying_offer(self) -> float:
		top_players = self.get_top_players()
		return statistics.mean(p.salary for p in top_players)

	def get_top_players(self) -> List[Player]:
		sorted_players = _sort_players_by_salary(self._players_with_salary)
		return sorted_players[:self.config.top_quantity]

	def get_excluded_players(self) -> List[Player]:
		return self._players_without_salary