function getCookies(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function getUserName(){
    return getCookies("username");
}

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function logout(){
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++)
      deleteCookie(cookies[i].split("=")[0]);
    window.location = "http://groupspaceuiuc.com/index.html";
 }

function getRequests() {
    var s1 = location.search.substring(1, location.search.length).split('&'),
        r = {}, s2, i;
    for (i = 0; i < s1.length; i += 1) {
        s2 = s1[i].split('=');
        r[decodeURIComponent(s2[0]).toLowerCase()] = decodeURIComponent(s2[1]);
    }
    return r;
};
function getTranditionalPlaceName(originalName) {
    if (originalName.includes("Grainger")){
        return "Grainger Library";
    }
    if (originalName.includes("Health")){
        return "SSHEL Library";
    }
    if (originalName.includes("Funk")){
        return "Funk ACES Library";
    }
    return originalName;
}
function getLidFromName(name){
    if (name.includes("Grainger")){
        return "0";
    }
    if (name.includes("Undergraduate")){
        return "1";
    }
    if (name.includes("Funk")){
        return "2";
    }
    if (name.includes("Main")){
        return "3";
    }
    if (name.includes("Health")){
        return "4";
    }
}
