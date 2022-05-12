<template>
  <div>
    <span class="title">Quatitative Trading Platform</span>
    <br />
    <br />
    <!-- <span style="font-size = 200px">Quatitative Trading Platform</span> -->

    <div class="buttonSet">
      <button @click="getAsset()">Personal Asset</button>
      <button @click="getBuy()">Buy</button>
      <button @click="getSell()">Sell</button>
      <button @click="getStockData()">Candlestick</button>
      <button @click="getTrack()">Track</button>
      <button @click="getTrackCancel()">Track Cancel</button>
      <button @click="getTrackList()">Track List</button>
    </div>
    <br />

    <!-- <div>
      <h1>Draw Candlestick</h1>
      <div
        id="echartContainer"
        ref="echartContainer"
        style="width: 100%; height: 400px; position: relative"
      ></div>
    </div> -->

    <div class="inputArea">
      <input v-model="arg1" placeholder="edit me" />
      <br />
      <p>stock_code / acct: {{ arg1 }}</p>
      <br />
      <input v-model="arg2" placeholder="edit me" />
      <br />
      <p>date_from / pwd: {{ arg2 }}</p>
      <br />
      <input v-model="arg3" placeholder="edit me" />
      <br />
      <p>date_to is / stock_code: {{ arg3 }}</p>
      <br />
      <input v-model="arg4" placeholder="edit me" />
      <br />
      <p>amount: {{ arg4 }}</p>
    </div>

    <br />

    <center>
      <div v-if="showchart" class="chart">
        <!-- <h2>kchart</h2> -->

        <div
          id="echartContainer"
          ref="echartContainer"
          style="width: 80%; height: 600px"
        ></div>
      </div>
    </center>

    <div v-if="showrecord" class="asset">
      <table>
        <thead>
          <tr>
            <th>stock number</th>
            <th>volume</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="(record, index) in records" v-bind:key="index">
            <td>
              {{ record.key }}
            </td>
            <td>
              {{ record.val }}
            </td>
          </tr>
        </tbody>
      </table>
      <!-- <ul>
        <li style="width: 200px; font-size: 20px; font-weight: 700">
          stock:volume
        </li>
        <li
          v-for="(record, index) in records"
          v-bind:key="index"
          style="width: 200px"
        >
          {{ record.key }}: {{ record.val }}
        </li>
      </ul> -->
    </div>
  </div>
</template>

<style scoped>
table {
  border-collapse: collapse;
  /* margin: 0 auto; */
  text-align: center;
}

table td,
table th {
  border: 1px solid #cad9ea;
  color: #666;
  height: 30px;
}

table thead th {
  background: #84cbd3;
  width: 200px;
}

table tr:nth-child(odd) {
  background: #fff;
}

table tr:nth-child(even) {
  background: #f5fafa;
}

.asset {
  position: relative; 
  bottom: 700px; 
  left: 400px
}
</style>

<script>
import axios from 'axios'
// import util from '../util'

