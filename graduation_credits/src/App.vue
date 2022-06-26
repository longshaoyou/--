<template>
  <div id="app">
    <div class="LoginApp">
      <div class="formBox">
        <h1>获取学生课程信息</h1>
        <el-form
          status-icon
          ref="loginForm"
          :model="formData"
          :rules="rules"
          label-width="80px"
          label-position="left"
        >
          <el-form-item prop="username">
            <el-input v-model="formData.username" placeholder="账号"
              ><template slot="prepend"><i class="el-icon-user"></i></template
            ></el-input>
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              type="password"
              v-model="formData.password"
              autocomplete="off"
              placeholder="密码"
              :show-password="true"
              ><template slot="prepend"><i class="el-icon-view"></i></template
            ></el-input>
          </el-form-item>
          <el-form-item>
            <el-button
              class="loginBtn"
              type="primary"
              @click="submitForm('loginForm')"
              >登录</el-button
            >
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "app",
  data() {
    var validatePass = (rules, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        callback();
      }
    };
    return {
      formData: {
        username: "",
        password: "",
      },
      rules: {
        username: [{ required: true, message: "请输入账号", trigger: "blur" }],
        password: [{ validator: validatePass, trigger: "blur" }],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(async (valid) => {
        if (valid) {
          const params = new URLSearchParams();
          const { username, password } = this.formData;
          axios
            .post(
              "/api/get",
              {
                username,
                password,
              },
              {
                headers: {
                  "Content-Type":
                    " application/x-www-form-urlencoded;charset:utf-8;",
                },
              }
            )
            .then((res) => {
              console.log(res);
              const { data } = res;
              // const data = JSON.parse(res.data);
              console.log(data);
              if (data.code == 200) {
                this.$message({
                  message: data.msg,
                  type: "success",
                });
                window.open(data.data);
              } else {
                this.$message.error(data.msg);
              }
              // console.log("res", res);
            })
            .catch((err) => {
              this.$message.error("遇到错误，请检查输入的账号密码");
            });
        } else {
          return false;
        }
      });
    },
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
}
.LoginApp {
  width: 100vw;
  height: 100vh;
  background-color: rgb(43, 58, 75);
  display: flex;
  /* 横向剧中 */
  justify-content: center;
  /* 竖向剧中 */
  align-items: center;
}
.formBox {
  /* color: rgba(255,255,255,.7); */
  width: 400px;
  height: 300px;
  display: flex;
  flex-direction: column;
  /* 横向剧中 */
  justify-content: center;
  /* 竖向剧中 */
  align-items: center;
  color: white;
}
.el-form {
  margin-top: 30px;
}
h1 {
  font-size: 20px;
}
.loginBtn {
  width: 100%;
}
.el-form-item {
  margin-left: -80px;
}
</style>
