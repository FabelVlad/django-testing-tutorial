from django.test import SimpleTestCase

from budget.forms import ExpenseForm


class TestForms(SimpleTestCase):
    def test_validation(self):
        form = ExpenseForm(data={
            'title': 'expense1',
            'amount': 2000,
            'category': 'development'
        })
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form = ExpenseForm(data={
            'title': '',
            'amount': 2000,
            'category': 'development'
        })
        self.assertFalse(form.is_valid())
