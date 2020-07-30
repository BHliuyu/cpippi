<template>
    <div class="allpieChart">
        <div class="pieTitle">{{pieName}}</div>
        <div class="pieDiscribe">2016年至今（单位：%）</div>
        <div ref="pieChart" class="pieChart">
            <!-- <div id="hfdatapieChart"></div> -->
        </div>
    </div>
</template>

<script>
import { Chart } from '@antv/g2'
import { DataView } from '@antv/data-set'

export default {
    name: 'pieChart',
    components: {},
    // 生命周期 - 创建完成（可以访问当前this实例）
    created() {},
    // 生命周期 - 载入后, Vue 实例挂载到实际的 DOM 操作完成，一般在该过程进行 Ajax 交互
    mounted() {
        this.initComponent()
    },
    props: ['chartData', 'pieName'],
    data() {
        return {
            msg: '',
            chart: ''
            // chartData: [
            //     {
            //         type: '0~1%',
            //         value: 27
            //     },
            //     {
            //         type: '1%~2%',
            //         value: 25
            //     },
            //     {
            //         type: '2%~3%',
            //         value: 18
            //     },
            //     {
            //         type: '3%~5%',
            //         value: 15
            //     },
            //     {
            //         type: '>5%',
            //         value: 10
            //     }
            // ]
        }
    },
    // 方法集合
    methods: {
        initComponent() {
            // console.log('5' + this.chartHeight)
            // let offsetHeight = this.chartHeight ? this.chartHeight : 144
            // let chart = new Chart({
            //     container: this.$refs.pieChart,
            //     autoFit: true,
            //     height: offsetHeight
            // })
            // console.log('pie offsetHeight' + offsetHeight)

            const e = document.createEvent('Event')
            e.initEvent('resize', true, true)
            window.dispatchEvent(e)

            let data = this.chartData
            // let name = this.pieName
            // console.log(name)

            // 通过DataSet计算百分比
            const dv = new DataView()
            dv.source(data).transform({
                type: 'percent',
                field: 'value',
                dimension: 'type',
                as: 'percent'
            })
            const chart = new Chart({
                container: this.$refs.pieChart,
                autoFit: true,
                // height: 500,
                padding: 0
            })
            // const piePlot = new Donut(this.$refs.pieChart, {
            //     forceFit: true,
            //     title: {
            //         visible: true,
            //         text: name
            //     },
            //     description: {
            //         visible: true,
            //         text: '2016年至今 （单位：次）'
            //     },
            //     radius: 1,
            //     padding: 'auto',
            //     data,
            //     angleField: 'value',
            //     colorField: 'type'
            //     statistic: {
            //         visible: false
            //     }

            //     radiusField: 'value',
            //     categoryField: 'type',
            //     label: {
            //         visible: true,
            //         type: 'outer',
            //         content: text => text.value
            //     }
            // })

            chart.data(dv.rows)
            chart.scale({
                percent: {
                    formatter: val => {
                        val = (val * 100).toFixed(2) + '%'
                        return val
                    }
                }
            })
            chart.coordinate('theta', {
                radius: 0.5
            })
            chart.tooltip({
                showTitle: false,
                showMarkers: false
            })
            chart.legend(false)
            chart
                .interval()
                .adjust('stack')
                .position('percent')
                .color('type')
                .label('type', {
                    offset: -10
                })
                .tooltip('type*percent', (item, percent) => {
                    percent = (percent * 100).toFixed(2) + '%'
                    return {
                        name: item,
                        value: percent
                    }
                })
                .style({
                    lineWidth: 1,
                    stroke: '#fff'
                })

            const outterView = chart.createView()
            const dv1 = new DataView()
            dv1.source(data).transform({
                type: 'percent',
                field: 'value',
                dimension: 'name',
                as: 'percent'
            })

            outterView.data(dv1.rows)
            outterView.scale({
                percent: {
                    formatter: val => {
                        val = (val * 100).toFixed(2) + '%'
                        return val
                    }
                }
            })
            outterView.coordinate('theta', {
                innerRadius: 0.5 / 0.75,
                radius: 0.75
            })
            outterView
                .interval()
                .adjust('stack')
                .position('percent')
                .color('name', [
                    '#BAE7FF',
                    '#7FC9FE',
                    '#71E3E3',
                    '#ABF5F5',
                    '#8EE0A1',
                    '#BAF5C4'
                ])
                .label('name', function(val) {
                    if (val < 0.51) {
                        return {
                            offset: 10
                        }
                    } else {
                        return null
                    }
                })
                .tooltip('name*percent', (item, percent) => {
                    percent = (percent * 100).toFixed(2) + '%'
                    return {
                        name: item,
                        value: percent
                    }
                })
                .style({
                    lineWidth: 1,
                    stroke: '#fff'
                })

            chart.interaction('element-highlight')
            chart.render()
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
.allpieChart {
    height: 100%;
    width: 100%;
    min-height: 144px;
}
.pieChart {
    height: calc(100% - 40px);
    width: 100%;
    min-height: 144px;
    /* overflow: hidden; */
}
.pieTitle {
    text-align: left;
    margin-left: 20px;
    margin-top: 10px;
}
.pieDiscribe {
    text-align: left;
    margin-left: 20px;
    font-size: 12px;
}
/* .pieChart .hfdatapieChart {
    height: 100%;
    width: 100%;
} */
</style>
