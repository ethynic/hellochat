var cookies = {
    "sessionid" : ''
};




if (!isLogin()){
    window.location.replace("login.html");
}

function isLogin(){
    if (!cookies["sessionid"]){
        return false;
    }
    return true;
}


function Login(){
    // 获取表单元素 
    var form = document.getElementById("login-form"); 
    var username = document.getElementById("username"); 
    var password = document.getElementById("password");

    // 监听表单提交事件 
    form.addEventListener("submit", function(event) { 
        // 阻止默认的表单提交行为 
        event.preventDefault(); 
        // 创建一个 XMLHttpRequest 对象 
        var xhr = new XMLHttpRequest(); 
        // 设置请求方法和地址 
        xhr.open("POST", "/login"); 
        // 设置请求头 
        xhr.setRequestHeader("Content-Type", "application/json"); 
        // 设置响应类型为 JSON 
        xhr.responseType = "json"; 
        // 设置响应事件处理函数 
        xhr.onload = function() { 
            // 如果响应状态码为 200，表示请求成功 
            if (xhr.status === 200) { 
                // 获取响应数据 
                var data = xhr.response; 
                // 如果响应数据的状态为 1，表示登录成功 
                if (data.status === 1) { 
                    // 获取响应数据中的 sessionid 
                    var sessionid = data.sessionid; 
                    // 将 sessionid 存到 cookie 中，设置过期时间为一天 
                    document.cookie = "sessionid=" + sessionid + ";max-age=86400"; 
                    // 跳转到主页或其他页面 
                    window.location.href = "/index.html"; } 
                else { 
                    // 否则，表示登录失败，显示错误信息 
                    alert(data.message); } } 
            else { 
                // 否则，表示请求失败，显示错误信息 
                alert("请求失败：" + xhr.statusText); } 
            }; 
                // 发送请求数据，将用户名和密码转换为 JSON 格式 
                xhr.send(JSON.stringify({ username: username.value, password: password.value })); 
    });
}

