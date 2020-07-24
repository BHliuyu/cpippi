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
    // 生命周期 - 创建完成（可以访问当前this实例）
    created() {},
    // 生命周期 - 载入后, Vue 实例挂载到实际的 DOM 操作完成，一般在该过程进行 Ajax 交互
    mounted() {
        this.initComponent()
    },
    props: ['chartData', 'chartHeight'],
    data() {
        return {
            msg: '',
            chart: ''
            // chartData: [
            //     { date: '1991', value: 3 },
            //     { date: '1992', value: 4 },
            //     { date: '1993', value: 3.5 },
            //     { date: '1994', value: 5 },
            //     { date: '1995', value: 4.9 },
            //     { date: '1996', value: 6 },
            //     { date: '1997', value: 7 },
            //     { date: '1998', value: 9 },
            //     { date: '1999', value: 13 }
            // ]
        }
    },
    // 方法集合
    methods: {
        initComponent() {
            // console.log('2' + this.chartHeight)
            let offsetHeight = this.chartHeight ? this.chartHeight : 144
            let chart = new Chart({
                container: this.$refs.lineChart,
                autoFit: true,
                height: offsetHeight,
                padding: [20, 10, 50, 25]
            })
            // console.log('offsetHeight' + offsetHeight)

            const e = document.createEvent('Event')
            e.initEvent('resize', true, true)
            window.dispatchEvent(e)

            chart.data(this.chartData)
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

            chart.line().position('date*value')
            // .label('value')
            // chart.point().position('date*value')

            chart.option('slider', {
                start: 0.5,
                end: 1,
                height: 20
            })
            this.chart = chart
            this.chart.render()
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
