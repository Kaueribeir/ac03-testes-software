import unittest
from unittest import mock
from blog import Blog

class TestBlog(unittest.TestCase):
    def test_posts(self):
        # cria um objeto mock para a resposta da API
        mock_response = mock.Mock()
        mock_response.json.return_value = [
            {'id': 1, 'title': 'Test post', 'body': 'Lorem ipsum'}]

        # substitui a função requests.get pela resposta mock
        with mock.patch('requests.get', return_value=mock_response):
            # cria um objeto Blog e chama a função posts
            blog = Blog()
            response = blog.posts()

            # verifica se a resposta é igual ao mock
            self.assertEqual(
                response, [{'id': 1, 'title': 'Test post', 'body': 'Lorem ipsum'}])

    def test_post_by_user_id(self):
        # Criamos um objeto mock da resposta da API
        mock_response = mock.Mock(status_code=200)
        mock_response.json.return_value = [
            {
                'id': 2,
                'title':'Post 2', 
                'userId': 2
            },
            {
                'id': 3, 
                'title': 'Post 3', 
                'userId': 3
            }
        ]
        

        # Criamos um objeto mock para a função requests.get
        with mock.patch('requests.get', return_value=mock_response):
            blog = Blog()
            response = blog.post_by_user_id(2)
            

        # Testamos se o retorno da função corresponde ao mock_response
        dado = response[0]
        self.assertEqual(dado['userId'], 2)

    def test_post_by_user_id_inexistente(self):
        #testando quando o id é inexistente
        mock_response = mock.Mock(status_code=200)
        mock_response.json.return_value = [ ]
        
        
        # Criamos um objeto mock para a função requests.get
        with mock.patch('requests.get', return_value=mock_response):
            blog = Blog()
            response = blog.post_by_user_id(2)
        
        self.assertEqual(response, [])
        
        
unittest.main()
