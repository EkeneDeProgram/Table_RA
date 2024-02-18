import graphene
from graphene_django.types import DjangoObjectType
from .models import Books


# Define GraphQL type for the Books model
class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")


# Define the Query class for GraphQL queries
class Query(graphene.ObjectType):
    # Field to get all books
    all_books = graphene.List(BooksType)

    # Field to get a particular book by ID
    book = graphene.Field(BooksType, id=graphene.Int(required=True))

    # Field to get a particular book by title
    book_by_title = graphene.Field(BooksType, title=graphene.String(required=True))

    # Field to get a particular book by excerpt
    book_by_excerpt = graphene.Field(BooksType, excerpt=graphene.String(required=True))

    # Resolver function for the "all_books" field
    def resolve_all_books(self, info):
        return Books.objects.all()

    # Resolver function for the "book" field
    def resolve_book(self, info, id):
        return Books.objects.get(pk=id)

    # Resolver function for the "book_by_title" field
    def resolve_book_by_title(self, info, title):
        return Books.objects.get(title=title)

    # Resolver function for the "book_by_excerpt" field
    def resolve_book_by_excerpt(self, info, excerpt):
        return Books.objects.get(excerpt=excerpt)


schema = graphene.Schema(query=Query)
