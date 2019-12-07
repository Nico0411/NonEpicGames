function validarForm()
{
	//alert("Validando");
	var verificar = true;
	var expRegNombre=/^[a-zA-ZÑñÁáÉéÍíÓóÚúÜü\s]+$/;
	var expRegEmail=/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
	var formulario = document.getElementById("contacto_frm");
	var nombre = document.getElementById("id_name");
	var usuario = document.getElementById("id_username");
	var email = document.getElementById("id_email");
	var clave1 = document.getElementById("id_password1");
    var clave2 = document.getElementById("id_password2");
	
	if(!usuario.value)
	{
		alert("El campo usuario es requerido");
		nombre.focus();
		verificar = false;
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
	else if(!nombre.value)
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
	else if(!clave1.value)
	{
		alert("El campo clave es requerido");
		verificar = false;
	}
		else if(clave1.value.length < 8)
	{
		alert("El campo clave requiere almenos 8 caracteres");
		verificar = false;
	}
	else if(clave1.value != clave2.value)
	{
		alert("Las claves son distintas");
		verificar=false;
	}
	if(verificar)
	{
		alert("Se ha registrado el usuario");
		formulario.submit();
	}
}


window.onload = function()
{
	var botonEnviar;
	botonEnviar = document.contacto_frm.enviar_btn;
	botonEnviar.onclick = validarForm;
}
