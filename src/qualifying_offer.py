from typing import List
from players import Player

class QualifyingOfferInfo(object):
	def __init__(self, offer_amount: float, top_players: List[Player], excluded_players: List[Player]):
		self.offer_amount = offer_amount
		self.top_players = top_players
		self.excluded_players = excluded_players