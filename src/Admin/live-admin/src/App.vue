<script>
export default {
  data() {
    return {
      table: [{ option: "", label: "" }],
      title: "",
      time: "60",
      ifOn: false,
    };
  },
  computed: {},
  methods: {
    // 动态添加
    addInput() {
      this.table.push({ option: "", label: "" });
    },
    submit() {
      this.ifOn = true;
      axios({
        method: "post",
        url: "http://127.0.0.1/test",
        data: {
          title: this.title,
          table: this.table,
        },
      })
        .then(function (response) {
          alert("发布成功！" + response);
        })
        .catch(function (error) {
          alert("发布失败！" + error);
        });
    },
    stop() {
      this.ifOn = false;
      axios({
        method: "post",
        url: "http://127.0.0.1/test",
        data: {
          ifOn: this.ifOn,
        },
      })
        .then(function (response) {
          alert("终止成功！" + response);
        })
        .catch(function (error) {
          alert("终止失败！" + error);
        });
    },
    reset() {
      this.table = [{ option: "", label: "" }];
    },
  },
};
</script>

<template>
  <div class="main">
    本轮投票题目：<input v-model="this.title" /> <br />
    设定时间：(单位：秒) <input v-model="this.time" type="number" />
    <div v-for="item in table" :key="item.option">
      选项：
      <el-select v-model="item.option">
        <el-option value="A">A</el-option>
        <el-option value="B">B</el-option>
        <el-option value="C">C</el-option>
        <el-option value="D">D</el-option>
        <el-option value="E">E</el-option>
      </el-select>
      <br />
      标签：<input v-model="item.label" />
    </div>
    <el-button @click="addInput">添加选项</el-button>
    <el-button @click="reset">重置表单</el-button>
    <el-button @click="submit">发布提交</el-button>
    <el-button @click="stop">终止投票</el-button>
  </div>

  <br />
  <div v-for="i in table" :key="i.id">
    选项为：{{ i.option }}
    <span v-html="'\u00a0\u00a0\u00a0\u00a0\u00a0'"></span>
    标签为：{{ i.label }}
  </div>
  <div>
    <br />
    投票题目 为：{{ title }} <br />
    设定时间 为：{{ time }} 秒<br />
  </div>
</template>
