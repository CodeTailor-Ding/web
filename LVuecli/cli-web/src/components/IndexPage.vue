<template>
  <a-layout id="components-layout-demo-responsive">
    <a-layout-sider
      breakpoint="lg"
      collapsed-width="0"
      width="90"
      @collapse="onCollapse"
      @breakpoint="onBreakpoint"
    >
      <div class="logo" />
      <a-menu theme="dark" mode="inline" :default-selected-keys="['trade']" @select='changeTab'>
        <a-menu-item v-for="menu in menus" :key="menu.key" :style="{ height: '60px',marginTop: '10px'}">
          <a-icon :type="menu.icon" :style="{ fontSize: '32px' }"/>
          <span class="nav-text" :style="{ display: 'block',lineHeight: '10px' }">{{menu.title}}</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header :style="{ background: '#fff', padding: 0 }" />
      <a-layout-content :style="{ margin: '10px 16px 0' }">
        <router-view></router-view>
        
        
      </a-layout-content>
      <a-layout-footer style="textAlign: center">
        Ant Design ©2018 Created by Ant UED
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script>
export default {
  name: 'IndexPage',
  data() {
    return {
      menus:[
        {
          key:'trade',
          icon:'strikethrough',
          title:'交易'
        },
        {
          key:'quotations',
          icon:'stock',
          title:'行情'
        },
        {
          key:'banc',
          icon:'swap',
          title:'银证'
        },
        {
          key:'my',
          icon:'user',
          title:'总览'
        },
      ],
    };
  },
  methods: {
    onCollapse(collapsed, type) {
      console.log(collapsed, type);
    },
    onBreakpoint(broken) {
      console.log(broken);
    },
    changeTab(e){
      this.$router.push({ name: e.key })
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#components-layout-demo-responsive .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}
#components-layout-demo-responsive {
  height: 100%;
}
</style>
