exports.regists=function(req,res,name,password){
    var sql="insert into stuinfo(name,password) values(?,?)";
    conn.query(sql,[name,password],function(err,result){
        if(result.affectedRows==1){
            req.session.name=name;
            res.sendfile('./public/view.html')
        }
    })
};
exports.login=login;