from dataclasses import dataclass
from typing import Union, Dict

class Player(object):
	def __init__(self, name: str, level: str, year: int, raw_salary: str, salary: Union[float, None]):
		self.name = name
		self.level = level
		self.year = year
		self.raw_salary = raw_salary
		self.salary = salary

	def to_dict(self) -> Dict:
		return self.__dict__