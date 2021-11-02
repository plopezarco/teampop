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
    $("#modal-login").click(function() {
        document.getElementById("modal-login").style.display = "none";
    });
    $("#login-btn").click(function() {
        document.getElementById("modal-login").style.display = "block";
    });
});