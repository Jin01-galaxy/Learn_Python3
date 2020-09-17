class Planet:
  def __init__(self):
    self.name = 'Mars'
    self.radius = 200000
    self.gravity = 2.1
    self.system = 'Solar System'

  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'


mars = Planet()
print(f'Name is: {mars.name}')
print(mars.orbit())

