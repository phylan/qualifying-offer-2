from configuration import OfferRulesConfig
from players import Player
from typing import List
import statistics

class OfferCalculator(object):
	def __init__(self, players: List[Player], offer_rules_config: OfferRulesConfig):
		self.config = offer_rules_config
		self.players_with_salary = [player for player in players if player.salary is not None]
		self.players_without_salary = [player for player in players if player.salary is None]

	def calculate_qualifying_offer(self) -> float:
		sorted_salary_players = sorted(self.players_with_salary, key=lambda player: player.salary, reverse=True)
		top_players = sorted_salary_players[:self.config.top_quantity]
		return statistics.mean(p.salary for p in top_players)