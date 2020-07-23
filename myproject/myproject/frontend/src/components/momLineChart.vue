<template>
    <div ref="momLineChart" class="momchartData">
        <!-- <div id="hfdataLineChart"></div> -->
    </div>
</template>

<script>
import Slider from '@antv/g2/lib/chart/controller/slider'
import { registerComponentController, Chart } from '@antv/g2'
// import { DataSet } from '@antv/data-set'

export default {
    name: 'momLineChart',
    components: {},
    // 生命周期 - 创建完成（可以访问当前this实例）
    created() {},
    // 生命周期 - 载入后, Vue 实例挂载到实际的 DOM 操作完成，一般在该过程进行 Ajax 交互
    mounted() {
        this.initComponent()
    },
    // props: ['chartData', 'chartHeight'],
    data() {
        return {
            msg: '',
            chart: '',
            chartData: [
                {
                    month: 'Jan',
                    CPIforecast: 6,
                    CPIvalue: 7,
                    pv: 17
                },
                {
                    month: 'Feb',
                    CPIforecast: 7,
                    CPIvalue: 6.9,
                    pv: 17
                },
                {
                    month: 'Mar',
                    CPIforecast: 9,
                    CPIvalue: 9.5,
                    pv: 17
                },
                {
                    month: 'Apr',
                    CPIforecast: 5,
                    CPIvalue: 4.5,
                    pv: 19
                },
                {
                    month: 'May',
                    CPIforecast: 8,
                    CPIvalue: 8.4,
                    pv: 1
                },
                {
                    month: 'Jun',
                    CPIforecast: 1,
                    CPIvalue: 1.5,
                    pv: 17
                },
                {
                    month: 'Jul',
                    CPIforecast: 5,
                    CPIvalue: 5.2,
                    pv: 3
                },
                {
                    month: 'Aug',
                    CPIforecast: 7,
                    CPIvalue: 6.5,
                    pv: 10
                },
                {
                    month: 'Sep',
                    CPIforecast: 3,
                    CPIvalue: 3.3,
                    pv: 17
                },
                {
                    month: 'Oct',
                    CPIforecast: 8,
                    CPIvalue: 8.3,
                    pv: 14
                },
                {
                    month: 'Nov',
                    CPIforecast: 4,
                    CPIvalue: 3.9,
                    pv: 12
                },
                {
                    month: 'Dec',
                    CPIforecast: 9,
                    CPIvalue: 9.6,
                    pv: 17
                }
            ]
        }
    },
    // 方法集合
    methods: {
        initComponent() {
            registerComponentController('slider', Slider)
            console.log('mom' + this.chartHeight)
            let offsetHeight = this.chartHeight ? this.chartHeight : 144
            let chart = new Chart({
                container: this.$refs.momLineChart,
                autoFit: true,
                height: offsetHeight,
                padding: [30, 40, 60, 40]
            })
            console.log('mom offsetHeight' + offsetHeight)

            const e = document.createEvent('Event')
            e.initEvent('resize', true, true)
            window.dispatchEvent(e)

            chart.data(this.chartData)
            console.log(this.chartData)
            chart.scale({
                month: {
                    // range: [0, 1]
                },
                CPIvalue: {
                    nice: true,
                    sync: true
                },
                CPIforecast: {
                    nice: true,
                    sync: true
                },
                pv: {
                    alias: '翘尾因素',
                    min: 0,
                    // sync: true, // 将 pv 字段数值同 time 字段数值进行同步
                    nice: true
                }
            })

            chart.tooltip({
                showCrosshairs: true,
                shared: true
            })

            chart.axis('CPIvalue', {
                label: {
                    formatter: val => {
                        return val + ' %'
                    }
                }
            })
            chart.axis('CPIforecast', false)
            chart.axis('pv', {
                title: {}
            })

            chart.legend({
                position: 'top', // 设置图例的显示位置
                itemSpacing: 50, // 图例项之间的间距
                // offsetY: -18
                custom: true,
                items: [
                    {
                        value: 'CPIvalue',
                        name: 'CPI真实值',
                        marker: {
                            symbol: 'hyphen',
                            style: { stroke: '#62DAAB', r: 5, lineWidth: 3 }
                        }
                    },
                    {
                        value: 'CPIforecast',
                        name: 'CPI预测值',
                        marker: {
                            symbol: 'hyphen',
                            style: { stroke: '#fdae6b', r: 5, lineWidth: 3 }
                        }
                    },
                    {
                        value: 'pv',
                        name: '翘尾因素',
                        marker: {
                            symbol: 'square',
                            style: { fill: '#E4E4E4', r: 5 }
                        }
                    }
                ]
            })

            chart
                .interval()
                .position('month*pv')
                .color('#E4E4E4')

            chart
                .line()
                .position('month*CPIvalue')
                .color('#62DAAB')
                .shape('smooth')
            chart
                .point()
                .position('month*CPIvalue')
                .color('#62DAAB')
                .shape('circle')

            chart
                .line()
                .position('month*CPIforecast')
                .color('#fdae6b')
                .shape('smooth')
            chart
                .point()
                .position('month*CPIforecast')
                .color('#fdae6b')
                .shape('circle')

            chart.option('slider', {
                end: 1,
                height: 26
            })

            chart.on('legend:click', ev => {
                let options = ev.view.options
                let items = options.legends.items
                let geoms = ev.view.geometries
                for (let i = 0; i < items.length; i++) {
                    let item = items[i]
                    for (let j = 0; j < geoms.length; j++) {
                        let geom = geoms[j]
                        if (
                            item.value === geom.getYScale().field &&
                            item.unchecked
                        ) {
                            geom.hide()
                        } else if (
                            item.value === geom.getYScale().field &&
                            !item.unchecked
                        ) {
                            geom.show()
                        }
                    }
                }
            })
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
.momchartData {
    height: 100%;
    width: 100%;
    min-height: 200px;
    /* overflow: hidden; */
}
</style>
