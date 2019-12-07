# NonEpicGames
Proyecto prueba 2: NonEpicGames

La tienda de NonEpicGames es un proyecto realizado por tres estudiantes de segundo año de Duoc UC, para poder aprender a utilizar Django en la creación de paginas web.

NonEpicGames no se encuentra relacionado de forma alguna con Epic Games™ o la Epic Games Store™.

Usuario del admin
User: Nico
Contraseña: Nicolasprats12

Pruebas (unittest):

Se realiza prueba con el modelo Game.
Se crean 2 variables para el modelo Developer(Foreign key) y otras 2 para el modelo Platform(Many_to_many).

Se crean 2 Juegos (Game) para hacer la pruebas.

--
La primera prueba test_game_developer sirve para verificar si el game Warframe, su developer es Digital Extrems.

La segunda prueba test_game_launch sirve para verificar si el game League of legends, su Launch es 11/05/2010.
   
Las pruebas son erroneas debido a que no se pudo instanciar correctamente la variable platform debido a que es Many_to_manyField.
************
TypeError: Direct assignment to the forward side of a many-to-many set is prohibited. Use platform.set() instead.
