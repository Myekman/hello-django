from django.test import TestCase

# Create your tests here.

class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

        # run test : python3 manage.py test todo.test.views

     def test_get_edit_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')


    #  def test_get_todo_list(self):

    #  def test_get_todo_list(self):



