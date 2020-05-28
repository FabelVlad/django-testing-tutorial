from django.test import TestCase

from budget.models import Project, Category, Expense


class TestModels(TestCase):
    def setUp(self):
        self.project1 = Project.objects.create(name='project 1', budget=10000)

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEquals(self.project1.slug, 'project-1')

    def test_budget_left(self):
        category1 = Category.objects.create(project=self.project1, name='development')
        Expense.objects.create(project=self.project1, title='expense1', amount=100, category=category1)
        Expense.objects.create(project=self.project1, title='expense2', amount=100, category=category1)
        self.assertEquals(self.project1.budget_left, 9800)

    def test_total_transactions(self):
        category1 = Category.objects.create(project=self.project1, name='development')
        Expense.objects.create(project=self.project1, title='expense1', amount=100, category=category1)
        Expense.objects.create(project=self.project1, title='expense2', amount=100, category=category1)
        self.assertEquals(self.project1.total_transactions, 2)

    def test_get_absolute_url(self):
        self.assertEquals(self.project1.get_absolute_url(), '/project-1')























