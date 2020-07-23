<template>
    <div class="allcontainer height-full-container">
        <myHeader></myHeader>
        <div class="container height-full-container">
            <el-row class="height-full-container" :gutter="10">
                <el-col class="grid-left" :xs="24" :sm="24" :md="6" :lg="6" :xl="6">
                    <div class="grid-content grid-left-row1">
                        <el-card class="box-card height-full-container">
                            <div class="paddingTop">本月预测同比数值</div>
                            <div class="largeNumber">4.2</div>
                            <div class="lastCPIValue">
                                <div class="lastCPIValue-item">
                                    <div>上月预测同比数值</div>
                                    <div class="number">4.1</div>
                                </div>
                                <div class="lastCPIValue-item">
                                    <div>上两月预测同比数值</div>
                                    <div class="number">4.0</div>
                                </div>
                            </div>
                        </el-card>
                    </div>
                    <div class="grid-content grid-left-row2">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>CPI权重数据</span>
                            </div>
                            <el-table :data="cpiData" style="width: 100%;margin-top: 20px;" row-key="id" default-expand-all :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
                                <el-table-column prop="date" label="品种" width="180"></el-table-column>
                                <el-table-column prop="address" label="权重" sortable></el-table-column>
                            </el-table>
                        </el-card>
                    </div>
                </el-col>
                <el-col class="grid-center" :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
                    <div class="grid-content grid-center-row1">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>CPI详情</span>
                            </div>
                            <el-tabs v-model="centerActiveTab" @tab-click="handleClickTab" style="height:100%">
                                <el-tab-pane label="CPI同比" name="yoy">
                                    <!-- <yoyLineChart :chart-data="yoydata" :chart-height="hfheight"></yoyLineChart> -->
                                    <yoyLineChart v-if="'yoy' === centerActiveTab"></yoyLineChart>
                                </el-tab-pane>
                                <el-tab-pane label="CPI环比" name="mom">
                                    <!-- <yoyLineChart :chart-data="yoydata" :chart-height="hfheight"></yoyLineChart> -->
                                    <momLineChart v-if="'mom' === centerActiveTab"></momLineChart>
                                </el-tab-pane>
                            </el-tabs>
                        </el-card>
                    </div>
                    <div class="grid-content grid-center-row2">
                        <el-card class="box-card height-full-container">
                            <!-- <div>
                                <span>预测误差</span>
                            </div>-->
                            <div class="bottom">
                                <div class="bottomBlock">
                                    <pieChart pie-name="指数公司预测误差"></pieChart>
                                </div>
                                <div class="bottomBlock">
                                    <pieChart pie-name="市场机构预测误差"></pieChart>
                                </div>
                            </div>
                        </el-card>
                    </div>
                </el-col>
                <el-col class="grid-right" :xs="24" :sm="24" :md="6" :lg="6" :xl="6">
                    <div class="grid-content grid-right-row">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>高频数据</span>
                            </div>
                            <div ref="hfchart" style="height:90%;overflow:hidden">
                                <lineChart v-if="ishfReady" v-loading="hfloading" :chart-data="hfdata1" :chart-height="hfheight"></lineChart>
                            </div>
                        </el-card>
                    </div>
                    <div class="grid-content grid-right-row">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>高频数据</span>
                            </div>
                            <div style="height:90%;overflow:hidden">
                                <lineChart v-if="ishfReady" v-loading="hfloading" :chart-data="hfdata2" :chart-height="hfheight"></lineChart>
                            </div>
                        </el-card>
                    </div>
                    <div class="grid-content grid-right-row1">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>高频数据</span>
                            </div>
                            <div style="height:90%;overflow:hidden">
                                <lineChart v-if="ishfReady" v-loading="hfloading" :chart-data="hfdata3" :chart-height="hfheight"></lineChart>
                            </div>
                        </el-card>
                    </div>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
