from flask_api import FlaskAPI, status, exceptions
from src.qualifying_offer import QualifyingOfferInfo
from src.configuration import OfferRulesConfig, ScraperConfig
from src.exceptions import ConfigurationException
import json

app = FlaskAPI(__name__)

try:
	with open('settings.json') as f:
		config = json.load(f)

	scraper_config = ScraperConfig.from_dict(config['scraper'])
	offer_config = OfferRulesConfig.from_dict(config['offer_rules'])

except (KeyError, FileNotFoundError, IOError) as ex:
	raise ConfigurationException(ex)


@app.route("/qualifying-offer", methods=['GET'])
def get():
	try:
		offer_info = QualifyingOfferInfo.build_offer_info(scraper_config, offer_config)
	except Exception as ex:
		app.logger.exception(ex.message)
		return ex.message, status.HTTP_500_INTERNAL_SERVER_ERROR

	return offer_info.to_dict(), status.HTTP_200_OK

if __name__ == "__main__":
	app.run(debug=True)