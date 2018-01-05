class SpaceAge(object):
    orbits = {'mercury':7600530.24, 'venus':19413907.2, 'earth':31558149.76, 'mars':59354294.4, 'jupiter':374335776.0, 'saturn':929596608.0, 'uranus':2661041808.0, 'neptune':5200418592.0}

    def __init__(self, seconds):
        self.seconds = seconds

    def on_planet(self, planet):
        return round(self.seconds / self.orbits[planet], 2)

def gen_fn(planet):
    setattr(SpaceAge, 'on_' + planet, lambda self: self.on_planet(planet))

for planet in SpaceAge.orbits.keys():
    gen_fn(planet)
