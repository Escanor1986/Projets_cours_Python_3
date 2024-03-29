#! ###############################################################################################################################

#! First Program in Python using basic functionalities 

#! ###############################################################################################################################


destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#* Fonction pour obtenir l'index d'une destination
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

#* Fonction pour extraire la destination du voyageur
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

attractions = [[] for x in range(5)]

#* Fonction pour ajouter une attraction en corrélation avec la destination
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#* Fonction pour trouver les attractions ayant un intérêt pour le voyageur
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    #? Au cas où nous aurions besoin d'utiliser le nom complet de l'attraction
    attraction_name = possible_attraction[0] 
    attraction_tags = possible_attraction[1]
    for interest in interests:
      if interest not in attraction_tags:
        break
    else:
      attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

#? print(la_arts)
la_arts = find_attractions("Los Angeles, USA", ['art'])

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_insterests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_insterests)
  interests_string = "Hi "
  interests_string += str(traveler[0])
  interests_string += ", we think you'll like these places around "
  for attraction in traveler_attractions:
    interests_string += " " + str(attraction) + " "
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
# print(smills_france)

#! ###############################################################################################################################

#! String method exo using .strip(), .split(), .format(), .find(), .upper()...

#! ###############################################################################################################################

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(",")
highlighted_poems_stripped = [elem.strip() for elem in highlighted_poems_list]
highlighted_poems_details = [elem.split(":") for elem in highlighted_poems_stripped]
print(highlighted_poems_details)

titles = []
poets = []
dates = []

for poem_details in highlighted_poems_details:
    for index, detail in enumerate(poem_details):
        if index == 0:
            titles.append(detail)
        elif index == 1:
            poets.append(detail)
        elif index == 2:
            dates.append(detail)
        else:
          print("You seem to have some unexpected behaviour with your app !")
print(titles, poets, dates)

for i in range(len(titles)):
    print("The poem {} was published by {} in {}".format(titles[i], poets[i], dates[i]))
