Scrabbletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(Scrabbletters, points)}
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"BLUE": ["EARTH", "ERASER", "ZAP"], "TENNIS": ["EYES", "BELLY", "COMA"], "EXIT": ["MACHINE", "HUSKY", "PERIOD"]}
player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0 
  for word in words:
    player_points += score_word(word)  
  player_to_points[player] = player_points 
  
#? Create a function that takes a player's name and a word, then adds that word to their list of played words.
def play_word(player, word):
    if player in player_to_words:
        player_to_words[player].append(word)
        update_point_totals()
        
#? Convert the nested loops that calculate player scores into a function that updates scores whenever a word is played.
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

#? Adjust score_word function or letter_to_points dictionary so it can handle lowercase letters.
letter_to_points = {key.upper(): value for key, value in zip(Scrabbletters, points)}
letter_to_points.update({key.lower(): value for key, value in zip(Scrabbletters, points)})

