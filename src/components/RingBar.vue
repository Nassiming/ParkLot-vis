<template>
  <div>
    <div>疏散完成度</div>
    <div ref="target" class="w-full h-full"></div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue'
import * as echarts from 'echarts'

let myChart = null

const target = ref(null)
const props = defineProps({
  data: {
    type: Object,
    required: true,
  },
})
onMounted(() => {
  myChart = echarts.init(target.value)
  renderChart()
})

const getSeriesData = () => {
  const series = []
  props.data.completes.forEach((item, index) => {
    series.push({
      name: item.name,
      type: 'pie',
      clockwise: false,
      hoverAnimation: false,
      radius: [75 - index * 15 + '%', 66 - index * 15 + '%'],
      center: ['55%', '55%'],
      label: {
        show: false,
      },
      data: [
        {
          value: item.value,
          name: item.name,
        },
        {
          value: 50,
          itemStyle: {
            color: 'rgba(0,0,0,0)',
            borderWidth: 0,
          },
          tooltip: {
            show: false,
          },
          hoverAnimation: false,
        },
      ],
    })

    series.push({
      name: item.name,
      type: 'pie',
      silent: true,
      z: 1,
      clockwise: false,
      hoverAnimation: false,
      radius: [75 - index * 15 + '%', 66 - index * 15 + '%'],
      center: ['55%', '55%'],
      label: {
        show: false,
      },
      data: [
        {
          value: 7.5,
          itemStyle: {
            color: 'rgba(3,31,62)',
            borderWidth: 0,
          },
          tooltip: {
            show: false,
          },
          hoverAnimation: false,
        },
        {
          value: 2.5,
          itemStyle: {
            color: 'rgba(0,0,0,0)',
            borderWidth: 0,
          },
          tooltip: {
            show: false,
          },
          hoverAnimation: false,
        },
      ],
    })
  })

  return series
}

const renderChart = () => {
  const option = {
    legend: {
      show: true,
      icon: 'circle',
      top: '14%',
      left: '60%',
      data: props.data.completes.map((item) => item.name),
      width: -5,
      itemWidth: 10,
      itemHeight: 10,
      itemGap: 6,
      textStyle: {
        fontSize: 10,
        lineHeight: 5,
        color: 'rgba(255,255,255,0.8)',
      },
    },
    tooltip: {
      show: true,
      trigger: 'item',
      formatter: '{a}<br>{b}:{c}({d}%)',
    },
    yAxis: [
      {
        type: 'category',
        inverse: true,
        axisLine: {
          show: false,
        },
      },
    ],
    xAxis: [
      {
        show: false,
      },
    ],
    series: getSeriesData(),
  }
  myChart.setOption(option)
}

watch(
  () => props.data,
  () => {
    renderChart()
  }
)
</script>

<style scoped></style>
