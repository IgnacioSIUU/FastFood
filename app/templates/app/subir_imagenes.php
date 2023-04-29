{% load static %}
<!DOCTYPE html>
<html>
  <head>
    <title>Subir fotos a la página web</title>
    <link rel="stylesheet" href="{% static 'app/css/subir_img.css' %}">
  </head>
  <body>
    <h1>Subir fotos a la página web</h1>
    <form action="/subir" method="post" enctype="multipart/form-data">
      <label for="foto">Selecciona una foto para subir:</label><br>
      <input type="file" id="foto" name="foto"><br>
      <center><input type="submit" value="Subir foto"></center>
    </form>
  </body>
</html>