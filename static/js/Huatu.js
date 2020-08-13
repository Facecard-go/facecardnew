/**
本模块为ajax请求
author:原也
create date:2020-8-10
update date:2020-8-13
**/
$("#show3").click(function () {
    var xiao=$("#catelogeid").val()
    $.ajax({
        url:"/show2",
        type:"post",
        data:{"xiao":xiao},
        success:function(datas){
            console.log(datas)
            ec_CX_option.xAxis.data=datas['bb']
            ec_CX_option.series.data=datas['cc']
            ec_ChangX.setOption(ec_CX_option)
        },
        error:function () {
        }
})
    })
$("#user_search").click(function () {
    var user__id=$("#user__id").val()
    // alert(user__id)
    $.ajax({
        url:"/showuser",
        type:"post",
        data:{"user__id":user__id},
        success:function(datas){
            console.log(datas)
            abcd=datas['dd']
            alert(abcd)
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

