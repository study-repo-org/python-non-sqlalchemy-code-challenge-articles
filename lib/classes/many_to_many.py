class Article:
    all = []

    def __init__(self, author, magazine, title):
        # Checking if the author is an instance of Author
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        # Checking if the magazine is an instance of Magazine
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        # Checking if the title is a string
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        # Checking if the title length is between 5 and 50 characters
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")

        # attributes for author, magazine, and title
        self.__author = author
        self.__magazine = magazine
        self.__title = title

        # Adding the article to the list of all articles
        Article.all.append(self)
        # Adding the article to the respective magazines article list
        magazine._add_article(self)
        # Adding the article to the respective authors article list
        author._add_article(self)

    @property
    def title(self):
        # Returning the title of the article
        return self.__title

    @property
    def author(self):
        # Returning the author of the article
        return self.__author

    @property
    def magazine(self):
        # Returning the magazine of the article
        return self.__magazine

    @author.setter
    def author(self, new_author):
        # Checking if the new author is an instance of Author
        if not isinstance(new_author, Author):
            raise ValueError("New author must be an instance of Author")
        # Removing the article from the current authors list
        self.__author._remove_article(self)
        # Sating the new author
        self.__author = new_author
        # Adding the article to the new authors list
        new_author._add_article(self)

    @magazine.setter
    def magazine(self, new_magazine):
        # Checking if the new magazine is an instance of Magazine
        if not isinstance(new_magazine, Magazine):
            raise ValueError("New magazine must be an instance of Magazine")
        # Removing the article from the current magazines list
        self.__magazine._remove_article(self)
        # Sating the new magazine
        self.__magazine = new_magazine
        # Adding the article to the new magazines list
        new_magazine._add_article(self)


class Author:
    def __init__(self, name):
        # Checking if the name is a string
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        # Checking if the name is longer than 0 characters
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        # Sating instance attributes
        self.__name = name
        self.__articles = []

    @property
    def name(self):
        # Returning the name of the author
        return self.__name

    def articles(self):
        # Returning the list of articles written by the author
        return self.__articles

    def magazines(self):
        # Returning the list of unique magazines the author has contributed to
        return list(set([article.magazine for article in self.__articles]))

    def add_article(self, magazine, title):
        # Create and return a new article
        return Article(self, magazine, title)

    def _add_article(self, article):
        # method for adding an article to the authors list
        self.__articles.append(article)

    def _remove_article(self, article):
        # method for removing an article from the authors list
        self.__articles.remove(article)

    def topic_areas(self):
        # Returning the list of unique topic areas covered by the authors articles
        if not self.__articles:
            return None
        return list(set([article.magazine.category for article in self.__articles]))


class Magazine:
    all = []

    def __init__(self, name, category):
        # Checking if the name and category are strings
        if not isinstance(name, str) or not isinstance(category, str):
            raise ValueError("Name and category must be strings")
        # Checking if the name length is between 2 and 16 characters
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        # Checking if the category length is greater than 0 characters
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        # Sating instance attributes
        self.__name = name
        self.__category = category
        self.__articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        # Returning the name of the magazine
        return self.__name

    @name.setter
    def name(self, new_name):
        # Checking if the new name is a string
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        # Checking if the new name length is between 2 and 16 characters
        if len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        # Sating the new name
        self.__name = new_name

    @property
    def category(self):
        # Returning the category of the magazine
        return self.__category

    @category.setter
    def category(self, new_category):
        # Checking if the new category is a string
        if not isinstance(new_category, str):
            raise ValueError("Category must be a string")
        # Checking if the new category length is greater than 0 characters
        if len(new_category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        # Sating the new category
        self.__category = new_category

    def articles(self):
        # Returning the list of articles published by the magazine
        return self.__articles

    def contributors(self):
        # Returning the list of unique authors who have contributed to the magazine
        return list(set([article.author for article in self.__articles]))

    def _add_article(self, article):
        # method for adding an article to the magazines list
        self.__articles.append(article)

    def _remove_article(self, article):
        # method for removing an article from the magazines list
        self.__articles.remove(article)

    def article_titles(self):
        # Returning the list of titles of all articles written for the magazine
        if not self.__articles:
            return None
        return [article.title for article in self.__articles]

    def contributing_authors(self):
        # Returning a list of authors who have written more than 2 articles for the magazine
        if not self.__articles:
            return None
        author_count = {}
        for article in self.__articles:
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1

        contributing_authors = [author for author, count in author_count.items() if count > 2]
        if not contributing_authors:
            return None
        return contributing_authors
    
    @staticmethod
    # Returning the Magazine with the most articles
    # Returning None if there are no articles.
    def top_publisher():
        if not Magazine.all:
            return None
        magazines_with_articles = [mag for mag in Magazine.all if mag.articles()]
        if not magazines_with_articles:
            return None
        return max(magazines_with_articles, key=lambda mag: len(mag.articles()), default=None)
