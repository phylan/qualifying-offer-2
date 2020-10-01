class ScrapingException(Exception):
	def __init__(self, exception: Exception, message:str = "An exception occurred while scraping salary HTML"):
		self.innerException = exception
		super().__init__(f"{message} {exception}")