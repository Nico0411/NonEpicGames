var x;
x=$(document);
x.ready(inicializarEventos);

function inicializarEventos()
{
  var x;
  x=$("#titulo1");          //recuperamos selectores 
  x.click(presionTitulo1)   //invocamos método click el cual ejecuta una función. 
  x=$("#titulo2");
  x.click(presionTitulo2)
  x=$("tr");
  x.click(presionFila);
  x=$("#boton1");
  x.click(resaltar);
}

function presionTitulo1()
{
  var x;
  x=$("#titulo1");
  x.css("color","#BA4A00");
  x.css("background-color","#D1F2EB");
  x.css("font-family","Courier");
}

function presionTitulo2()
{
  var x;
  x=$("#titulo2");
  x.css("color","#ffff00");
  x.css("background-color","#D1F2EB");
  x.css("font-family","Arial");
}

function presionFila()
{
  var x;
  x=$(this);              //this permite hacer referencia al elemento que activo el evento.
  x.css("background-color","#D6EAF8");
}

function resaltar()
{
  var x;
  x=$(".resaltado");
  x.css("background-color","#ffff00");
}



