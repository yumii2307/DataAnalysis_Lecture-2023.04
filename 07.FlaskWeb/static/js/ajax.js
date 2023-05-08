// AJAX(Asynchronous Javascript and XML)
// Web page의 일부분만 변경하는 방법
function changeQuote() {
    $.ajax({
        type: 'GET',
        url: '/change_quote',
        data: ' ',                      // 서버로 전달할 데이터
        success: function(msg) {        // msg: 서버로부터 받은 데이터
            $('#quoteMsg').html(msg);
        }
    })
    $('#quoteMsg').html('새로운 명언입니다.');
}
function changeAddr() {
    $('#addrInput').attr('class', 'mt-2');       // input box가 보이게
}
function addrSubmit() {
    $('#addrInput').attr('class', 'mt-2 d-none');    // input box가 안보이게
    let addr = $('#addrInputTag').val();
    $.ajax({
        type: 'GET',
        url: '/change_addr',
        data: {addr: addr},
        success: function(msg) {
            $('#addr').html(msg);
        }
    })
}
function copyToClipboard(val) {
    var t = document.createElement("textarea");
    document.body.appendChild(t);
    t.value = val;
    t.select();
    document.execCommand('copy');
    document.body.removeChild(t);
}
function changeWeather() {
    let addr = $('#addr').text();
    $.ajax({
        type: 'GET',
        url: '/weather',
        data: {addr: addr},
        success: function(result) {
            $('#weather').html(result);
        }
    })
}