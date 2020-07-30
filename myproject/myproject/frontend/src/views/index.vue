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
                            <el-table
                                :data="cpiData"
                                height="540"
                                style="width: 100%;margin-top: 20px;"
                                row-key="id"
                                :expand-row-keys="['2']"
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
                                <span>CPI详情</span>
                            </div>
                            <el-tabs v-model="centerActiveTab" @tab-click="handleClickTab" style="height:100%">
                                <el-tab-pane label="CPI同比" name="yoy">
                                    <!-- <yoyLineChart :chart-data="yoydata" :chart-height="hfheight"></yoyLineChart> -->
                                    <yoyLineChart v-if="'yoy' === centerActiveTab && ifCpiyoyReady" :chart-data="cpiyoy_data"></yoyLineChart>
                                </el-tab-pane>
                                <el-tab-pane label="CPI环比" name="mom">
                                    <!-- <yoyLineChart :chart-data="yoydata" :chart-height="hfheight"></yoyLineChart> -->
                                    <momLineChart v-if="'mom' === centerActiveTab && ifCpimomReady" :chart-data="cpimom_data"></momLineChart>
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
                                <span>高频数据：猪肉</span>
                            </div>
                            <div ref="hfchart" style="height:90%;overflow:hidden">
                                <lineChart v-if="ishfReady" v-loading="hfloading" :chart-data="hfdata1" :chart-height="hfheight"></lineChart>
                            </div>
                        </el-card>
                    </div>
                    <div class="grid-content grid-right-row">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>高频数据：蔬菜</span>
                            </div>
                            <div style="height:90%;overflow:hidden">
                                <lineChart v-if="ishfReady" v-loading="hfloading" :chart-data="hfdata2" :chart-height="hfheight"></lineChart>
                            </div>
                        </el-card>
                    </div>
                    <div class="grid-content grid-right-row1">
                        <el-card class="box-card height-full-container">
                            <div>
                                <span>高频数据：水果</span>
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
            cpiData: [
                {
                    id: 1,
                    name: '食品烟酒',
                    value: '25.57%',
                    children: [
                        { id: 11, name: '粮食', value: '1.79%' },
                        { id: 12, name: '食用油', value: '1.50%' },
                        { id: 13, name: '鲜菜', value: '2.54%' },
                        { id: 14, name: '禽肉类', value: '1.21%' },
                        { id: 15, name: '猪肉', value: '2.26%' },
                        { id: 16, name: '牛肉', value: '1.13%' },
                        { id: 17, name: '羊肉', value: '0.74%' },
                        { id: 18, name: '水产品', value: '1.92%' },
                        { id: 19, name: '蛋类', value: '0.50%' },
                        { id: 110, name: '奶类', value: '1.50%' },
                        { id: 111, name: '鲜果', value: '1.72%' },
                        { id: 112, name: '烟草', value: '1.75%' },
                        { id: 113, name: '酒类', value: '1.75%' },
                        { id: 114, name: '在外餐饮', value: '5.26%' }
                    ]
                },
                {
                    id: 2,
                    name: '非食品',
                    value: '74.43%',
                    children: [
                        { id: 21, name: '衣着', value: '7.28%' },
                        { id: 22, name: '居住', value: '23.32%' },
                        { id: 23, name: '生活用品及服务', value: '6.20%' },
                        { id: 24, name: '交通和通信', value: '13.20%' },
                        { id: 25, name: '教育文化和娱乐', value: '10.73%' },
                        { id: 26, name: '医疗保健', value: '7.90%' },
                        { id: 27, name: '其他用品和服务', value: '5.80%' }
                    ]
                }
            ],
            centerActiveTab: '',
            yoydata: [],
            ishfReady: false,
            hfloading: true,
            hfheight: null,
            ifCpiyoyReady: false, // 保证获取数据后在渲染
            ifCpimomReady: false,
            isPieReady: false,
            cpiyoy_data: [],
            cpimom_data: [],
            cciForecast_data: [],
            otherForecast_data: [],
            hfdata1: [],
            hfdata2: [],
            hfdata3: []
        }
    },
    methods: {
        getData() {
            let HFDATA_URL = '/api/data/cpidata/'
            let CPIYOY_URL = '/api/data/cpiyoy/'
            let CPIMOM_URL = '/api/data/cpimom/'
            let PIE_URL = '/api/data/cpicompare/'

            axios
                .get(CPIYOY_URL, {})
                .then(res => {
                    let data = res.data.data

                    this.cpiyoy_data = data.map(item => {
                        return {
                            date: item.date,
                            forecast: item.cpi_forecast,
                            real_value: item.cpi_true,
                            pv: item.cpi_tail
                        }
                    })
                    this.ifCpiyoyReady = true
                    // console.log(this.cpiyoy_data)
                })
                .catch(res => {
                    console.log('cpi同比数据获取有误，错误原因为：' + res)
                })

            axios
                .get(CPIMOM_URL, {})
                .then(res => {
                    let data = res.data.data

                    this.cpimom_data = data.map(item => {
                        return {
                            date: item.date,
                            forecast: item.cpi_forecast,
                            real_value: item.cpi_true
                        }
                    })
                    this.ifCpimomReady = true
                    // console.log(this.cpimom_data)
                })
                .catch(res => {
                    console.log('cpi环比数据获取有误，错误原因为：' + res)
                })

            axios
                .get(PIE_URL, {})
                .then(res => {
                    let data = res.data.data
                    let arr1 = []
                    let arr2 = []
                    data.map(item => {
                        if (item.other_number !== 0) {
                            let obj1 = {
                                type: item.level1,
                                name: item.level2,
                                value: item.other_number
                            }
                            arr1.push(obj1)
                        }
                        if (item.our_number !== 0) {
                            let obj2 = {
                                type: item.level1,
                                name: item.level2,
                                value: item.our_number
                            }
                            arr2.push(obj2)
                        }
                    })
                    this.otherForecast_data = arr1
                    this.cciForecast_data = arr2
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
                    // console.log(data)
                    let arr1 = []
                    let arr2 = []
                    let arr3 = []
                    data.map(item => {
                        if (item.thirtythreecitysale !== null) {
                            let obj1 = {
                                date: item.date,
                                value: item.thirtythreecitysale
                            }
                            arr1.push(obj1)
                        }
                        if (item.twentyeightvegetables !== null) {
                            let obj2 = {
                                date: item.date,
                                value: item.twentyeightvegetables
                            }
                            arr2.push(obj2)
                        }
                        if (item.sevenfruits !== null) {
                            let obj = {
                                date: item.date,
                                value: item.sevenfruits
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
            // console.log('this.getdata')
            // console.log('1' + this.hfheight)
            // console.log(this.hfdata3)
            // this.flag = true
            // if (this.hfdata1) {
            //     this.flag = true
            // }
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
