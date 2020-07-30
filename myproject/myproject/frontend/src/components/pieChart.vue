<template>
    <div ref="pieChart" class="pieChart">
        <!-- <div id="hfdatapieChart"></div> -->
    </div>
</template>

<script>
import { Donut } from '@antv/g2plot'
// import { DataSet } from '@antv/data-set'

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
            let name = this.pieName
            // console.log(name)
            const piePlot = new Donut(this.$refs.pieChart, {
                forceFit: true,
                title: {
                    visible: true,
                    text: name
                },
                description: {
                    visible: true,
                    text: '2016年至今 （单位：次）'
                },
                radius: 1,
                padding: 'auto',
                data,
                angleField: 'value',
                colorField: 'type'
                // statistic: {
                //     visible: false
                // }

                // radiusField: 'value',
                // categoryField: 'type',
                // label: {
                //     visible: true,
                //     type: 'outer',
                //     content: text => text.value
                // }
            })

            piePlot.render()
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
.pieChart {
    height: 100%;
    width: 100%;
    min-height: 144px;
    /* overflow: hidden; */
}
/* .pieChart .hfdatapieChart {
    height: 100%;
    width: 100%;
} */
</style>
