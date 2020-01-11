function errors(dom_id, error_text, dom_display) {
    // 为用户呈现错误信息
    document.getElementById(dom_id).innerHTML = error_text;
    document.getElementById(dom_id).style.display = dom_display;
}

function SendEmail() {
    let xmlhttp, url;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();
    }
    else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    url = "/users/send-mail/";
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            if (xmlhttp.responseText == "OK") {
                errors("seError", "", "none");
            }
            else {
                errors("seError", '发送邮件失败，点击下方链接重试', "");
            }
        }
    }
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}


function SaveEmail(str) {
    if (str) {
        verify_code = str;

        let xmlhttp, url;
        if (window.XMLHttpRequest) {
            xmlhttp = new XMLHttpRequest();
        }
        else {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        url = "/users/check/verify-code/?d="+verify_code;
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                if (xmlhttp.responseText == "false") {
                    errors("cdError", "验证码不正确", "");
                }
                else {
                    errors("cdError", "", "none");
                }
            }
        }
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
    }
    else {
        errors("cdError", "验证码不可为空", "");
    }
}
