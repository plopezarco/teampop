var produktuLista = localStorageIrakurri()

function produktuaGehitu(produktuId) {
    if (produktuId > 0) {
        const prod = {
            id: produktuId,
            izena: $("#produktu-izena-" + produktuId).text(),
            prezioa: $("#produktu-prezioa-" + produktuId).text(),
            irudia: $("#produktu-irudia-" + produktuId).attr('src'),
            kopurua: 1
        }
        var berria = true
        produktuLista = localStorageIrakurri()
        produktuLista.forEach(element => {
            if (element.id === produktuId) {
                element.kopurua++
                    berria = false
            }
        });
        if (berria) {
            produktuLista.push(prod)
        }
        localStorage.setItem('produktuak', JSON.stringify(produktuLista))
    }
}

function produktuaEzabatu(produktuId) {
    produktuLista = localStorageIrakurri()
    produktuLista.forEach(function(element, index) {
        if (element.id == produktuId) {
            produktuLista.splice(index, 1);
        }
    });
    localStorage.setItem('produktuak', JSON.stringify(produktuLista))
    saskiaIkusi()
}

function localStorageIrakurri() {
    if (localStorage.getItem('produktuak') === null) {
        produktuLista = []
    } else {
        produktuLista = JSON.parse(localStorage.getItem('produktuak'))
    }
    return produktuLista
}

function localStorageBorratu() {
    produktuLista = []
    localStorage.clear()
    produktuakGehituTaulara()
}

function saskiaIkusi() {
    produktuLista = localStorageIrakurri()
    var s = ""
    produktuakGehituTaulara()
    $(".produktua-ezabatu").click(function() {
        produktuaEzabatu($(this).data("id"))
    });
}

function produktuakGehituTaulara(taula) {
    var produktuTaula
    if (taula !== undefined) {
        produktuTaula = document.getElementById(taula)
    } else {
        produktuTaula = document.getElementById('saskia-lista-tbody')
    }
    produktuTaula.innerHTML = ""
    produktuLista = localStorageIrakurri()
    produktuLista.forEach(element => {
        const row = document.createElement('tr')
        row.innerHTML = `<td>
		<img src="${element.irudia}" width=100>
	</td>
	<td>${element.izena}</td>
	<td>${element.prezioa}</td>
	<td>${element.kopurua}</td>
	<td>
		<a href="#0" class="produktua-ezabatu" data-id="${element.id}"><i class="icon fa fa-times-circle"></i></a>
	</td>`
        produktuTaula.appendChild(row)
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');