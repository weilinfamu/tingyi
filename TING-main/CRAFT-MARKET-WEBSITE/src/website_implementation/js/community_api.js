const FormData = require('form-data');

const fetch = require('node-fetch');

// 替换为实际的 API 端点 URL
const baseURL = "https://damp-castle-86239-1b70ee448fbd.herokuapp.com/decoapi/community_events/";

// 准备要创建的事件数据
var formData = new FormData();
formData.append("name", "Yoga in a tree 4");
formData.append("location", "Morningside Forest");
formData.append("organiser", "Morningside Community Wellness Collective");
formData.append("event_type", "Group Activity");
formData.append("description", "Doing yoga in a tree");
formData.append("date_time", "2023-10-21 17:30");
formData.append("website_code", "Pete123");

// 准备创建事件的请求选项
const postCommunityEventMethod = 'POST';

const requestOptions = {
    method: postCommunityEventMethod,
    body: formData,
    redirect: 'follow'
};

// 创建事件的函数
async function createEvent() {
  try {
    // 发送 POST 请求创建事件
    const response = await fetch(baseURL, requestOptions);
    
    // 检查响应状态码
    if (response.status === 201) {
      const data = await response.json();
      console.log("创建的新事件：");
      console.log(data);
    } else {
      // 处理错误响应
      const errorData = await response.json();
      console.error("创建事件时发生错误：");
      console.error(errorData);
    }
  } catch (error) {
    console.error("发生网络错误：", error);
  }
}

// 调用创建事件的函数
createEvent();

// 准备获取事件信息的请求选项
const getEventsMethod = 'GET';

const queryParams = {
    website_code: 'Pete123'
};

const queryString = new URLSearchParams(queryParams).toString();
const urlWithParams = baseURL + "?" + queryString;

const getOptions = {
  method: getEventsMethod,
  redirect: 'follow'
};

// 获取事件信息的函数
async function getEvents() {
  try {
    // 发送 GET 请求获取事件信息
    const response = await fetch(urlWithParams, getOptions);
    
    // 检查响应状态码
    if (response.status === 200) {
      const data = await response.json();
      console.log("获取的事件信息：");
      console.log(data);
    } else {
      // 处理错误响应
      const errorData = await response.json();
      console.error("获取事件信息时发生错误：");
      console.error(errorData);
    }
  } catch (error) {
    console.error("发生网络错误：", error);
  }
}

// 调用获取事件信息的函数
getEvents();
