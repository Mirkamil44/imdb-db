import sqlite3
import pandas as pd

# Connect to your SQLite database
conn = sqlite3.connect('movies.sqlite')

# List of queries to execute
queries = [
    "SELECT id, original_title, budget FROM movies LIMIT 5;",
  
    "SELECT COUNT(*) FROM movies;",
  
    "SELECT * from directors where name == 'James Cameron' or name =='Luc Besson' or name =='John Woo';",

  "SELECT * from directors where name LIKE 'Steven%';",

  "SELECT COUNT(*) from directors where gender == 1",

  "SELECT name FROM directors WHERE gender == 1 ORDER by id asc limit 1 OFFSET 10;",

  "select original_title from movies order by popularity desc limit 3;",

  "SELECT original_title FROM movies WHERE release_date > '2000-01-01' ORDER by vote_average DESC LIMIT 1;",

  "SELECT original_title FROM movies JOIN directors ON directors.id =movies.director_id WHERE directors.name = 'Brenda Chapman';",

  "select name from directors join movies on movies.director_id = directors.id group by director_id order by count(name) desc limit 1;",

  "SELECT name FROM directors JOIN movies ON directors.id = movies.director_id GROUP BY director_id ORDER BY sum(budget) DESC limit 1;"

  
]

# Execute each query and print results
for query in queries:
    # Get column information
    columns_info = pd.read_sql_query(query, conn)

    # Print query and its result
    print(f"Query: {query}")
    print(columns_info)
    print("\n" + "="*50 + "\n")  # Separator for readability

# Close the connection
conn.close()


