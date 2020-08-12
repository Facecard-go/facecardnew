$("#show3").click(function () {
    alert("hello")
    var xiao=$("#catelogeid").val()
    $.ajax({
        url:"/show2",
        type:"post",
        data:{"xiao":xiao},
        success:function(datas){
            console.log(datas)
            ec_CX_option.xAxis[0].data=datas['bb']
            ec_CX_option.series[0].data=datas['cc']
            ec_ChangX.setOption(ec_CX_option)
        },
        error:function () {
        }
})
    })




    $("#show_t").click(function () {
        var ca=$("#cateloge_id").val()
        $.ajax({
            url:"/show1",
            type:"post",
            data:{"abc":ca},
            // dataType:'json',
            success:function(datas){
                console.log(datas)
                ec_Jijie_option.series[0].data=datas['aa']
                ec_Jijie.setOption(ec_Jijie_option)
            },
            error:function () {
            }
        })
        })

//定时器
