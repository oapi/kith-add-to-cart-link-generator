from discord_webhooks import DiscordWebhooks
from bs4 import BeautifulSoup
import lxml
import requests

class Kith():
	def __init__(self):
		self.getInput

	def getInput(self):

		link = input("Enter a kith product link: ")
		checkout = checkoutLink(link)

class checkoutLink():
	def __init__(self, link):
		self.link = link
		self.s = requests.Session()

		self.getProductLink()

	def getProductLink(self):
		webhook = DiscordWebhooks("https://discordapp.com/api/webhooks/673405122377809920/HCFgn_ceoOq-mH0dwzcYY77f8W-z0OyKtlPTfblkKqbV-E32Vcief8lQEXJb1yGcJl9o")
		response = self.s.get(self.link)
		responseSoup = BeautifulSoup(response.text, "lxml")

		productSelect = responseSoup.find("select", {"name": "id"})
		sizes = productSelect.findAll("option")

		productTitle = responseSoup.find("h1", {"class", "product-single__title"})

		img = responseSoup.find("img")
		imgURL = "http:" + img['src']

		webhookContent = ""

		for size in sizes:
			if "value" and not "disabled" in str(size):
				inStockSize = size.text.strip()
				variant = size["value"]
				print(inStockSize + " (" + variant + ")")
				webhookContent += f"{inStockSize} ([{variant}](http://www.kith.com/cart/{variant}:1))\n"

		webhook.set_content(title=productTitle.text.strip(), description=(webhookContent), url=self.link, color=0xdc00ff)
		webhook.set_footer(text="oapi webhook", icon_url='https://avatars1.githubusercontent.com/u/58406347?s=460&v=4')
		webhook.set_thumbnail(url=imgURL)
		webhook.send()

m = Kith()
m.getInput()