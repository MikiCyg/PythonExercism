class SpaceAge(object):
	def __init__(self, seconds):
		self.seconds = seconds

	def on_mercury(self):
		return round(self.seconds / (0.2408467 * 31557600), 2)

	def on_venus(self):
		return round(self.seconds / (0.61519726 * 31557600), 2)

	def on_earth(self):
		return round(self.seconds / 31557600, 2)

	def on_mars(self):
		return round(self.seconds / (1.8808158 * 31557600), 2)

	def on_jupiter(self):
		return round(self.seconds / (11.862615 * 31557600), 2)

	def on_saturn(self):
		return round(self.seconds / (31557600 * 29.447498), 2)

	def on_uranus(self):
		return round(self.seconds / (31557600 * 84.016846), 2)

	def on_neptune(self):
		return round(self.seconds / (31557600 * 164.79132), 2)
