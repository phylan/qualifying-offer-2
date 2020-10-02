from dataclasses import dataclass
from typing import Dict


@dataclass
class ScraperConfig:
	url: str
	table_id: str
	player_name_class: str
	player_salary_class: str
	player_year_class: str
	player_level_class: str

	@classmethod
	def from_dict(cls, config: Dict):
		return cls(config['url'], config['table_id'], config['player_name_class'],
					config['player_salary_class'], config['player_year_class'],
					config['player_level_class'])


@dataclass
class OfferRulesConfig:
	top_quantity: int

	@classmethod
	def from_dict(cls, config: Dict):
		return cls(config['top_quantity'])