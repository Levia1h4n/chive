<template>
  <div>
    <span class="title">Chive</span>

    <div>
      <button @click="getData('k线图')">k线图</button>
      <button @click="getData('')">资产</button>
      <button @click="getStockData">查股票数据</button>
    </div>

    <div>
      <h1>Echarts绘制k线图</h1>
      <div id='echartContainer' ref='echartContainer' style='width:100%; height:400px; position: relative;'></div>
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
    // macd计算
    splitData( rawData ) {
      var categoryData = []
      var values = []
      var macds = []
      var difs = []
      var deas = []
      for (var i = 0; i < rawData.length; i++) {
        categoryData.push( rawData[i].splice(0, 1)[0] )
        values.push( rawData[i] )
        macds.push( rawData[i][6] )
        difs.push( rawData[i][7] )  
        deas.push( rawData[i][8] )  
      }
      return {
        categoryData: categoryData,
        values: values,
        macds: macds,
        difs: difs,
        deas: deas
      }
    },
    // ma均线函数
    calculateMA(dayCount, data0) {
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
        result.push(sum / dayCount)
      }
      return result
    },
    getStockData () {
      var path =
        'http://127.0.0.1:5000/data?stock_code=603912.SH&date_from=2020-03-01&date_to=2020-04-01'
      axios
        .get(path)
        .then(res => {
          var data = res.data.data
          var msg = res.data.msg
          // 这里实现的是一个比较简单的，可以按照需求将函数移动到methods函数中
          var data0 = this.$options.methods.splitData(data);
          console.log(data0)
          var echarts = require('echarts');
          // k线配置项
          var option = {
                legend: {
                      // bottom: auto,
                      left: 'center',
                      data: ['MA5', 'MA10', 'MA20', 'MA30']
                      // data: ['Dow-Jones index', 'MA5', 'MA10', 'MA20', 'MA30']
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
                    axisLine: { onZero: false },
                    axisTick: { show: false },
                    splitLine: { show: false },
                    axisLabel: { show: true },
                    axisLine: {
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
                    name: '555',
                    type: 'candlestick',
                    data: data0.values,
                    markPoint: {
                      data: [
                        {
                          name: 'XX标点'
                        }
                      ]
                    },
                    markLine: {
                      silent: true,
                      data: [
                        {
                          yAxis: 2222
                        }
                      ]
                    }
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
                  {
                    name: 'MACD',
                    type: 'bar',
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    data: data0.macds,
                    itemStyle: {
                      normal: {
                        color: function(params) {
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
                  },
                  {
                    name: 'DIF',
                    type: 'line',
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    data: data0.difs
                  },
                  {
                    name: 'DEA',
                    type: 'line',
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    data: data0.deas
                  }
                ]
          }
          // 进行初始化
          var charts = echarts.init(this.$refs.echartContainer)
          charts.setOption(option)
          // console.log(data)
          // console.log(msg)
          // for (var i = 0; i < data.length; i++) {
          //   console.log(data[i])
          // }
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
