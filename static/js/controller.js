/**
本模块为echarts绘制季节搜索出的季节性商品图
author:原也 刘益争
create date:2020-8-10
update date:2020-8-12
**/
var jijie_1 = document.getElementById("Jijietu");
var ec_Jijie = echarts.init(jijie_1);
var app = {};
ec_Jijie_option = null;
ec_Jijie_option = {
    color: ['#3398DB'],
    tooltip: {
        trigger: 'axis',
        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: [
        {
            type: 'category',
            data: ['第一季度','第二季度','第三季度','第四季度'],
            axisTick: {
                alignWithLabel: true
            }
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    series: [
        {
            name: '直接访问',
            type: 'bar',
            barWidth: '60%',
            data: []
        }
    ]
};
    ec_Jijie.setOption(ec_Jijie_option, true);


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
    series: [{
        data: [],
        type: 'line'
    }]
};

 ec_ChangX.setOption(ec_CX_option, true);

