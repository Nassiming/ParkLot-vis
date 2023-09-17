<template>
  <div>
    <div>云端报警风险</div>
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
const renderChart = () => {
  const option = {
    radar: {
      axisName: {
        color: '#05D5FF',
        fontSize: 14,
      },
      shape: 'polygon',
      center: ['50%', '50%'],
      radius: '80%',
      startAngle: 120,
      axisLine: {
        lineStyle: {
          color: 'rgba(5,213,255,0.8)',
        },
      },
      splitLine: {
        show: true,
        lineStyle: {
          width: 1,
          color: 'rgba(5,213,255,0.8)',
        },
      },
      indicator: props.data.risks.map((item) => ({
        name: item.name,
        max: 100,
      })),
      splitArea: {
        show: false,
      },
    },
    polar: {
      center: ['50%', '50%'],
      radius: '0%',
    },
    angleAxis: {
      min: 0,
      interval: 5,
      clockwise: false,
    },
    radiusAxis: {
      min: 0,
      interval: 20,
      splitLine: {
        show: true,
      },
    },
    series: {
      type: 'radar',
      Symbol: 'circle',
      symbolSize: 6,
      itemStyle: {
        normal: {
          color: 'rgba(255, 145, 124, 0.9)',
        },
      },
      areaStyle: {
        normal: {
          color: 'rgba(255, 145, 124, 0.9)',
          opacity: 0.5,
        },
      },
      lineStyle: {
        width: 2,
        color: 'rgba(255, 145, 124, 0.9)',
      },
      label: {
        normal: {
          show: true,
          color: '#fff',
        },
      },
      data: [
        {
          value: props.data.risks.map((item) => item.value),
        },
      ],
    },
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
