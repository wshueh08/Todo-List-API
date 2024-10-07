import unittest
from app import app
from extensions import db
from flask import json

class AuthTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


        with app.app_context():
            db.create_all()

    def tearDown(self):
   
        with app.app_context():
            db.drop_all()

    def test_register_user(self):
        response = self.app.post('/auth/register',
                                 data=json.dumps(dict(name='Test User', email='testuser@example.com', password='password')),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('token', data)

    def test_login_user(self):
    
        self.app.post('/auth/register',
                      data=json.dumps(dict(name='Test User', email='testuser@example.com', password='password')),
                      content_type='application/json')
    
        response = self.app.post('/auth/login',
                                 data=json.dumps(dict(email='testuser@example.com', password='password')),
                                 content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', data)

if __name__ == "__main__":
    unittest.main()
