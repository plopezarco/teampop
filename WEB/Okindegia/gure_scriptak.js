function pasahitzaKonprobatu() {
    var erabiltzaileak = [
        { user: "Pablo", pass: "1234" },
        { user: "Admin", pass: "Admin123" },
    ];

    var user = document.getElementById("username").value;
    var pass = document.getElementById("password").value;

    erabiltzaileak.forEach((element) => {
        if (element.user == user && element.pass == pass) {
            window.open(
                "file:///C:/Users/lopez.pablo/Documents/GitHub/teampop/JS/login.html",
                "_self"
            );
        }
    });
    document.getElementById("wrong").style.display = "block";
}

function login() {
    var erabiltzaileak = [
        { user: "Pablo", pass: "1234" },
        { user: "Admin", pass: "Admin123" },
    ];

    var user = prompt("Sartu erabiltzailea:");
    if (user == null) {
        return
    }
    var pass = prompt("Sartu pasahitza:");
    if (pass == null) {
        return
    }

    erabiltzaileak.forEach((element) => {
        if (element.user == user && element.pass == pass) {
            sessionStorage.Izena = element.user;
            sessionStorage.Loged = "true";
            alert("Ongi etorri, " + sessionStorage.Izena);
            document.getElementById("login1").style.display = "none";
            document.getElementById("login2").style.display = "none";
            document.getElementById("logout1").style.display = "block";
            document.getElementById("logout2").style.display = "block";
            document.getElementById("saskia1").style.display = "block";
            document.getElementById("saskia2").style.display = "block";
            return;
        }
    });

    if (sessionStorage.Loged != "true") {
        alert("Saiatu berriz");
    }
}

function logout() {
    sessionStorage.Izena = null;
    sessionStorage.Loged = false;
    document.getElementById("login1").style.display = "block";
    document.getElementById("login2").style.display = "block";
    document.getElementById("logout1").style.display = "none";
    document.getElementById("logout2").style.display = "none";
    document.getElementById("saskia1").style.display = "none";
    document.getElementById("saskia2").style.display = "none";
}

function data() {
    var date_regex = /^(0?[1-9]|[12][0-9]|3[01])[/-](0?[1-9]|1[012])[/-]\d{4}$/;
    do {
        var data = prompt("Sartu data bat (dd/mm/aaaa) formatuan:");
        if (!date_regex.test(data)) {
            alert("Gaizki sartu duzu.");
        }
    } while (!date_regex.test(data));
}

function erosketa() {
    var r = /^\+?(0|[1-9]\d*)$/;
    var bezero_izena = prompt("Sartu zure izena:");
    var saski_num;
    do {
        saski_num = prompt("Sartu erosiko dituzun produktu kopurua:");
    } while (!r.test(saski_num));

    var produktuak = [];
    for (var i = 0; i < saski_num; i++) {
        var izena = prompt("Sartu " + (parseInt(i) + 1) + ". produktua: ");
        var kopurua, prezioa;
        do {
            kopurua = prompt("Sartu " + izena + " kopurua: ");
        } while (!r.test(kopurua));
        do {
            prezioa = prompt("Sartu " + izena + " prezioa: ");
        } while (!r.test(prezioa));
        produktuak.push({ izena: izena, kopurua: kopurua, prezioa: prezioa });
    }

    var mezua = bezero_izena + ", hau da zure erosketa saskia: \n         ";
    produktuak.forEach((element) => {
        mezua += element.izena + ", Unitateak: " + element.kopurua + "\n         ";
    });
    alert(mezua);

    kalkulatuPrezioa(produktuak);
}

function bezeroaGorde() {
    var bezero_izena = prompt("Sartu zure izena:");
    var bezero_abizena = prompt("Sartu zure abizena:");
    var txartela = prompt("Sartu zure txartela:");
    var helbidea = prompt("Sartu zure helbidea:");

    alert(
        "Izen osoa: " +
        bezero_izena +
        " " +
        bezero_abizena +
        "\n           Txartela: " +
        txartela +
        "\n           Helbidea: " +
        helbidea
    );
}

function kalkulatuPrezioa(produktuak) {
    var totala = 0;
    produktuak.forEach((element) => {
        totala += element.prezioa;
    });

    alert("Erosketaren totala: " + totala);
}

var mybutton = document.getElementById("scroll_top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

if (sessionStorage.Loged == "true") {
    document.getElementById("login1").style.display = "none";
    document.getElementById("login2").style.display = "none";
    document.getElementById("logout1").style.display = "block";
    document.getElementById("logout2").style.display = "block";
    document.getElementById("saskia1").style.display = "block";
    document.getElementById("saskia2").style.display = "block";
} else {
    document.getElementById("login1").style.display = "block";
    document.getElementById("login2").style.display = "block";
    document.getElementById("logout1").style.display = "none";
    document.getElementById("logout2").style.display = "none";
    document.getElementById("saskia1").style.display = "none";
    document.getElementById("saskia2").style.display = "none";
}