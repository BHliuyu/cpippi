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
                            <div class="lastPPIValue">
                                <div class="lastPPIValue-item">
                                    <div>上月预测同比数值</div>
                                    <div class="number">4.1</div>
                                </div>
                                <div class="lastPPIValue-item">
                                    <div>上两月预测同比数值</div>
                                    <div class="number">4.0</div>
                                </div>
                            </div>
                        </el-card>
                    </div>
                    <div class="grid-content grid-left-row2">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>PPI权重数据</span>
                            </div>
                            <el-table
                                :data="ppiData"
                                height="540"
                                style="width: 100%;margin-top: 20px;"
                                row-key="id"
                                default-expand-all
                                :tree-props="{children: 'children', hasChildren: 'hasChildren'}"
                            >
                                <el-table-column prop="name" label="品种" width="180"></el-table-column>
                                <el-table-column prop="value" label="权重" sortable></el-table-column>
                            </el-table>
                        </el-card>
                    </div>
                </el-col>
                <el-col class="grid-center" :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
                    <div class="grid-content grid-center-row1">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>PPI详情</span>
                            </div>
                            <el-tabs v-model="centerActiveTab" @tab-click="handleClickTab" style="height:100%">
                                <el-tab-pane label="PPI同比" name="yoy">
                                    <!-- <yoyLineChart :chart-data="yoydata" :chart-height="hfheight"></yoyLineChart> -->
                                    <yoyLineChart v-if="'yoy' === centerActiveTab && ifPpiyoyReady" :chart-data="ppiyoy_data"></yoyLineChart>
                                </el-tab-pane>
                                <el-tab-pane label="PPI环比" name="mom">
                                    <!-- <yoyLineChart :chart-data="yoydata" :chart-height="hfheight"></yoyLineChart> -->
                                    <momLineChart v-if="'mom' === centerActiveTab && ifPpimomReady" :chart-data="ppimom_data"></momLineChart>
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
                                    <pieChart v-if="isPieReady" :chart-data="cciForecast_data" pie-name="指数公司预测误差"></pieChart>
                                </div>
                                <div class="bottomBlock">
                                    <pieChart v-if="isPieReady" :chart-data="otherForecast_data" pie-name="市场机构预测误差"></pieChart>
                                </div>
                            </div>
                        </el-card>
                    </div>
                </el-col>
                <el-col class="grid-right" :xs="24" :sm="24" :md="6" :lg="6" :xl="6">
                    <div class="grid-content grid-right-row">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>高频数据：OPEC一篮子原油</span>
                            </div>
                            <div ref="hfchart" style="height:90%;overflow:hidden">
                                <lineChart v-if="ishfReady" v-loading="hfloading" :chart-data="hfdata1" :chart-height="hfheight"></lineChart>
                            </div>
                        </el-card>
                    </div>
                    <div class="grid-content grid-right-row">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>高频数据：螺纹钢</span>
                            </div>
                            <div style="height:90%;overflow:hidden">
                                <lineChart v-if="ishfReady" v-loading="hfloading" :chart-data="hfdata2" :chart-height="hfheight"></lineChart>
                            </div>
                        </el-card>
                    </div>
                    <div class="grid-content grid-right-row1">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>高频数据：LME铜</span>
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
import axios from 'axios'

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
            ppiData: [
                {
                    id: 1,
                    name: '生产资料',
                    value: '76.76%',
                    children: [
                        { id: 11, name: '采掘工业', value: '0.49%' },
                        { id: 12, name: '原材料工业', value: '21.84%' },
                        { id: 13, name: '加工工业', value: '50.02%' }
                    ]
                },
                {
                    id: 2,
                    name: '生活资料',
                    value: '23.24%',
                    children: [
                        { id: 21, name: '食品类', value: '8.21%' },
                        { id: 22, name: '衣着类', value: '3.44%' },
                        { id: 23, name: '一般日用品类', value: '5.60%' },
                        { id: 24, name: '耐用消费品类', value: '6.02%' }
                    ]
                }
            ],
            centerActiveTab: '',
            yoydata: [],
            ishfReady: false,
            hfloading: true,
            hfheight: null,
            ifPpiyoyReady: false, // 保证获取数据后在渲染
            ifPpimomReady: false,
            isPieReady: false,
            ppiyoy_data: [],
            ppimom_data: [],
            cciForecast_data: [],
            otherForecast_data: [],
            hfdata1: [],
            hfdata2: [],
            hfdata3: []
        }
    },
    methods: {
        getData() {
            let HFDATA_URL = '/api/data/ppidata/'
            let PPIYOY_URL = '/api/data/ppiyoy/'
            let PPIMOM_URL = '/api/data/ppimom/'
            let PIE_URL = '/api/data/ppicompare/'

            axios
                .get(PPIYOY_URL, {})
                .then(res => {
                    let data = res.data.data

                    this.ppiyoy_data = data.map(item => {
                        return {
                            date: item.date,
                            forecast: item.ppi_forecast,
                            real_value: item.ppi_true,
                            pv: item.ppi_tail
                        }
                    })
                    this.ifPpiyoyReady = true
                    // console.log(this.cpiyoy_data)
                })
                .catch(res => {
                    console.log('ppi同比数据获取有误，错误原因为：' + res)
                })

            axios
                .get(PPIMOM_URL, {})
                .then(res => {
                    let data = res.data.data

                    this.ppimom_data = data.map(item => {
                        return {
                            date: item.date,
                            forecast: item.ppi_forecast,
                            real_value: item.ppi_true
                        }
                    })
                    this.ifPpimomReady = true
                    // console.log(this.cpimom_data)
                })
                .catch(res => {
                    console.log('cpi环比数据获取有误，错误原因为：' + res)
                })

            axios
                .get(PIE_URL, {})
                .then(res => {
                    let data = res.data.data

                    this.cciForecast_data = data.map(item => {
                        return {
                            type: item.level,
                            value: item.our_number
                        }
                    })
                    this.otherForecast_data = data.map(item => {
                        return {
                            type: item.level,
                            value: item.other_number
                        }
                    })
                    this.isPieReady = true
                    // console.log(this.cpiyoy_data)
                })
                .catch(res => {
                    console.log('cpi同比数据获取有误，错误原因为：' + res)
                })

            axios
                .get(HFDATA_URL, {})
                .then(res => {
                    let data = res.data.data
                    let arr1 = []
                    let arr2 = []
                    let arr3 = []
                    data.map(item => {
                        if (item.crudeoil !== null) {
                            let obj1 = {
                                date: item.date,
                                value: item.crudeoil
                            }
                            arr1.push(obj1)
                        }
                        if (item.hrb400 !== null) {
                            let obj2 = {
                                date: item.date,
                                value: item.hrb400
                            }
                            arr2.push(obj2)
                        }
                        if (item.lmecopper !== null) {
                            let obj = {
                                date: item.date,
                                value: item.lmecopper
                            }
                            arr3.push(obj)
                        }
                    })
                    this.hfdata1 = arr1
                    this.hfdata2 = arr2
                    this.hfdata3 = arr3
                    this.hfloading = false
                    this.ishfReady = true
                    // console.log(this.hfdata1)
                })
                .catch(res => {
                    console.log('高频数据获取有误，错误原因为：' + res)
                })

            this.hfheight = this.$refs.hfchart.offsetHeight

            // console.log(this.flag)
            // console.log(this.hfdata1)
        },
        initComponent() {
            this.centerActiveTab = 'yoy'
            this.getData()
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
    padding-top: 5px;
}
.lastPPIValue {
    border-top: 1px solid #f6f6f6;
    display: flex;
    padding: 20px 0;
    width: 100%;
    margin-top: 20px;
}
.lastPPIValue .lastPPIValue-item {
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
.lastPPIValue .lastPPIValue-item:last-child {
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
    flex: 3;
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
