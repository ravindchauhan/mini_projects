import random
movies=[
    "The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction",
    "Schindler's List", "The Lord of the Rings", "Forrest Gump", "Inception",
    "The Matrix", "Goodfellas", "Seven", "It's a Wonderful Life",
    "The Silence of the Lambs", "Saving Private Ryan", "Interstellar", "Spirited Away",
    "The Green Mile", "Parasite", "Whiplash", "The Prestige",
    "Gladiator", "The Departed", "The Lion King", "Back to the Future",
    "Alien", "The Pianist", "Django Unchained", "The Shining",
    "WALL-E", "Before Sunrise", "Blade Runner 2049", "Spider-Man: Into the Spider-Verse",
    "No Country for Old Men", "Catch Me If You Can", "Good Will Hunting"
]

total_revenue=0
for i in range (0,len(movies)):
  shows=random.choice([5,10,7,6,8,9])
  tickets=random.randint(10,30)
  price=random.choice([200,400,500,600])
  totalCollection=shows*tickets*price
  print("Total Collection of",movies[i]," :","$",totalCollection)
  total_revenue+=totalCollection
print("\nGrand Total Collection:", "$", total_revenue)
