<template>
  <div>
    <div>累计疏散车辆</div>
    <div ref="target" class="w-full h-full"></div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue'
import * as echarts from 'echarts'
import seriesData from '../assets/data/seriesData.json'

let myChart = null
const target = ref(null)
onMounted(() => {
  myChart = echarts.init(target.value)
  renderChart(seriesData)
})

function run(_rawData) {
  const countries = ['Zone 1', 'Zone 2', 'Zone 3', 'Zone 4', 'Zone 5', 'Zone 6']
  const datasetWithFilters = []
  const seriesList = []
  echarts.util.each(countries, function (country) {
    let datasetId = 'dataset_' + country
    datasetWithFilters.push({
      id: datasetId,
      fromDatasetId: 'dataset_raw',
      transform: {
        type: 'filter',
        config: {
          and: [
            { dimension: 'Date', gte: 0 },
            { dimension: 'Zone', '=': country },
          ],
        },
      },
    })
    seriesList.push({
      type: 'line',
      datasetId: datasetId,
      showSymbol: false,
      name: country,
      endLabel: {
        show: true,
        formatter: function (params) {
          return params.value[0]
        },
        fontSize: 10,
      },
      labelLayout: {
        moveOverlap: 'shiftY',
      },
      emphasis: {
        focus: 'series',
      },
      encode: {
        x: 'Date',
        y: 'Number',
        label: ['Zone', 'Number'],
        itemName: 'Date',
        tooltip: ['Number'],
      },
    })
  })
  const option = {
    animationDuration: 8000,
    dataset: [
      {
        id: 'dataset_raw',
        source: _rawData,
      },
      ...datasetWithFilters,
    ],
    title: {
      show: false,
    },
    tooltip: {
      order: 'valueDesc',
      trigger: 'axis',
    },
    xAxis: {
      type: 'category',
      nameLocation: 'middle',
    },
    yAxis: {
      name: 'Number',
      axisLabel: {
        formatter: function (value, index) {
          return value / 1000 + 'e3'
        },
      },
    },
    grid: {
      right: 45,
      bottom: 50,
      left: 30,
      top: 10,
    },
    series: seriesList,
  }
  myChart.setOption(option)
}

const renderChart = (_rawData) => {
  run(_rawData)
}
</script>

<style scoped></style>
