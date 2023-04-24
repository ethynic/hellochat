var cookies = document.cookie
console.log(cookies)

if (cookies.indexOf("user_name") == -1 || cookies[user_name] == ''){
    window.location.replace("/");
}




