import unittest
from app import app
from extensions import db
from flask import json
from flask_jwt_extended import create_access_token

class TodoTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        with app.app_context():
            db.create_all()
      
            self.app.post('/auth/register',
                          data=json.dumps(dict(name='Test User', email='testuser@example.com', password='password')),
                          content_type='application/json')
            self.token = create_access_token(identity=1)

    def tearDown(self):
  
        with app.app_context():
            db.drop_all()

    def test_create_todo_item(self):
        response = self.app.post('/api/todos',
                                 headers={'Authorization': f'Bearer {self.token}'},
                                 data=json.dumps(dict(title='Test Todo', description='Test Description')),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['title'], 'Test Todo')

    def test_get_todo_items(self):

        self.app.post('/api/todos',
                      headers={'Authorization': f'Bearer {self.token}'},
                      data=json.dumps(dict(title='Test Todo', description='Test Description')),
                      content_type='application/json')

        response = self.app.get('/api/todos',
                                headers={'Authorization': f'Bearer {self.token}'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 1)

if __name__ == "__main__":
    unittest.main()

