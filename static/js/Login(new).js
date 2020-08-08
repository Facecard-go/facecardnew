exports.login =function(req,res){
    var username=req.body.uname;
    var pwd=req.body.password1;
    var sql="select * from myuser where uname=? and password1=?";
    var con=dbcon.getCon();
    con.query(sql,[uname,password1], function (err,result) {
          if(!err){
              if(result.length==0){
                  res.json(0);
              }else{
                  res.json(1)
              }
          }else{
             console.log(err)
          }
        con.destroy()
    })
};