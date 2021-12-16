import { defineConfig } from 'vite'
import path from 'path'
import Vue from '@vitejs/plugin-vue'
import Pages from 'vite-plugin-pages'
import Layouts from 'vite-plugin-vue-layouts'
import Icons from 'unplugin-icons/vite'
import IconsResolver from 'unplugin-icons/resolver'
import Components from 'unplugin-vue-components/vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    Vue(),
    Pages(),
    Layouts(),
    Icons(),
    Components({
      resolvers: [
        // auto import icons
        IconsResolver({
          prefix: 'icon'
        })
      ],
      dts: 'src/components.d.ts'
    })
  ],
  resolve: {
    alias: {
      '~': path.resolve(__dirname, './src')
    }
  }
})
