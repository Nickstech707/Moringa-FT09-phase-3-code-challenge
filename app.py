# app.py

from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

# Assuming get_author_by_id and get_magazine_by_id are implemented elsewhere
def get_author_by_id(author_id):
    # Placeholder for fetching author by ID
    # You need to replace this with actual database query logic
    pass
    

def get_magazine_by_id(magazine_id):
    # Placeholder for fetching magazine by ID
    # You need to replace this with actual database query logic
    pass


def main():
    # Initialize the database and create tables
    create_tables()



    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Validate inputs
    if not magazine_category:
        print("Magazine category cannot be empty.")
        return

    if len(article_title) < 5 or len(article_title) > 50:
        print("Article title must be between 5 and 50 characters.")
        return

    if not article_content:
        print("Article content cannot be empty.")
        return

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))
    article_id = cursor.lastrowid  

    conn.commit()

    

    # Fetch all records
    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in authors:
        print(Author(author["id"], author["name"]))


    print("\nArticles:")
    for article in articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))



if __name__ == "__main__":
    main()
