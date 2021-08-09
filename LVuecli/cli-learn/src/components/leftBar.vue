<template>
    <a-layout id="left-bar">
        <a-layout-sider v-model="collapsed" :trigger="null" collapsible class="gloo">
        <div class="logo" />
        <a-menu @click="cli" theme="dark" mode="inline" :default-selected-keys="['1']">
            <a-menu-item key="1">
            <a-icon type="user" />
            <span>nav 1</span>
            </a-menu-item>
            <a-menu-item key="2">
            <a-icon type="video-camera" />
            <span>nav 2</span>
            </a-menu-item>
            <a-menu-item key="3">
            <a-icon type="upload" />
            <span>nav 3</span>
            </a-menu-item>
        </a-menu>
        </a-layout-sider>
        <a-layout>
        <a-layout-header style="background: #fff; padding: 0">
            <a-icon
            class="trigger"
            :type="collapsed ? 'menu-unfold' : 'menu-fold'"
            @click="() => (collapsed = !collapsed)"
            />
        </a-layout-header>
        <!-- <a-layout-content
            :style="{ margin: '24px 16px', padding: '24px', background: '#fff', minHeight: '280px' }"
        >
            Content
        </a-layout-content> -->
        <ma-one></ma-one>
        </a-layout>
    </a-layout>
    
</template>

<script>
    import maOne from "./maOne.vue"

    export default {
        name: 'left-bar',
        data() {
            return {
                collapsed: false,
            }
        },
        methods: {
            cli(e) {
                console.log('clickkk', e)
            }
        },
        components: {
            maOne
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.gloo {
    width: 100%;
    /* min-height: 1080px; */
}

.trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
  float: left;
}

.trigger:hover {
  color: #1890ff;
}

.logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}
</style>
