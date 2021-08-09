<template>
    <h2 class="titlecss">{{ titleText }}</h2>
</template>

<script>
    export default {
        name: 'Header',
        props: {
            titleText: String
        }
    }
</script>

<style>
    .titlecss{
        color: black;
    }
</style>
