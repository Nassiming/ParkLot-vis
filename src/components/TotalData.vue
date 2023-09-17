<template>
  <div>
    <div class="p-6">
      <div class="text-slate-300 text-center">
        数据总量：
        <span ref="totalCountTarget" class="text-7xl ml-2 mr-2 font-bold font-[Electronic] text-gradient"> 679,473,929 </span>
        条记录
      </div>
      <div class="mt-3 flex flex-wrap">
        <div class="w-1/3 text-center text-slate-400 text-sm">
          区域1：
          <span ref="city1" class="text-[#5DC5EF] text-3xl font-[Electronic]"> 8,778,988 </span>
        </div>
        <div class="w-1/3 text-center text-slate-400 text-sm">区域2：<span ref="city2" class="text-[#5DC5EF] text-3xl font-[Electronic]">8,778,988</span></div>
        <div class="w-1/3 text-center text-slate-400 text-sm">区域3：<span ref="city3" class="text-[#5DC5EF] text-3xl font-[Electronic]">8,778,988</span></div>
        <div class="w-1/3 text-center text-slate-400 text-sm">区域4：<span ref="city4" class="text-[#5DC5EF] text-3xl font-[Electronic]">8,778,988</span></div>
        <div class="w-1/3 text-center text-slate-400 text-sm">区域5：<span ref="city5" class="text-[#5DC5EF] text-3xl font-[Electronic]">8,778,988</span></div>
        <div class="w-1/3 text-center text-slate-400 text-sm">区域6：<span ref="city6" class="text-[#5DC5EF] text-3xl font-[Electronic]">8,778,988</span></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { CountUp } from 'countup.js'
const props = defineProps({
  data: {
    type: Object,
    required: true,
  },
})

const totalCountTarget = ref(null)
const city1 = ref(null)
const city2 = ref(null)
const city3 = ref(null)
const city4 = ref(null)
const city5 = ref(null)
const city6 = ref(null)

onMounted(() => {
  new CountUp(totalCountTarget.value, props.data.total).start()
  new CountUp(city1.value, props.data['区域1']).start()
  new CountUp(city2.value, props.data['区域2']).start()
  new CountUp(city3.value, props.data['区域3']).start()
  new CountUp(city4.value, props.data['区域4']).start()
  new CountUp(city5.value, props.data['区域5']).start()
  new CountUp(city6.value, props.data['区域6']).start()
})
</script>

<style scoped></style>
