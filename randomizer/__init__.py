NAMES = [
  'Aron',
  'Carsten',
  'Dima',
  'Max',
  'Stephan',
  'Willy',
]


NATIONS = [
  'Elben',
  'Isengart',
  'Menschen',
  'Mordor',
  'Orks',
  'Zwerge',
]

from random import Random

def get_rand_el(l):
  return l[Random().randint(0, len(l)-1)]

def pop_rand_el(l):
  return l.pop(Random().randint(0, len(l)-1))

class Person(object):
  def __init__(self, name, team = None, nation = None):
    super(Person, self).__init__()
    self.name = name
    self.team = team
    self.setNation(nation)


  def __str__(self):
    return "<%s - Team: %s, Volk: %s>" %(self.name, self.team or "kein", self.nation or "kein")

  def __repr__(self):
    return str(self)

  def setNation(self, nation = None, nations = None, distinct = False):
    if nation:
      self.nation = nation
      return self.nation
    nations_list = nations or NATIONS
    if distinct:
      self.nation = pop_rand_el(nations_list)
    else:
      self.nation = get_rand_el(nations_list)
    return self.nation

  def getNation(self):
    self.setNation(self.nation)
    return self.nation

  @staticmethod
  def setTeam(person_list, teams = []):
    if not teams: return None
    res = []
    curTeam = 0
    while person_list:
      person = pop_rand_el(person_list)
      curTeam += 1
      curTeam %= len(teams)
      person.team = curTeam + 1
      res.append(person)
    return res



def randomize(players, max_teams, nations):
  players = [Person(**a) for a in players]

  if nations:
    for p in players:
      p.setNation(nations = nations)
  if max_teams:
    players = Person.setTeam(players, range(1, max_teams + 1))
  print players
  return players
