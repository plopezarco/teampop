$(document).ready(function() {
    $(".plus").click(function() {
        kantitateaGehitu(this.id)
    });
    $(".minus").click(function() {
        kantitateaKendu(this.id)
    });
});
window.onload = function() {
    produktuakGehituListara()
};

function produktuakGehituListara() {
    var produktuTaula = document.getElementById('erosi-lista')
    produktuTaula.innerHTML = ""
    produktuLista = localStorageIrakurri()
    produktuLista.forEach(element => {
        const div = document.createElement('div')
        div.classList = "row"
        div.innerHTML = `<div class="col-12 col-sm-12 col-md-2 text-center">
        <img class="img-responsive" src="${element.irudia}" alt="prewiew" width="120">
    </div>
    <div class="col-12 text-sm-center col-sm-12 text-md-left col-md-6">
        <h4 class="product-name"><strong>${element.izena}</strong></h4>
        <h4>
            <small>Deskripzioa</small>
        </h4>
    </div>
    <div class="col-12 col-sm-12 text-sm-center col-md-4 text-md-right row">
        <div class="col-3 col-sm-3 col-md-6 text-md-right" style="padding-top: 5px">
            <h6><strong>${element.prezioa} <span class="text-muted"></span></strong></h6>
        </div>
        <div class="col-4 col-sm-4 col-md-4">
            <div class="quantity">
                <input type="button" value="+" class="plus" id="plus-${element.id}">
                <input type="number" value="${element.kopurua}" title="Kopurua" class="qty" id="kopurua-${element.id}" size="4">
                <input type="button" value="-" class="minus" id="minus-${element.id}">
            </div>
        </div>
        <div class="col-2 col-sm-2 col-md-2 text-right">
            <button type="button" class="btn btn-outline-danger btn-xs produktua-ezabatu" data-id="${element.id}">
                         <i class="fa fa-trash" aria-hidden="true"></i>
                     </button>
        </div>
    </div>`
        produktuTaula.appendChild(div)
        produktuTaula.appendChild(document.createElement('hr'))
    });
}

function kantitateaGehitu(id) {
    var id = id.split("-")[1]
    document.getElementById("kopurua-" + id).value++;
    produktuaAldatu(id, document.getElementById("kopurua-" + id).value)
}

function kantitateaKendu(idProd) {
    var id = idProd.split("-")[1]
    if (document.getElementById("kopurua-" + id).value > 1)
        document.getElementById("kopurua-" + id).value--;
    produktuaAldatu(id, document.getElementById("kopurua-" + id).value)
}