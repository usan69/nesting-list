capital = {"bangladesh": "dhaka",
           "india": "delhi",
           }

travel_log = {
    "bangladesh": ["dhaka", "barisal"],
    "india": ["delhi", "chennai"],
}

travel_log = {
    "bangladesh": {"cities_visited": ["dhaka", "barisal"], "total_visited": 12},
    "india": {"cities_visited": ["delhi", "chennai"], "total_visited": 12},
}

travel_log = [
    {
        "country": "bangladesh",
        "cities_visited": ["dhaka", "barisal"],
        "total_visited": 12
    },

    {
        "country": "india",
        "cities_visited": ["delhi", "chennai"],
        "total_visited": 12
    },
]
print(travel_log)
