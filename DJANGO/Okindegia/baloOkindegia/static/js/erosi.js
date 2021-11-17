$(document).ready(function() {
    $(".plus").click(function() {
        kantitateaGehitu(this.id)
    });
    $(".minus").click(function() {
        kantitateaKendu(this.id)
    });
    $("#erosi-btn").click(function() {
        checkout()
    });
    $("#data-ordua").change(function() {
        dataKonprobatu($(this).val())
    })
    dataSartu()
});
window.onload = function() {
    produktuakGehituListara()
};

var tot = 0

function produktuakGehituListara() {
    var produktuTaula = document.getElementById('erosi-lista')
    produktuTaula.innerHTML = ""
    produktuLista = localStorageIrakurri()
    tot = 0
    if (produktuLista.length > 0) {
        produktuLista.forEach(element => {
            const div = document.createElement('div')
            div.classList = "row"
            div.innerHTML = `<div class="col-12 col-sm-12 col-md-2 text-center">
        <img class="img-responsive" src="${element.irudia}" alt="prewiew" width="100%">
    </div>
    <div class="col-12 text-sm-center col-sm-12 text-md-left col-md-6">
        <h4 class="product-name"><strong>${element.izena}</strong></h4>
        <h4>
        <small>${element.prezioa}€</small>
        </h4>
    </div>
    <div class="col-12 col-sm-12 text-sm-center col-md-4 text-md-right row">
        <div class="col-3 col-sm-3 col-md-6 text-md-right" style="padding-top: 5px">
            <h6><strong>${(element.prezioa * element.kopurua).toFixed(2)}<span class="text-muted">€</span></strong></h6>
        </div>
        <div class="col-4 col-sm-4 col-md-4">
            <div class="quantity">
                <input type="button" value="+" class="plus" id="plus-${element.id}">
                <input type="number" value="${element.kopurua}" title="Kopurua" class="qty" id="kopurua-${element.id}" size="4" readonly>
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
            tot += (element.prezioa * element.kopurua)
        });
    } else {
        const div = document.createElement('div')
        div.classList = "row"
        div.innerHTML = `<div class="col-12 col-sm-12 col-md-2 text-center">Ez dago produkturik</div>`
        produktuTaula.appendChild(div)
    }
    document.getElementById('prezio-totala').innerHTML = tot.toFixed(2) + "€"
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

function produktuaAldatu(id, kopurua) {
    produktuLista = localStorageIrakurri()
    produktuLista.forEach(function(element, index) {
        if (element.id == id) {
            element.kopurua = kopurua
        }
    });
    localStorage.setItem('produktuak', JSON.stringify(produktuLista))
    saskiaIkusi()
}

function checkout() {
    $.ajax({
        type: 'POST',
        url: "/check_login/",
        data: { csrfmiddlewaretoken: csrftoken },
        success: function(response) {
            erosi()
        },
        error: function(response) {
            $("#modal-login").show()
        }
    })
}

function erosi() {
    var div = document.getElementById("ordaindu")
    produktuLista = localStorageIrakurri()
    if (produktuLista.length > 0) {
        var btn = document.getElementById('erosi-btn')
        btn.removeAttribute('data-target')
        btn.removeAttribute('data-toggle')
        if (dataKonprobatu(document.getElementById("data-ordua").value)) {
            btn.setAttribute('data-target', "#staticBackdrop")
            btn.setAttribute('data-toggle', "modal")
            if (div.innerHTML.trim() === '') {
                div.innerHTML = `<div class="modal fade" id="staticBackdrop" data-backdrop="static" data-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-body">
                        <div class="text-right"> <i class="fa fa-close close" data-dismiss="modal"></i> </div>
                        <div class="tabs mt-3">
                            <ul class="nav nav-tabs" id="myTab" role="tablist">
                                <li class="nav-item" role="presentation"> <a class="nav-link active" id="visa-tab" data-toggle="tab" href="#visa" role="tab" aria-controls="visa" aria-selected="true"> <img src="https://i.imgur.com/sB4jftM.png" width="80"> </a> </li>
                                <li class="nav-item" role="presentation"> <a class="nav-link" id="paypal-tab" data-toggle="tab" href="#paypal" role="tab" aria-controls="paypal" aria-selected="false"> <img src="https://i.imgur.com/yK7EDD1.png" width="80"> </a> </li>
                            </ul>
                            <div class="tab-content" id="myTabContent">
                                <div class="tab-pane fade show active" id="visa" role="tabpanel" aria-labelledby="visa-tab">
                                    <div class="mt-4 mx-4">
                                        <div class="text-center">
                                            <h5>Kreditu Txartela</h5>
                                        </div>
                                        <div class="form mt-3">
                                            <div class="inputbox"> <input type="text" name="name" autocomplete="off" maxlength="50" class="form-control" required="required"> <span>Izen Abizenak</span> </div>
                                            <div class="inputbox"> <input type="text" id="txartela-input" name="name" maxlength="19" autocomplete="off" class="form-control" required="required"> <span>Txartel Zenbakia</span> <i class="fa fa-eye"></i> </div>
                                            <div class="d-flex flex-row">
                                                <div class="inputbox"> <input type="text" id="iraungitze-data-input" name="name" maxlength="5" autocomplete="off" class="form-control" required="required"> <span>Iraungitze Data</span> </div>
                                                <div class="inputbox"> <input type="text" name="name" maxlength="3" autocomplete="off" class="form-control" required="required"> <span>CVV</span> </div>
                                            </div>
                                            <div class="px-5 pay"> <button class="btn btn-success btn-block">Ordaindu</button> </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="tab-pane fade" id="paypal" role="tabpanel" aria-labelledby="paypal-tab">
                                    <div class="px-5 mt-5">
                                        <div class="inputbox"> <input type="text" name="name" class="form-control" required="required"> <span>Paypal Email Helbidea</span> </div>
                                        <div class="pay px-5"> <button class="btn btn-primary btn-block">Ordaindu</button> </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>`
                $('.pay').click(function(e) {
                    ordaindu()
                });
                btn.click();
            }
            $('#txartela-input').on('input', function(e) {
                var val = $(this).val();
                var newval = '';
                val = val.replace(/\D/g, '');
                val = val.replace(/\s/g, '');
                for (var i = 0; i < val.length; i++) {
                    if (i % 4 == 0 && i > 0) newval = newval.concat(' ');
                    newval = newval.concat(val[i]);
                }
                $(this).val(newval);
            });
            $('#iraungitze-data-input').on('input', function(e) {
                var val = $(this).val();
                var newval = '';
                val = val.replace(/\W/g, '');
                for (var i = 0; i < val.length; i++) {
                    if (i % 2 == 0 && i > 0) newval = newval.concat('/');
                    newval = newval.concat(val[i]);
                }
                $(this).val(newval);
            });
        }
    } else {
        Swal.fire('Kontuz!',
            'Ez daukazu produkturik',
            'warning')
    }
}

function dataSartu() {
    var data_ordua = document.getElementById("data-ordua")
    var min = new Date()
    min.setHours(min.getHours() + 2)
    min.setMinutes(min.getMinutes() + 1)
    var max = new Date()
    max.setMonth(max.getMonth() + 1)
    data_ordua.setAttribute("value", min.toISOString().slice(0, 16))
    data_ordua.setAttribute("min", min.toISOString().slice(0, 16))
    data_ordua.setAttribute("max", max.toISOString().slice(0, 16))
}

function dataKonprobatu(data_var) {
    var data = new Date(data_var)
    var orain = new Date()
    orain.setHours(orain.getHours() + 1)
    if (data < orain) {
        Swal.fire('Kontuz!',
            'Eguna eta ordua ezin da ' + orain.toLocaleString() + ' baino lehenago izan!',
            'warning')
        return false
    }
    return true

}

function ordaindu() {
    $.ajax({
        type: 'POST',
        url: "/ordaindu/",
        data: { csrfmiddlewaretoken: csrftoken, produktuak: JSON.stringify(localStorageIrakurri()), totala: tot },
        success: function(response) {
            Swal.fire('Eskerrik asko', 'Zure erosketa ondo gauzatu da. Eskerrik asko', 'success')
            localStorageBorratu()
        },
        error: function(response) {
            Swal.fire('Errorea', 'Errore ezezagun bat gertatu da', 'error')
        }
    })
}