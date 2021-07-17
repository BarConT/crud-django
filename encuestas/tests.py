from django.test import TestCase

# Create your tests here.

class MyIntegrationTest(TestCase):

    def setUp(self) -> None:
        '''
            Inicializa el set de pruebas.
        '''
        return super().setUp()
    
    def testHelloWrold(self):
        pass
        response = self.client.get("/saludo/")
        self.assertContains(response , "Hello World from Django for Codo a Codo 4.0")
       
    def testSatusCodeHelloWorld(self):
        response = self.client.get("/saludo/")
        self.assertEqual(response.status_code, 200 )