export default {
  name: 'Admin',
  data () {
    return {
      arg1: '',
      arg2: '',
      arg3: '',
      arg4: '',
      records: [],
      charts: null,
      // r: null,
      // msg: null,
      menu: {
        k线图: '/t1/t2',
        资产: '/t3/t4'
      },
      showchart: false,
      showrecord: false
    }
  },
  methods: {
    getInput () {
      return [this.arg1, this.arg2, this.arg3, this.arg4]
    },
    getTrack () {
      var input = this.getInput()
      console.log('input: ', input)

      var path = 'http://127.0.0.1:5000/track?stock_code=' + input[0]
      console.log('URL: ', path)

      axios
        .get(path, { headers: { 'Access-Control-Allow-Origin': '*' } })
        .then(res => {
          var data = res.data
          console.log('data: ', data)
          // TODO
        })
        .catch(error => {
          console.error(error)
        })
    },
    getTrackCancel () {
      var input = this.getInput()
      console.log('input: ', input)

      var path = 'http://127.0.0.1:5000/track_cancel?stock_code=' + input[0]
      console.log('URL: ', path)

      axios
        .get(path, { headers: { 'Access-Control-Allow-Origin': '*' } })
        .then(res => {
          var data = res.data
          console.log('data: ', data)
          // TODO
        })
        .catch(error => {
          console.error(error)
        })
    },
    getTrackList () {
      var path = 'http://127.0.0.1:5000/track_list'
      console.log('URL: ', path)

      axios
        .get(path, { headers: { 'Access-Control-Allow-Origin': '*' } })
        .then(res => {
          var data = res.data
          console.log('data: ', data)
          // TODO
        })
        .catch(error => {
          console.error(error)
        })
    },
    getAsset () {
      this.showrecord = true
      this.showchart = true
      var input = this.getInput()
      console.log('input: ', input)

      var path =
        'http://127.0.0.1:5000/asset?acct=' + input[0] + '&pwd=' + input[1]
      console.log('URL: ', path)

      axios
        .get(path, { headers: { 'Access-Control-Allow-Origin': '*' } })
        .then(res => {
          var data = res.data.data.stocks
          var msg = res.data.msg
          console.log('data: ', data)
          var data1 = []
          for (var i in data) {
            // 用javascript的for/in循环遍历对象的属性
            console.log('key: ', i, '  val: ', data[i])
            data1.push({ key: i, val: data[i] })
          }
          console.log('msg: ', msg)

          // for (var i = 0; i < data.length; i++) {
          //   data1.push(data[i])
          // }

          console.log('data1', data1)
          // 把data显示出来就行
          this.records = data1
        })
        .catch(error => {
          console.error(error)
        })
    },
    getBuy () {
      var input = this.getInput()
      console.log('input: ', input)

      var path =
        'http://127.0.0.1:5000/buy?acct=' +
        input[0] +
        '&pwd=' +
        input[1] +
        '&stock_code=' +
        input[2] +
        '&amount=' +
        input[3]
      console.log('URL: ', path)

      axios
        .get(path, { headers: { 'Access-Control-Allow-Origin': '*' } })
        .then(res => {
          var data = res.data
          var msg = res.data.msg
          console.log('data: ', data)
          console.log('msg: ', msg)
        })
        .catch(error => {
          console.error(error)
        })
      this.getAsset ()
    },
    getSell () {
      var input = this.getInput()
      console.log('input: ', input)

      var path =
        'http://127.0.0.1:5000/sell?acct=' +
        input[0] +
        '&pwd=' +
        input[1] +
        '&stock_code=' +
        input[2] +
        '&amount=' +
        input[3]
      console.log('URL: ', path)

      axios
        .get(path, { headers: { 'Access-Control-Allow-Origin': '*' } })
        .then(res => {
          var data = res.data
          var msg = res.data.msg
          console.log('data: ', data)
          console.log('msg: ', msg)
        })
        .catch(error => {
          console.error(error)
        })
    },
    // macd计算
    splitData (rawData) {
      var categoryData = []
      var values = []
      var volumes = []
      var tag = []
      // var macds = []
      // var difs = []
      // var deas = []
      for (var i = 0; i < rawData.length; i++) {
        categoryData.push(rawData[i].splice(0, 1)[0])
        var temp = rawData[i][4]
        rawData[i][4] = rawData[i][3]
        rawData[i][3] = temp
        volumes.push(rawData[i][5] * (rawData[i][2] >= rawData[i][1] ? 1 : -1))
        tag.push(rawData[i][2] >= rawData[i][1] ? 1 : -1)
        values.push(rawData[i].splice(1, 5))
        // macds.push(rawData[i][6])
        // difs.push(rawData[i][7])
        // deas.push(rawData[i][8])
      }
      return {
        categoryData: categoryData,
        values: values,
        tag: tag,
        volumes: volumes
        // macds: macds,
        // difs: difs,
        // deas: deas
      }
    },
    // ma均线函数
    calculateMA (dayCount, data0) {
      var result = []
      for (var i = 0, len = data0.values.length; i < len; i++) {
        if (i < dayCount) {
          result.push('-')
          continue
        }
        var sum = 0
        for (var j = 0; j < dayCount; j++) {
          sum += data0.values[i - j][1]
        }
        result.push(+(sum / dayCount).toFixed(3))
        // result.push(sum / dayCount)
      }
      return result
    },
    getStockData () {
      // this.showrecord = true
      this.showchart = true
      var input = this.getInput()
      console.log('input: ', input)

      if (
        input[0].length !== 9 ||
        input[1].length !== 10 ||
        input[2].length !== 10
      ) {
        alert(
          'Invalid input\ne.g.\narg1: 603912.SH\narg2: 2020-03-01\narg3: 2020-04-01'
        )
        return
      }
      var path =
        'http://127.0.0.1:5000/data?stock_code=' +
        input[0] +
        '&date_from=' +
        input[1] +
        '&date_to=' +
        input[2]
      console.log('URL: ', path)

      // var path =
      //   'http://127.0.0.1:5000/data?stock_code=603912.SH&date_from=2020-03-01&date_to=2020-04-01'
      axios
        .get(path, { headers: { 'Access-Control-Allow-Origin': '*' } })
        .then(res => {
          var data = res.data.data
          console.log(data)
          // 这里实现的是一个比较简单的，可以按照需求将函数移动到methods函数中
          var data0 = this.$options.methods.splitData(data)
          console.log(data0)
          var echarts = require('echarts')
          // k线配置项
          var option = {
            legend: {
              // bottom: auto,
              left: 'center',
              // data: ['MA5', 'MA10', 'MA20', 'MA30']
              data: ['Dow-Jones index', 'MA5', 'MA10', 'MA20', 'MA30']
            },
            tooltip: {
              trigger: 'axis',
              axisPointer: {
                type: 'cross'
              }
            },
            grid: [
              {
                left: '3%',
                top: '0',
                height: '75%'
              },
              {
                left: '3%',
                right: '10%',
                top: '80%',
                height: '10%'
              }
            ],
            xAxis: [
              {
                type: 'category',
                data: data0.categoryData,
                scale: true,
                boundaryGap: false,
                axisLine: {
                  onZero: false,
                  lineStyle: {
                    color: 'red'
                  }
                },
                splitLine: {
                  show: false
                },
                splitNumber: 20
              },
              {
                type: 'category',
                gridIndex: 1,
                data: data0.categoryData,
                axisLabel: { show: false }
              }
            ],
            yAxis: [
              {
                scale: true,
                splitArea: {
                  show: true
                },
                axisLine: {
                  lineStyle: {
                    color: 'red'
                  }
                },
                position: 'right'
              },
              {
                gridIndex: 1,
                splitNumber: 3,
                // axisLine: { onZero: false },
                axisTick: { show: false },
                splitLine: { show: false },
                axisLabel: { show: true },
                axisLine: {
                  onZero: false,
                  lineStyle: {
                    color: 'red'
                  }
                },
                position: 'right'
              }
            ],
            dataZoom: [
              {
                type: 'inside',
                start: 100,
                end: 80
              },
              {
                show: true,
                type: 'slider',
                y: '90%',
                start: 50,
                end: 100
              },
              {
                show: false,
                xAxisIndex: [0, 1],
                type: 'slider',
                start: 20,
                end: 100
              }
            ],
            series: [
              {
                name: 'Dow-Jones index',
                type: 'candlestick',
                data: data0.values
                // markPoint: {
                //   data: [
                //     {
                //       name: 'XX标点'
                //     }
                //   ]
                // },
                // markLine: {
                //   silent: true,
                //   data: [
                //     {
                //       yAxis: 2222
                //     }
                //   ]
                // }
              },
              {
                name: 'MA5',
                type: 'line',
                data: this.$options.methods.calculateMA(5, data0),
                // data: calculateMA(5),
                smooth: true,
                lineStyle: {
                  normal: {
                    opacity: 0.5
                  }
                }
              },
              {
                name: 'MA10',
                type: 'line',
                data: this.$options.methods.calculateMA(10, data0),
                // data: calculateMA(10),
                smooth: true,
                lineStyle: {
                  normal: {
                    opacity: 0.5
                  }
                }
              },
              {
                name: 'MA20',
                type: 'line',
                data: this.$options.methods.calculateMA(20, data0),
                // data: calculateMA(20),
                smooth: true,
                lineStyle: {
                  normal: {
                    opacity: 0.5
                  }
                }
              },
              {
                name: 'MA30',
                type: 'line',
                data: this.$options.methods.calculateMA(30, data0),
                // data: calculateMA(30),
                smooth: true,
                lineStyle: {
                  normal: {
                    opacity: 0.5
                  }
                }
              },
              // {
              //   name: 'Volume',
              //   type: 'bar',
              //   xAxisIndex: 1,
              //   yAxisIndex: 1,
              //   data: data0.volumes
              // }
              {
                name: 'Vol',
                type: 'bar',
                xAxisIndex: 1,
                yAxisIndex: 1,
                data: data0.volumes,
                itemStyle: {
                  normal: {
                    color: function (params) {
                      var colorList
                      if (params.data >= 0) {
                        colorList = '#ef232a'
                      } else {
                        colorList = '#14b143'
                      }
                      return colorList
                    }
                  }
                }
              }
              // {
              //   name: 'DIF',
              //   type: 'line',
              //   xAxisIndex: 1,
              //   yAxisIndex: 1,
              //   data: data0.difs
              // },
              // {
              //   name: 'DEA',
              //   type: 'line',
              //   xAxisIndex: 1,
              //   yAxisIndex: 1,
              //   data: data0.deas
              // }
            ]
          }
          if (this.charts !== null && this.charts !== undefined) {
            this.charts.dispose()
          }
          // 进行初始化
          this.charts = echarts.init(this.$refs.echartContainer)
          this.charts.setOption(option)
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
      console.log('URL: ', path)
      // var msg = ''
      axios
        .get(path, { headers: { 'Access-Control-Allow-Origin': '*' } })
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
