 def test_hello(self):
          rv = self.app.get('/')
 -        assert "Hello, World!" in rv.data
 +        assert "Hello, continuous delivery!" in rv.data
  
      def test_get_movie_nonexisting(self):
          response = self.app.get('/movies/1')
