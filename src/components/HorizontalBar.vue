<template>
  <div>
    <div>区域人员数量</div>
    <div ref="target" class="w-full h-full"></div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  data: {
    type: Object,
    required: true,
  },
})
// console.log(data)
// 1.初始化echarts实例
let myChart = null

const target = ref(null)
onMounted(() => {
  myChart = echarts.init(target.value)
  renderChart()
})
// 2.构建option配置对象
const renderChart = () => {
  const options = {
    // x、y轴展示数据
    xAxis: {
      // 不显示轴
      show: false,
      // 作为数据进行展示
      type: 'value',
      // 指定最大值
      max: function (value) {
        return parseInt(value.max * 1.2)
      },
    },
    yAxis: {
      type: 'category',
      data: props.data.regions.map((item) => item.name),
      // 反向展示数据
      inverse: true,
      axisLine: {
        show: false,
      },
      axisTick: {
        show: false,
      },
      axisLabel: {
        color: '#9eb1c8',
      },
    },
    // 图表绘制的位置，对应 上下左右
    grid: {
      top: 0,
      right: 0,
      bottom: 0,
      left: 0,
      containLabel: true,
    },
    // 核心配置
    series: [
      {
        type: 'bar',
        data: props.data.regions.map((item) => ({
          name: item.name,
          value: item.value,
        })),
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180,180,180,0.2)',
        },
        itemStyle: {
          color: '#479AD3',
          borderRadius: 5,
          shadowColor: 'rgba(0,0,0,0.3)',
          shadowBlur: 5,
        },
        barWidth: 12,
        label: {
          show: true,
          position: 'right',
          color: '#fff',
        },
      },
    ],
  }
  myChart.setOption(options)
}
// 3.通过实例.setOption(options)

// 监听数据变化
watch(
  () => props.data,
  () => {
    renderChart()
  }
)
</script>

<style scoped></style>
