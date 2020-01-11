let username, password1, password2;
let ajax_data;

window.onload = function() {
    if(navigator.cookieEnabled == true) {
        document.getElementById("btn").disabled = false;
        document.getElementById("ckError").style.display = "none";
      }
}

function errors(dom_id, error_text, dom_display) {
    // 为用户呈现错误信息
    document.getElementById(dom_id).innerHTML = error_text;
    document.getElementById(dom_id).style.display = dom_display;
}

function SaveUsername(str) {
    if (str) {
        username = str;
        ajax_data = username;

        // 使用 ajax 检查用户名是否已经被使用
        let xmlhttp, url;
        if (window.XMLHttpRequest) {
            xmlhttp = new XMLHttpRequest();
        }
        else {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        url = "/users/check/username/?d="+ajax_data;
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                if (xmlhttp.responseText == "false") {
                    errors("unError", "已存在一位使用该名字的用户", "");
                }
                else {
                    errors("unError", "", "none");
                }
            }
        }
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
    }
    else {
        errors("unError", "用户名不可为空", "");
    }
}

function SavePassword1(str) {
    if (str) {
        password1 = str;

        // 确定密码不是全部是数字
        if (isNaN(password1 * 1) == false) {
            errors("pw1Error", "密码不能全是数字", "");
        } 
        else {
            errors("pw1Error", "", "none");
        }
        // 确定密码长度大于 8 个字符
        if (password1.length < 8) {
            errors("pw1Error", "密码长度不足 8 个字符", "");
        } 
        else {
            errors("pw1Error", "", "none");
        }
        // 确定密码不与用户名太相似
        if (password1.length >= username.length) {
            let first = "", last = "", usernameLength = username.length; 
            for (let i = 0; i < usernameLength; i++) {
                first += password1[i];
            }
            for (let i = password1.length - usernameLength; i < password1.length; i++) {
                last += password1[i];
            }
            if (first==username || last==username) {
                errors("pw1Error", "密码与用户名太接近", "");
            } 
            else {
                errors("pw1Error", "", "none");
            }
        }
    }
    else {
        errors("pw1Error", "密码不可为空", "");
    }
}

function SavePassword2(str) {
  if (str) {
      password2 =str;
      if (password2 == password1) {
          errors("pw2Error", "", "none");
      } 
      else {
          errors("pw2Error", "两次输入的密码不一致", "");
      }
  }
  else {
      errors("pw2Error", "密码确认不可为空", "");
  }
}

function SaveEmail(str) {
    if (str) {
        let re = /^\w+@[a-zA-Z0-9]{2,10}(?:\.[a-z]{2,4}){1,3}$/;
        if (re.test(str)) {
            errors("emError", "", "none");
        } 
        else {
            errors("emError", "邮箱格式不匹配", "");
        }
    } 
    else {
      errors("emError", "电子邮件地址不可为空", "");
    }
    
}