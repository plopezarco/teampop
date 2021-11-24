$(document).ready(function() {
    $(".saskira-gehitu").click(function() {
        produktuaGehitu(this.id)
    });
    $(".saskia-erakutsi").click(function() {
        saskiaIkusi()
    });
    $("#saskia-hustu").click(function() {
        localStorageBorratu()
    });
    $("#modal-login").on('click', function(e) {
        if (!(($(e.target).closest("#modal-content").length > 0))) {
            $("#modal-login").hide();
        }
    });
    $("#login-btn, #login-btn2").click(function() {
        $("#modal-login").show();
    });
    $(".filters").click(function() {
        produktuakFiltratu(this.id)
    });
    $(".produktua-ezabatu").click(function() {
        produktuaEzabatu($(this).data("id"))
    });
    $("#login-form").submit(function(e) {
        e.preventDefault()
        erabiltzailea = document.forms["login-form"]["erabiltzailea-login"].value
        pasahitza = document.forms["login-form"]["pasahitza-login"].value
        login(erabiltzailea, pasahitza)
    });
    $("#register-form").submit(function(e) {
        e.preventDefault()
        register(document.forms["register-form"])
    });
    $("#mezua-form").submit(function(e) {
        e.preventDefault()
        $("#mezua-bidali").attr("disabled", true);
        mezuaBidali(document.forms["mezua-form"])
        document.forms["mezua-form"].reset()
    });

});
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    var mybutton = document.getElementById("scroll_top");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

function produktuakFiltratu(filtroa) {
    $.ajax({
        type: 'POST',
        url: "/produktuakfiltratu/",
        data: { csrfmiddlewaretoken: csrftoken, kategoria: filtroa },
        success: function(response) {
            produktuakErakutsi(response)
        },
        error: function(response) {
            alert("Ezin da aldatu. Saiatu beranduago" + response);
        }
    })
}

function produktuakErakutsi(response) {
    produktuakLista = response.produktuak
    document.getElementById("produktu-lista").innerHTML = ""
    produktuakLista.forEach(p => {
        const div = document.createElement('div')
        div.classList = "col-md-6 col-lg-6 col-xl-4"
        div.innerHTML = `<div class="single-product">
            <div class="part-1">
                <img id="produktu-irudia-${p.id}" src="${p.irudia}">
                <ul>
                    <li><a href="#0" id="${p.id}" class="saskira-gehitu"><i class="icon fa fa-shopping-cart"></i></a></li>
                    <li><a href="#0" data-toggle="modal" data-target="#produktu${p.id}"><i class="icon fa fa-expand"></i></a></li>
                </ul>
            </div>
            <div class="modal fade bd-example-modal-lg" id="produktu${p.id}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
                    <div class="modal-content">
                        <img src="${p.irudia}">
                        <div class="modal-body">
                            <h3 class="product-title">${p.izena}</h3>
                            <h4 class="product-price">${p.prezioa.toFixed(2)}€</h4>
                        </div>
                    </div>
                </div>
            </div>
            <div class="part-2">
                <h3 id="produktu-izena-${p.id}" class="product-title">${p.izena}</h3>
                <h4 id="produktu-prezioa-${p.id}" class="product-price">${p.prezioa.toFixed(2)}</h4><span class="product-price">€</span>
            </div>
        </div>`
        document.getElementById("produktu-lista").appendChild(div)
    });
    $(".saskira-gehitu").click(function() {
        produktuaGehitu(this.id)
    });
}

function login(erabiltzailea, pasahitza) {
    $.ajax({
        type: 'POST',
        url: "/user_login/",
        data: { csrfmiddlewaretoken: csrftoken, erabiltzailea: erabiltzailea, pasahitza: pasahitza },
        success: function(response) {
            location.reload()
        },
        error: function(response) {
            Swal.fire('Kontuz!',
                'Erabiltzaile edo pasahitza okerrak',
                'error')
        }
    })
}

function register(form) {
    document.getElementById("register-btn").setAttribute("disabled", "")
    var user = {
        izena: form["izena"].value,
        abizena: form["abizena"].value,
        email: form["email"].value,
        erab: form["erabiltzailea-register"].value,
        pass1: form["pasahitza-register"].value,
        pass2: form["pasahitza-register-2"].value
    }
    if (user.pass1 === user.pass2) {
        $.ajax({
            type: 'POST',
            url: "/register/",
            data: { csrfmiddlewaretoken: csrftoken, user: JSON.stringify(user) },
            success: function(response) {
                document.getElementById("register-btn").removeAttribute("disabled")
                location.reload()
            },
            error: function(response) {
                if (response.status == 409)
                    Swal.fire('Kontuz!',
                        'Emaila edo erabiltzailea dagoeneko erabilita dago',
                        'warning')
                else
                    Swal.fire('Errorea!',
                        'Errore ezezagun bat gertatu da',
                        'error')
            }
        })
    } else {
        Swal.fire('Kontuz!', 'Pasahitza biak berdinak izan behar dira', 'warning')
    }
}

function mezuaBidali(form) {
    izena = form["izena"].value
    email = form["email"].value
    mezua = form["mezua"].value
    $.ajax({
        type: 'POST',
        url: "/mezuagorde/",
        data: { csrfmiddlewaretoken: csrftoken, izena: izena, email: email, mezua: mezua },
        success: function(response) {
            Swal.fire('Ederto!',
                'Zure mezua gorde da, eskerrik asko!',
                'success')
            $("#mezua-bidali").attr("disabled", false);
        },
        error: function(response) {
            Swal.fire('Errorea!',
                'Errore ezezagun bat gertatu da',
                'error')
        }
    })
}