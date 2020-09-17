class Planet:
  def __init__(self,name,radius,gravity,system):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system = system
  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}'


mars = Planet('Mars',200000,5.5,'Solar System')
print(f'Name is: {mars.name}')
print(mars.orbit())

naboo= Planet('Naboo',300000,8,'Naboo System')
print(f'Name is: {naboo.name}')
print(naboo.gravity)
print(naboo.orbit())