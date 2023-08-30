from django.test import TestCase
from .models import Publisher, Book, Contributor, BookContributor, Review
from datetime import date
from django.contrib.auth import get_user_model

class PublisherModelTest(TestCase):
    def test_create_publisher(self):
        publisher = Publisher.objects.create(name="Example Publisher", website="https://example.com", email="example@example.com")
        self.assertEqual(publisher.name, "Example Publisher")
        self.assertEqual(publisher.website, "https://example.com")
        self.assertEqual(publisher.email, "example@example.com")

    def test_publisher_str_representation(self):
        publisher = Publisher.objects.create(name="Another Publisher", website="https://another.com", email="another@another.com")
        self.assertEqual(str(publisher), "Another Publisher")

class ContributorModelTest(TestCase):
    def test_create_contributor(self):
        contributor = Contributor.objects.create(first_names="John", last_names="Doe", email="johndoe@example.com")
        self.assertEqual(contributor.first_names, "John")
        self.assertEqual(contributor.last_names, "Doe")
        self.assertEqual(contributor.email, "johndoe@example.com")

    def test_contributor_str_representation(self):
        contributor = Contributor.objects.create(first_names="Jane", last_names="Smith", email="janesmith@example.com")
        self.assertEqual(str(contributor), "Smith, J")

class BookModelTest(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name="Test Publisher", website="https://test.com", email="test@test.com")

    def test_create_book(self):
        book = Book.objects.create(title="Sample Book", publication_date=date(2022, 1, 1), isbn="1234567890123", publisher=self.publisher)
        self.assertEqual(book.title, "Sample Book")
        self.assertEqual(book.publisher, self.publisher)

    def test_book_str_representation(self):
        book = Book.objects.create(title="Another Book", publication_date=date(2021, 12, 31), isbn="9876543210987", publisher=self.publisher)
        self.assertEqual(str(book), "Another Book (9876543210987)")

    def test_isbn13(self):
        book = Book.objects.create(title="ISBN Book", publication_date=date(2021, 12, 31), isbn="1234567890123", publisher=self.publisher)
        self.assertEqual(book.isbn13(), "123-4-56-789012-3")

class BookContributorModelTest(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name="Test Publisher", website="https://test.com", email="test@test.com")
        self.contributor = Contributor.objects.create(first_names="John", last_names="Doe", email="johndoe@example.com")
        self.book = Book.objects.create(title="Sample Book", publication_date=date(2022, 1, 1), isbn="1234567890123", publisher=self.publisher)

    def test_create_book_contributor(self):
        book_contributor = BookContributor.objects.create(book=self.book, contributor=self.contributor, role=BookContributor.ContributionRole.AUTHOR)
        self.assertEqual(book_contributor.book, self.book)
        self.assertEqual(book_contributor.contributor, self.contributor)
        self.assertEqual(book_contributor.role, BookContributor.ContributionRole.AUTHOR)

class ReviewModelTest(TestCase):
    def setUp(self):
        self.publisher = Publisher.objects.create(name="Test Publisher", website="https://test.com", email="test@test.com")
        self.contributor = Contributor.objects.create(first_names="John", last_names="Doe", email="johndoe@example.com")
        self.book = Book.objects.create(title="Sample Book", publication_date=date(2022, 1, 1), isbn="1234567890123", publisher=self.publisher)
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")

    def test_create_review(self):
        review = Review.objects.create(content="Great book!", rating=5, creator=self.user, book=self.book)
        self.assertEqual(review.content, "Great book!")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.creator, self.user)
        self.assertEqual(review.book, self.book)

    def test_review_str_representation(self):
        review = Review.objects.create(content="Another review", rating=4, creator=self.user, book=self.book)
        self.assertEqual(str(review), "testuser - Sample Book")



