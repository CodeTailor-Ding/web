<template>
    <ul class="link">
        <li v-for="link in links" :key="link"><a href="#">{{link}}</a></li>
    </ul>
</template>

<script>
    export default {
        name: 'Sidebar',
        data() {
            return {
                links: ['首页', '咨询', '图文', '关于']
            }
        }
    }
</script>

<style>
    .link a {
        color: brown;
    }
</style>
