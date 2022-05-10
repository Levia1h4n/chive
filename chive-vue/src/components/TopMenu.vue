<template>
  <div>
    <!-- <Menu mode="vertical" theme="light" :accordion="true">
      <Menu v-for="(sub, name) in menus" :key="name" :name="name">
        <template slot="title">
          {{ name }}
        </template>
        <button
          v-for="(path, key) in getSubItems(sub)"
          :key="key"
          :name="key"
          :to="path"
        >
          {{ key }}
        </button>
      </Menu>
    </Menu> -->
  </div>
</template>

<script>
import TopMenu from './TopMenu'

export default {
  components: { TopMenu },
  name: 'TopMenu',
  data () {
    return {
      message: '',
      menu: {
        k线图: '/test/get',
        资产: '/scene/frontpage'
      },
      menus: {
        数据管理: {
          k123: '/test/get'
        },
        场景管理: {
          资产123: '/scene/frontpage',
          测试123: '/scene/tag'
        }
      }
    }
  },
  methods: {
    getData (cmd) {
      console.log(cmd)
      console.log(12321)
    },
    getMenuName (routeName, menu) {
      if (!menu) {
        menu = this.menus
      }
      for (const k in menu) {
        const v = menu[k]
        if (typeof v === 'string') {
          if (v === routeName) {
            return k
          }
        } else if (typeof v === 'object') {
          const r = this.getMenuName(routeName, v)
          if (r) {
            return r
          }
        }
      }
      return null
    },
    getSubItems (sub) {
      const r = {}
      for (const k in sub) {
        r[k] = sub[k]
      }
      return r
    }
  }
}
</script>

<style>
.ivu-drawer-mask {
  background-color: rgba(150, 150, 150, 0.2);
}
.ivu-drawer-body {
  padding: 0;
}
</style>
