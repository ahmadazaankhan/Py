# Nesting
capitals = {
  'France': 'Paris',
  'Germany': 'Berlin',
}

# Nesting a list in a dictionary

tarvel_log = {
  "France": {"cities_visited":["Paris", "Little", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionary in a dictionary
# cities_visited = {
#   "Europe": ["France", "Germany"]
# }

# Nesting Dictionary in a List

tarvel_log = [
  { 
    "country": "France", 
    "cities_visited":["Paris", "Little", "Dijon"], 
    "total_visits": 12
  },

  { 
    "country": "Germany",
    "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  },
]