import myHeader from '@/components/header.vue'
import lineChart from '@/components/hfdataLineChart.vue'
import yoyLineChart from '@/components/yoyLineChart.vue'
import momLineChart from '@/components/momLineChart.vue'
import pieChart from '@/components/pieChart.vue'
// import axios from 'axios'

export default {
    name: 'index',
    components: {
        myHeader,
        lineChart,
        yoyLineChart,
        momLineChart,
        pieChart
    },
    mounted() {
        // this.getData()
        this.initComponent()
    },
    data() {
        return {
            cpiData: [
                { id: 1, date: '生猪', address: '20%' },
                { id: 2, date: '玉米', address: '20%' },
                { id: 3, date: '粮食', address: '20%' },
                {
                    id: 4,
                    date: '衣食住行',
                    address: '40%',
                    children: [
                        { id: 41, date: '玉米', address: '20%' },
                        { id: 42, date: '粮食', address: '20%' }
                    ]
                }
            ],
            centerActiveTab: '',
            yoydata: [],
            ishfReady: false,
            hfloading: true,
            hfheight: null,
            hfdata1: [],
            hfdata2: [],
            hfdata3: []
        }
    },
    methods: {
        getData() {
            this.yoydata = [
                { month: 'Jan', city: 'Tokyo', temperature: 7 },
                { month: 'Jan', city: 'London', temperature: 3.9 },
                { month: 'Feb', city: 'Tokyo', temperature: 6.9 },
                { month: 'Feb', city: 'London', temperature: 4.2 },
                { month: 'Mar', city: 'Tokyo', temperature: 9.5 },
                { month: 'Mar', city: 'London', temperature: 5.7 },
                { month: 'Apr', city: 'Tokyo', temperature: 14.5 },
                { month: 'Apr', city: 'London', temperature: 8.5 },
                { month: 'May', city: 'Tokyo', temperature: 18.4 },
                { month: 'May', city: 'London', temperature: 11.9 },
                { month: 'Jun', city: 'Tokyo', temperature: 21.5 },
                { month: 'Jun', city: 'London', temperature: 15.2 },
                { month: 'Jul', city: 'Tokyo', temperature: 25.2 },
                { month: 'Jul', city: 'London', temperature: 17 },
                { month: 'Aug', city: 'Tokyo', temperature: 26.5 },
                { month: 'Aug', city: 'London', temperature: 16.6 },
                { month: 'Sep', city: 'Tokyo', temperature: 23.3 },
                { month: 'Sep', city: 'London', temperature: 14.2 },
                { month: 'Oct', city: 'Tokyo', temperature: 18.3 },
                { month: 'Oct', city: 'London', temperature: 10.3 },
                { month: 'Nov', city: 'Tokyo', temperature: 13.9 },
                { month: 'Nov', city: 'London', temperature: 6.6 },
                { month: 'Dec', city: 'Tokyo', temperature: 9.6 },
                { month: 'Dec', city: 'London', temperature: 4.8 }
            ]
            this.hfdata1 = [
                { year: '1991', value: 3 },
                { year: '1992', value: 4 },
                { year: '1993', value: 3.5 },
                { year: '1994', value: 5 },
                { year: '1995', value: 4.9 },
                { year: '1996', value: 6 },
                { year: '1997', value: 7 },
                { year: '1998', value: 9 },
                { year: '1999', value: 13 }
            ]
            this.hfdata2 = [
                { year: '1991', value: 3 },
                { year: '1992', value: 4 },
                { year: '1993', value: 3.5 },
                { year: '1994', value: 5 },
                { year: '1995', value: 4.9 },
                { year: '1996', value: 6 },
                { year: '1997', value: 7 },
                { year: '1998', value: 9 },
                { year: '1999', value: 13 }
            ]
            this.hfdata3 = [
                { year: '1991', value: 3 },
                { year: '1992', value: 4 },
                { year: '1993', value: 3.5 },
                { year: '1994', value: 5 },
                { year: '1995', value: 4.9 },
                { year: '1996', value: 6 },
                { year: '1997', value: 7 },
                { year: '1998', value: 9 },
                { year: '1999', value: 13 }
            ]
            this.hfheight = this.$refs.hfchart.offsetHeight
            console.log('this.getdata')
            console.log('1' + this.hfheight)
            // console.log(this.hfdata3)
            // this.flag = true
            // if (this.hfdata1) {
            //     this.flag = true
            // }
            // console.log(this.flag)
            // console.log(this.hfdata1)
        },
        initComponent() {
            // let _this = this
            // new Promise(function(resolve, reject) {
            //     setTimeout(function() {
            //         _this.getData()
            //     }, 100)
            // }).then(() => {
            //     console.log('2' + this.hfheight)
            //     _this.hfloading = false
            //     _this.ishfReady = true
            // })
            this.centerActiveTab = 'yoy'
            this.getData()
            this.hfloading = false
            this.ishfReady = true
        },
        handleClickTab(tab, event) {
            // console.log(tab.name)
            tab.name === 'mom'
                ? (this.centerActiveTab = 'mom')
                : (this.centerActiveTab = 'yoy')
            // console.log(tab, event)
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.allcontainer {
    min-width: 768px;
    width: 100%;
}
.container {
    margin-right: auto;
    margin-left: auto;
    padding-left: 15px;
    padding-right: 15px;
}
.container:after {
    clear: both;
}
.bottom {
    height: 100%;
    overflow: hidden;
}
.bottomBlock {
    height: 100%;
    width: 50%;
    display: inline-block;
    vertical-align: top;
}
.paddingTop {
    padding-top: 20px;
}
.lastCPIValue {
    border-top: 1px solid #f6f6f6;
    display: flex;
    padding: 20px 0;
    width: 100%;
    margin-top: 20px;
}
.lastCPIValue .lastCPIValue-item {
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
    border-right: 1px solid #ebebeb;
    display: flex;
    -webkit-box-flex: 1;
    -ms-flex: 1 0;
    flex: 1 0;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
}
.lastCPIValue .lastCPIValue-item:last-child {
    border-right: none;
}
.largeNumber {
    color: #444;
    font-size: 30px;
    line-height: 28px;
    font-weight: 600;
    margin-top: 10px;
}
.number {
    color: #444;
    font-size: 22px;
    line-height: 28px;
    font-weight: 600;
    margin-top: 10px;
}
.el-col {
    border-radius: 4px;
}
/* 添加scoped情况下改变el-card的header和body样式无效，需要使用深度选择器 */
.el-card /deep/ .el-card__body {
    height: 88%;
}
.grid-center-row2 .el-card /deep/ .el-card__body {
    height: 100%;
    padding: 0;
}
.el-tabs /deep/ .el-tabs__content,
.el-tab-pane {
    height: 95%;
}
.grid-content {
    border-radius: 4px;
    min-height: 36px;
    margin: 0px;
    padding: 5px 0px;
}
.grid-left {
    height: 100%;
    display: flex;
    flex-direction: column;
}
.grid-left .grid-left-row1 {
    flex: 1;
    /* margin: 0; */
}
.grid-left .grid-left-row2 {
    flex: 2;
    margin-bottom: 10px;
    /* margin: 0; */
}
.grid-center {
    height: 100%;
    display: flex;
    flex-direction: column;
}
.grid-center .grid-center-row1 {
    flex: 2;
}
.grid-center .grid-center-row2 {
    flex: 1;
    margin-bottom: 10px;
}
.grid-right {
    height: 100%;
    display: flex;
    flex-direction: column;
}
.grid-right .grid-right-row {
    /* overflow: hidden; */
    flex: 1;
}
.grid-right .grid-right-row1 {
    /* overflow: hidden; */
    flex: 1;
    margin-bottom: 10px;
}
</style>
