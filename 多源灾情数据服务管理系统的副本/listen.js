var http = require('http');
var exec = require("child_process").exec;
var execSync = require('child_process').execSync;
// 创建createServer方法用于接受http客户端请求及返回响应的http服务器程序
http.createServer(function (req,res){
    exec('python exportdata.py',function(error,stdout,stderr){
        res.setHeader("Access-Control-Allow-Origin", "*");
        res.setHeader("Access-Control-Allow-Headers", "*");
        res.setHeader("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
        res.setHeader("X-Powered-By", ' 3.2.1');
        res.setHeader("Content-Type", "application/json;charset=utf-8");
        console.log(error);
        console.log(stdout);
        res.end(stdout);
    })
}).listen(8008);
