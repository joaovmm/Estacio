const form = document.querySelector("#form")
const nomesobinput = document.querySelector("#nomesobrenome")
const enderecoinput = document.querySelector("#endereco")
const telinput = document.querySelector("#telefone")
const observacaoinput = document.querySelector("#observacao")
const produtoselect = document.querySelector("#produtoId")
const quantnumber = document.querySelector("#quant")

form.addEventListener("submit", (event) => {
    event.preventDefault();


    if(nomesobinput.value === ""){
        alert("Por Favor, Preencha seu nome");
        return;
    }
    if(enderecoinput.value === ""){
        alert("Por Favor, informe seu endereço");
        return;
    }
    if(telinput.value === ""){
        alert("Por Favor, informe seu telefone/celular");
        return;
    }
    if(produtoselect.value === "1"){
        alert("Por Favor, escolha um sabor");
        return;
    }
    if(quantnumber.value === ""){
        alert("Por Favor, escolha a quantidade");
        return;
    }
    form.submit();
});