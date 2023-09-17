<template>
  <div>
    <div>路径可视化</div>
    <div ref="target" class="w-full h-full"></div>
  </div>
</template>

<script setup>
import $ from 'jquery'
import { onMounted, ref } from 'vue'
import * as echarts from 'echarts'

let myChart = null

const target = ref(null)

onMounted(() => {
  myChart = echarts.init(target.value)

  renderChart()
})

const renderChart = () => {
  let ROOT_PATH = ''
  $.get(ROOT_PATH + 'bg.svg', function (svg) {
    echarts.registerMap('ksia-ext-plan', { svg: svg })
    const option = {
      tooltip: {},
      geo: {
        map: 'ksia-ext-plan',
        roam: true,
        layoutCenter: ['50%', '50%'],
        layoutSize: '100%',
        zoom: 1.5,
      },
      series: [
        {
          name: 'Route',
          type: 'lines',
          coordinateSystem: 'geo',
          geoIndex: 0,
          emphasis: {
            label: {
              show: false,
            },
          },
          polyline: true,
          lineStyle: {
            color: '#c46e54',
            width: 0,
            // opacity: 0.8,
            // type: 'dotted',
          },
          effect: {
            show: true,
            period: 8,
            color: '#a10000',
            // roundTrip: true,
            // loop: false,
            // constantSpeed: 50,
            trailLength: 0,
            symbolSize: [12, 30],
            symbol:
              'path://M87.1667 3.8333L80.5.5h-60l-6.6667 3.3333L.5 70.5v130l10 10h80l10 -10v-130zM15.5 190.5l15 -20h40l15 20zm75 -65l-15 5v35l15 15zm-80 0l15 5v35l-15 15zm65 0l15 -5v-40l-15 20zm-50 0l-15 -5v-40l15 20zm 65,-55 -15,25 c -15,-5 -35,-5 -50,0 l -15,-25 c 25,-15 55,-15 80,0 z',
          },
          z: 100,
          data: [
            {
              effect: {
                color: '#fff',
                constantSpeed: 40,
                delay: 0,
              },
              coords: [
                [45, 100],
                [45, 170],
                [150, 170],
                [150, 333],
                [150, 480],
                [410, 480],
                [410, 420],
              ],
            },
            {
              effect: {
                color: '#ffff1a',
                constantSpeed: 40,
                delay: 0,
              },
              coords: [
                [525, 170],
                [590, 170],
                [590, 60],
                [800, 60],
                [800, 120],
                [1000, 120],
                [1000, 190],
              ],
            },
            {
              effect: {
                color: '#00ffbf',
                constantSpeed: 40,
                delay: 0,
              },
              coords: [
                [880, 380],
                [800, 380],
                [800, 460],
                [800, 520],
                [560, 520],
                [490, 490],
                [410, 490],
                [410, 410],
              ],
            },
            {
              effect: {
                color: '#66ccff',
                constantSpeed: 40,
                delay: 1000,
              },
              coords: [
                [575, 230],
                [575, 300],
                [830, 300],
                [830, 125],
                [1000, 125],
                [1000, 190],
              ],
            },
          ],
        },
      ],
    }
    myChart.setOption(option)
  })
}
</script>

<style scoped></style>
