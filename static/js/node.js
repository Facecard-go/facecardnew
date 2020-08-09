/*exports.login=function(req,res){
    var username=req.body.uname;
    var ped=req.body.psd;
    var sql="select * from myuser where uname=? and upwd=?";
    var con=dbcon.getCon();
        con.query(sql,[uname,upwd],function(err,result){
            if(!err){
                if(result.length==0){
                    res.json(0);
                }else{
                    res.json(1)
               }else{
                    console.log(err)
                }
                con.destroy()
            }
        })
}

exports.register=function(req,res,name,password){
    var aql="insert into stuinfo(name,password) values(?,?)"
    conn.query(sql,[uname,upwd],function(err,result){
        if(result.affectedRows==1){
            req.session.name=name;
           res.sendfile('../zhuye.html')
        }
    })
}
exports.login=login;
*/