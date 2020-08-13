/**
本模块为echarts绘制畅销图
author:原也 刘益争
create date:2020-8-10
update date:2020-8-12
**/
var dom = document.getElementById("CX_tu");
    var ec_ChangX = echarts.init(dom);
    var add = {};
    ec_CX_option = null;
    ec_CX_option = {
        xAxis: {
            type: 'category',
            data: []
        },
        yAxis: {
            type: 'value'
        },
        series: {
            data: [],
            type: 'line'
        }
    };
    ec_ChangX.setOption(ec_CX_option, true);