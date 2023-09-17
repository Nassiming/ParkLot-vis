import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { inject } from 'vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    inject({
      $: 'jquery',
      jQuery: 'jquery',
      'windows.jQuery': 'jquery',
    }),
  ],
  base: '/ParkLot_vis/',
  resolve: {
    alias: {
      '@': './src',
    },
  },
  server: {
    hmr: true,
  },
})
