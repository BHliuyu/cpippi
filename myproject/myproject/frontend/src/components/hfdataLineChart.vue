<template>
    <div ref="lineChart" class="hfchartData">
        <!-- <div id="hfdataLineChart"></div> -->
    </div>
</template>

<script>
import { Chart } from '@antv/g2'
// import { DataSet } from '@antv/data-set'

export default {
    name: 'lineChart',
    components: {},
    created() {},
    mounted() {
        this.initComponent()
    },
    props: ['chartData', 'chartHeight'],
    data() {
        return {
            msg: '',
            chart: ''
        }
    },
    // 方法集合
    methods: {
        initComponent() {
            // let _this = this
            // console.log('2' + this.chartHeight)
            let offsetHeight = this.chartHeight ? this.chartHeight : 144
            let chart = new Chart({
                container: this.$refs.lineChart,
                autoFit: true,
                height: offsetHeight,
                padding: [20, 10, 50, 40]
            })
            // console.log('offsetHeight' + offsetHeight)

            const e = document.createEvent('Event')
            e.initEvent('resize', true, true)
            window.dispatchEvent(e)

            let data = this.chartData
            chart.data(data)
            // console.log(this.chartData)
            chart.scale({
                date: {
                    range: [0, 1]
                },
                value: {
                    // min: 0,
                    tickCount: 4,
                    nice: true
                }
            })

            chart.tooltip({
                showCrosshairs: true, // 展示 Tooltip 辅助线
                shared: true
            })

            chart.axis('date', {
                label: null
            })

            chart.axis('value', {
                grid: null
            })

            chart.line().position('date*value')
            // .label('value')
            // chart.point().position('date*value')

            const maxObj = this.findMax(data)
            const minObj = this.findMin(data)
            chart.annotation().dataMarker({
                position: [maxObj.date, maxObj.value],
                // position() {
                //     const obj = _this.findMax(data)
                //     return [obj.date, obj.value]
                // },
                point: {
                    style: {
                        fill: '#fdae6b',
                        stroke: '#fdae6b'
                    }
                },
                // autoAdjust: false,
                // direction: 'downward',
                text: {
                    content: maxObj.date + '\n最高点' + maxObj.value,
                    style: {
                        textAlign: 'left',
                        lineWidth: 2
                    }
                }
            })
            chart.annotation().dataMarker({
                position: [minObj.date, minObj.value],
                // position() {
                //     const obj = _this.findMax(data)
                //     return [obj.date, obj.value]
                // },
                point: {
                    style: {
                        fill: '#fdae6b',
                        stroke: '#fdae6b'
                    }
                },
                // autoAdjust: false,
                // direction: 'downward',
                text: {
                    content: minObj.date + '\n最低点' + minObj.value,
                    style: {
                        textAlign: 'left',
                        lineWidth: 2
                    }
                }
            })

            chart.option('slider', {
                start: 0,
                end: 1,
                height: 20
            })
            this.chart = chart
            this.chart.render()
        },
        // 查找最大值
        findMax(data) {
            let maxValue = 0
            let maxObj = null
            data.forEach(obj => {
                if (obj.value > maxValue) {
                    maxValue = obj.value
                    maxObj = obj
                }
            })
            // console.log(maxObj)
            return maxObj
        },
        // 查找最小值
        findMin(data) {
            let minValue = 100
            let minObj = null
            data.forEach(obj => {
                if (obj.value < minValue) {
                    minValue = obj.value
                    minObj = obj
                }
            })
            // console.log(maxObj)
            return minObj
        }
    },
    // 计算属性
    computed: {}
    // watch: {
    //     chartData(val) {
    //         this.chartData = val
    //         // this.loading = false
    //         // this.initComponent()
    //     }
    // }
}
</script>

<style scoped>
.hfchartData {
    height: 100%;
    width: 100%;
    min-height: 144px;
    /* overflow: hidden; */
}
/* .hfchartData .hfdataLineChart {
    height: 100%;
    width: 100%;
} */
</style>
