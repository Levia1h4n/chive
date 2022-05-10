<template>
  <div>
    <span class="title">Chive</span>

    <div>
      <button @click="getData('k线图')">k线图</button>
      <button @click="getData('')">资产</button>
      <button @click="getStockData">查股票数据</button>
    </div>

    <div>
      <input v-model="stock_code" placeholder="edit me" />
      <p>stock_code is: {{ stock_code }}</p>
      <input v-model="date_from" placeholder="edit me" />
      <p>date_from is: {{ date_from }}</p>
      <input v-model="date_to" placeholder="edit me" />
      <p>date_to is: {{ date_to }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import util from '../util'

export default {
  name: 'Admin',
  data () {
    return {
      stock_code: '',
      date_from: '',
      date_to: '',
      // r: null,
      // msg: null,
      menu: {
        k线图: '/t1/t2',
        资产: '/t3/t4'
      }
    }
  },
  methods: {
    getStockData () {
      var path =
        'http://127.0.0.1:5000/data?stock_code=603912.SH&date_from=2020-03-01&date_to=2020-04-01'
      axios
        .get(path)
        .then(res => {
          var data = res.data.data
          var msg = res.data.msg
          console.log(data)
          console.log(msg)
          for (var i = 0; i < data.length; i++) {
            console.log(data[i])
          }
        })
        .catch(error => {
          console.error(error)
        })
    },
    getData (cmd) {
      var path = 'http://127.0.0.1:5000/test/get'
      if (cmd !== '') {
        path += '?arg=1'
      }
      console.log(path)
      // var msg = ''
      axios
        .get(path)
        .then(res => {
          var data = res.data.data
          var msg = res.data.msg
          console.log(data, 'after')
          console.log(msg, 'after')
          for (var i = 0; i < data.length; i++) {
            console.log(data[i])
          }
          // let msg = res.data.msg
          // this.serverResponse = msg
          // alter('Success' + response.status + ',' + response.data + ',' + msg)
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
}
</script>

<style scoped>
.title {
  margin-left: 20px;
  margin-right: 20px;
  font-family: "Times New Roman", Times, serif;
  font-weight: 400;
  font-size: 26px;
}
</style>
