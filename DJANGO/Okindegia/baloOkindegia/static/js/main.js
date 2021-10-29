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
});