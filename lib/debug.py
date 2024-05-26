#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Creating instances
    author = Author("Mohamed Ahmed")
    magazine = Magazine("Daily Code", "Code")
    article = Article(author, magazine, "Why Learn Python")

    # Accessing properties
    print(f"Author Name: {author.name}")
    print(f"Magazine Name: {magazine.name}, Magazine Category: {magazine.category}")
    print(f"Article Magazine: {article.magazine.name}")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
