<template>
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
        <a class="logo" herf="{path:/}">
            <img src="@/assets/logo.png" alt="logo" />
        </a>
        <a class="menu-text" herf="{path:/}">
            <span>首页</span>
        </a>
        <div class="menu-container">
            <el-menu router :default-active="$route.path" class="el-menu-demo" mode="horizontal">
                <el-menu-item index="/">CPI预测指数</el-menu-item>
                <el-menu-item index="/PPI">PPI预测指数</el-menu-item>
                <el-menu-item index="/other">商品综合指数</el-menu-item>
                <el-submenu index="3">
                    <template slot="title">消息中心</template>
                    <el-menu-item index="/other">选项1</el-menu-item>
                    <el-menu-item index="/other">选项2</el-menu-item>
                    <el-menu-item index="/other">选项3</el-menu-item>
                </el-submenu>
                <el-menu-item index="/other">关于我们</el-menu-item>
            </el-menu>
        </div>
    </div>
</template>

<script>
export default {
    name: 'myheader',
    data() {
        return { activeIndex: '1', activeIndex2: '1' }
    },
    methods: {
        // handleSelect(key, keyPath) {
        //     // console.log(key, keyPath)
        // }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar-default {
    background-color: #fff;
    border-color: #f0f0f0;
    width: 100%;
    height: 59px;
    border-bottom: solid 1px #e6e6e6;
    min-width: 768px;
    /* margin-bottom: 20px; */
}
.navbar-fixed-top {
    top: 0;
    border-width: 0 0 1px;
    position: fixed;
    right: 0;
    left: 0;
    z-index: 1000;
}
.navbar .logo {
    float: left;
    height: 56px;
    margin-left: 10px;
    padding: 0;
}
.navbar .logo img {
    height: 100%;
}
.navbar .menu-text {
    float: left;
    height: 56px;
    margin-left: 20px;
    padding: 15px 2px;
}
.navbar .menu-text span {
    font-size: 18px;
    line-height: 26px;
    height: 56px;
    color: #41b883;
}
.navbar .menu-container {
    width: 600px;
    float: right;
    height: 56px;
}
a:hover {
    cursor: pointer;
}
</style>
