<template>
  <div class="bg-[url('assets/imgs/bg.jpg')] bg-cover bg-center h-screen text-white p-2 flex overflow-hidden" v-if="mydata">
    <!-- 左 -->
    <div class="flex-1 mr-2 bg-opacity-50 bg-slate-800 p-3 flex flex-col">
      <!-- 横向柱状图 -->
      <HorizontalBar class="h-1/3 box-border pb-4" :data="mydata.regionData"></HorizontalBar>
      <!-- 雷达图 -->
      <RadarBar class="h-1/3 box-border pb-4" :data="mydata.riskData"></RadarBar>
      <!-- 关系图 -->
      <Relation class="h-1/3" :data="mydata.relationData"></Relation>
    </div>
    <!-- 中 -->
    <div class="w-1/2 mr-2 flex flex-col">
      <!-- 数据总览 -->
      <TotalData class="bg-opacity-50 bg-slate-800 p-3 h-1/3" :data="mydata.totalData"></TotalData>
      <!-- 地图可视化 -->
      <MapChart class="bg-opacity-80 bg-slate-800 p-3 mt-2 flex-1 h-2/3"></MapChart>
    </div>
    <!-- 右 -->
    <div class="flex-1 bg-opacity-50 bg-slate-800 p-3 flex flex-col">
      <!-- 竖向柱状图 -->
      <VerticalBar class="h-1/3 box-border pb-4" :data="mydata.serverData"></VerticalBar>
      <!-- 环形图 -->
      <RingBar class="h-1/3 box-border pb-4" :data="mydata.completeData"></RingBar>
      <!-- 云图 -->
      <WordCount class="h-1/3 box-border"></WordCount>
    </div>
  </div>
</template>

<script setup>
import MapChart from './components/MapChart.vue'
import HorizontalBar from './components/HorizontalBar.vue'
import WordCount from './components/WordCount.vue'
import RingBar from './components/RingBar.vue'
import VerticalBar from './components/VerticalBar.vue'
import TotalData from './components/TotalData.vue'
import RadarBar from './components/RadarBar.vue'
import Relation from './components/Relation.vue'

import axios from 'axios'
import { onMounted, ref } from 'vue'

const mydata = ref(null)
const baseUrl = 'https://www.fastmock.site/mock/e6c1156fd50105b0b4844db8fd4c1c60/data/test'
const loadData = () => {
  axios.get(baseUrl).then(({ data }) => {
    mydata.value = data
  })
}

onMounted(() => {
  loadData()
})

setInterval(() => {
  loadData()
}, 3000)
</script>

<style scoped lang="scss">
@import './assets/fonts/font.css';
#app {
  font-family: 'Alimama ShuHeiTi Bold';
}
body {
  font-family: 'Alimama ShuHeiTi Bold';
}
</style>
