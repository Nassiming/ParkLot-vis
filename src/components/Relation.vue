<template>
  <div>
    <div>数据传递网络</div>
    <div ref="target" class="w-full h-full font-[Alimama ShuHeiTi Bold]"></div>
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

let myChart = null
const target = ref(null)
onMounted(() => {
  myChart = echarts.init(target.value)
  renderChart()
})

const renderChart = () => {
  const option = {
    xAxis: {
      show: false,
      type: 'value',
    },
    yAxis: {
      show: false,
      type: 'value',
    },
    series: [
      // 圆
      {
        type: 'graph',
        layout: 'none',
        coordinateSystem: 'cartesian2d',
        symbolSize: 24,
        z: 3,
        edgeLabel: {
          normal: {
            show: true,
            color: '#fff',
            textStyle: {
              fontSize: 10,
            },
            formatter: function (params) {
              return params.data.speed
            },
          },
        },
        label: {
          normal: {
            show: true,
            position: 'bottom',
            color: '#5e5e5e',
            textStyle: {
              fontSize: 10,
            },
          },
        },
        edgeSymbol: ['none', 'arrow'],
        edgeSymbolSize: 8,
        data: props.data.relations.map((item) => {
          if (item.id != 0) {
            return {
              name: item.name,
              category: 0,
              active: true,
              speed: `${item.speed}kb/s`,
              value: item.value,
            }
          } else {
            return {
              name: item.name,
              value: item.value,
              symbolSize: 80,
              itemStyle: {
                normal: {
                  color: {
                    colorStops: [
                      {
                        offset: 0,
                        color: '#157eff',
                      },
                      {
                        offset: 1,
                        color: '#35c2ff',
                      },
                    ],
                  },
                },
              },
              label: {
                fontSize: 12,
              },
            }
          }
        }),
        // 连接线
        links: props.data.relations.map((item, index) => ({
          source: item.source,
          target: item.target,
          speed: `${item.speed}kb/s`,
          lineStyle: {
            normal: {
              color: '#12b5d0',
              curveness: 0.2,
            },
          },
          label: {
            show: true,
            position: 'middle',
            offset: [10, 0], // 偏移
          },
        })),
      },
      // 动态的线
      {
        // coordinateSystem: 'bmap',
        type: 'lines',
        coordinateSystem: 'cartesian2d',
        z: 1,
        // 线特效
        effect: {
          show: true,
          smooth: false,
          trailLength: 0,
          symbol: 'arrow',
          color: 'rgba(55,155,255,0.6)',
          symbolSize: 12,
        },
        lineStyle: {
          normal: {
            curveness: 0.2,
          },
        },
        data: [
          [{ coord: [0, 300] }, { coord: [50, 200] }],
          [{ coord: [0, 100] }, { coord: [50, 200] }],
          [{ coord: [50, 200] }, { coord: [100, 100] }],
          [{ coord: [50, 200] }, { coord: [100, 300] }],
        ],
      },
    ],
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
