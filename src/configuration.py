from dataclasses import dataclass


@dataclass
class ScraperConfig:
	url: str
	table_id: str
	player_name_class: str
	player_salary_class: str
	player_year_class: str
	player_level_class: str


@dataclass
class OfferRulesConfig:
	top_quantity: int
