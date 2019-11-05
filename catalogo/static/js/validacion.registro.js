function validarForm()
{
	//alert("Validando");
	var verificar = true;
	var expRegNombre=/^[a-zA-ZÑñÁáÉéÍíÓóÚúÜü\s]+$/;
	var expRegEmail=/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;

	var formulario = document.getElementById("contacto_frm");
	var nombre = document.getElementById("inputNombre");
	var usuario = document.getElementById("inputUsername");
	var email = document.getElementById("inputEmail");
	var clave1 = document.getElementById("inputPassword");
    var clave2 = document.getElementById("inputConfirmPassword");

	if(!nombre.value)
	{
		alert("El campo nombre es requerido");
		nombre.focus();
		verificar = false;
	}
	else if(!expRegNombre.exec(nombre.value))
	{
		alert("El campo nombre solo acepta letras y espacios en blanco");
		nombre.focus();
		verificar=false;
	}
	else if(!email.value)
	{
		alert("El campo email es requerido");
		email.focus();
		verificar = false;
	}
	else if(!expRegEmail.exec(email.value))
	{
		alert("El campo email no es valido");
		email.focus();
		verificar=false;
	}
	else if(!clave1.value == clave2.value){
		alert("Las claves son distintas");
		verificar=false;
	}
	if(verificar)
	{
		alert("Se ha registrado el usuario");
		document.contacto_frm.submit();
	}
}


window.onload = function()
{
	var botonEnviar;
	botonEnviar = document.contacto_frm.enviar_btn;
	botonEnviar.onclick = validarForm;
}