movies = [("Patton Oswalt: Annihilation", 2017), ("New York Doll", 2005), ("And Then I Go", 2017), ("Love Songs", 2007), ("Forever My Girl", 2018)]

moviedate = [date for (movie, date) in movies if date > 2007] 
print(moviedate)