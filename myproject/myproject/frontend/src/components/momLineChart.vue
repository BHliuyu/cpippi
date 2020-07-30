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
    props: ['chartData'],
    data() {
        return {
            msg: '',
            chart: ''
            // chartData: [
            //     {
            //         date: 'Jan',
            //         forecast: 6,
            //         real_value: 7,
            //         pv: 17
            //     },
            //     {
            //         date: 'Feb',
            //         forecast: 7,
            //         real_value: 6.9,
            //         pv: 17
            //     },
            //     {
            //         date: 'Mar',
            //         forecast: 9,
            //         real_value: 9.5,
            //         pv: 17
            //     },
            //     {
            //         date: 'Apr',
            //         forecast: 5,
            //         real_value: 4.5,
            //         pv: 19
            //     },
            //     {
            //         date: 'May',
            //         forecast: 8,
            //         real_value: 8.4,
            //         pv: 1
            //     },
            //     {
            //         date: 'Jun',
            //         forecast: 1,
            //         real_value: 1.5,
            //         pv: 17
            //     },
            //     {
            //         date: 'Jul',
            //         forecast: 5,
            //         real_value: 5.2,
            //         pv: 3
            //     },
            //     {
            //         date: 'Aug',
            //         forecast: 7,
            //         real_value: 6.5,
            //         pv: 10
            //     },
            //     {
            //         date: 'Sep',
            //         forecast: 3,
            //         real_value: 3.3,
            //         pv: 17
            //     },
            //     {
            //         date: 'Oct',
            //         forecast: 8,
            //         real_value: 8.3,
            //         pv: 14
            //     },
            //     {
            //         date: 'Nov',
            //         forecast: 4,
            //         real_value: 3.9,
            //         pv: 12
            //     },
            //     {
            //         date: 'Dec',
            //         forecast: 9,
            //         real_value: 9.6,
            //         pv: 17
            //     }
            // ]
        }
    },
    // 方法集合
    methods: {
        initComponent() {
            registerComponentController('slider', Slider)
            // console.log('mom' + this.chartHeight)
            let offsetHeight = this.chartHeight ? this.chartHeight : 144
            let chart = new Chart({
                container: this.$refs.momLineChart,
                autoFit: true,
                height: offsetHeight,
                padding: [30, 40, 60, 40]
            })
            // console.log('mom offsetHeight' + offsetHeight)

            const e = document.createEvent('Event')
            e.initEvent('resize', true, true)
            window.dispatchEvent(e)

            chart.data(this.chartData)
            // console.log(this.chartData)
            chart.scale({
                // tickCount: 5,
                date: {
                    // range: [0, 1]
                },
                real_value: {
                    alias: '真实值',
                    nice: true,
                    sync: true
                },
                forecast: {
                    alias: '预测值',
                    nice: true,
                    sync: true
                }
            })

            chart.tooltip({
                showCrosshairs: true,
                shared: true
            })

            chart.axis('real_value', {
                grid: null,

                label: {
                    formatter: val => {
                        return val + ' %'
                    }
                }
            })
            chart.axis('forecast', false)

            chart.legend({
                position: 'top', // 设置图例的显示位置
                itemSpacing: 50, // 图例项之间的间距
                // offsetY: -18
                custom: true,
                items: [
                    {
                        value: 'real_value',
                        name: 'CPI真实值',
                        marker: {
                            symbol: 'hyphen',
                            style: { stroke: '#62DAAB', r: 5, lineWidth: 3 }
                        }
                    },
                    {
                        value: 'forecast',
                        name: 'CPI预测值',
                        marker: {
                            symbol: 'hyphen',
                            style: { stroke: '#fdae6b', r: 5, lineWidth: 3 }
                        }
                    }
                ]
            })

            chart
                .line()
                .position('date*real_value')
                .color('#62DAAB')
                .shape('smooth')
            chart
                .point()
                .position('date*real_value')
                .color('#62DAAB')
                .shape('circle')

            chart
                .line()
                .position('date*forecast')
                .color('#fdae6b')
                .shape('smooth')
            chart
                .point()
                .position('date*forecast')
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
