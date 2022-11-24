<script>
export default {
  data() {
    return {
      table: [{ option: "", label: "" }],
      title: "",
      time: "60",
      option_list: [],
    };
  },
  computed: {},
  methods: {
    // 动态添加
    addInput() {
      this.table.push({ option: "", label: "" });
    },
    // 查看
    search() {
      console.log(this.table);
      console.log(this.title);
      console.log(this.time);
    },
    submit() {
      axios({
        method: "get",
        url: "",
        data: {
          title: this.title,
          table: this.table,
        },
      });
    },
    reset() {},
  },
};
</script>

<template>
  <div class="main">
    本轮投票：<input v-model="this.title" /> <br />
    设定时间：(单位：秒) <input v-model="this.time" type="number" />
    <div v-for="item in table" :key="item.option">
      选项：
      <select v-model="item.option">
        <option value="A">A</option>
        <option value="B">B</option>
        <option value="C">C</option>
        <option value="D">D</option>
        <option value="E">E</option>
      </select>
      <br />
      标签：<input v-model="item.label" />
    </div>
    <button @click="addInput">添加选项</button>
    <button @click="search">查看选项</button>
    <button @click="reset">更新表单</button>
    <button @click="submit">提交</button>
  </div>

  <br />
  <div v-for="i in table" :key="i.id">
    选项为：{{ i.option }}
    <span v-html="'\u00a0\u00a0\u00a0\u00a0\u00a0'"></span>
    标签为：{{ i.label }}
  </div>
  <div>
    <br />
    题目 为：{{ title }} <br />
    设定时间 为： {{ time }} 秒<br />
  </div>
</template>
