<template>
  <div class="data">
    <div class="DataBox">
      <el-row>
        <el-col :span="18">
          <div class="grid-content bg-purple">
            <h2 class="title">控制面板</h2>
            <div class="time">
              <el-input placeholder="时间" v-model="problemtime">
                <template slot="prepend">时间 ：</template>
              </el-input>
            </div>
            <div>
              <el-input placeholder="请输入内容" v-model="problemContent">
                <template slot="prepend">问题 ：</template>
              </el-input>
            </div>
            <div class="Options">
              <div class="option" v-for="(value, key) in options" :key="key">
                <el-tag class="tag">{{ key }}</el-tag>
                <el-input class="optionvalue" v-model="options[key]"></el-input>
              </div>
              <div class="new">
                <el-button type="primary" round @click="newOption">新增选项</el-button>
              </div>
            </div>
            <div>
              <el-button type="primary" @click="submit" round>发布提交</el-button>
              <el-button type="primary" @click="reset" round>重置表单</el-button>
              <el-button type="primary" @click="stop" round>终止投票</el-button>
            </div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content bg-purple-light">
            <h4 class="title"> 预设选择</h4>
            <el-select v-model="value" placeholder="请选择">
              <el-option v-for="item in opts" :key="item.value" :label="item.label" :value="item.value">
              </el-option>
            </el-select>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import { Stop, Submit } from '../request/api'
export default {
  name: 'DataBox',
  data() {
    return {
      problemContent: '',
      problemtime: 60,
      options: {

      },
      opts: [{
        value: '选项1',
        label: '预设一'
      }, {
        value: '选项2',
        label: '预设二'
      }, {
        value: '选项3',
        label: '预设三'
      }, {
        value: '选项4',
        label: '预设四'
      }, {
        value: '选项5',
        label: '预设五'
      }, {
        value: '选项6',
        label: '预设六'
      }, {
        value: '选项7',
        label: '预设七'
      }, {
        value: '选项8',
        label: '预设八'
      }],
      value: ''
    }
  },
  methods: {
    newOption() {
      if (Object.keys(this.options).length === 0) { this.$set(this.options, 'A', '') } else if (Object.keys(this.options).length === 1) { this.$set(this.options, 'B', '') } else if (Object.keys(this.options).length === 2) { this.$set(this.options, 'C', '') } else if (Object.keys(this.options).length === 3) { this.$set(this.options, 'D', '') } else if (Object.keys(this.options).length === 4) { this.$set(this.options, 'E', '') }
    },
    submit() {
      submit()
    },
    stop() {
      stop()
    },
    reset() {

    }
  },
  props: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.data {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.DataBox {
  width: 77%;
}

.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf;
}

.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.title {
  text-align: center;
}

.time {
  width: 26%;
}

.option {
  width: 60%;
  padding: 4px;
  display: inline-block;
}

.new {
  width: 29%;
  display: inline-block;
}

.optionvalue {
  width: 66%;
  display: inline-block;
}

.tag {
  display: inline-block;
}
</style>
