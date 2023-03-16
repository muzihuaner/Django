# JavaScript

DOM和BOM

js内置模块

jquery

第三方模块

### 1.变量

```javascript
var 变量名称
```

### 2.字符串类型

常见功能

```javascript
var name="你好，世界"
var v1=name.length;
var v2=name[0];//name.charAt(n)
var v3=name.trim();
var v4=name.substring(1,2) //前取后不取
```

### 3.函数

```javascript
function show() {
const tag = document.getElementById("txt");
const text = tag.innerHTML;
// console.log(text)
let firstChar = text[0];
let otherString = text.substring(1, text.length);
let newText = otherString + firstChar;
tag.innerHTML = newText;
}
```

### 4.数组

```javascript
//定义
var v1=[11,22,33,44,55]
var v2=Array([11,22,33,44])
```

```javascript
//操作
var v1=[11,22,33,44,55]
v1[0]
v1[0]="小欢"

v1.push("66") //尾部追加 [11,22,33,44,55,66]
v1.unshift("00")//添加到头部[00,11,22,33,44,55]
v1.splice(索引,0,元素）//splice() 方法用于添加或删除数组中的元素。
v1.splice(1,0,"中国")[11,"中国",22,33,44,55]

v1.pop() //尾部删除
v1.shift()//shift() 方法用于把数组的第一个元素从其中删除，并返回第一个元素的值。
```

```javascript
var v1=[11,22,33,44,55]
for(var item in v1){
//idx=0,1,2,3 data=v1[idx]
}

for(var i=0;i<v1.length;i++){

}
```

注意：break和continue

#### 案例：动态添加内容

```html
<ul id="city">

</ul>
<script !src="">
    let cityList = ["北京", "上海", "广州", "重庆"]
    for (let city in cityList) {
        let cityname = cityList[city]
        //将文本添加
        const tag = document.createElement("li");
        tag.innerHTML = cityname
        //添加到ul里
        const list = document.getElementById("city");
        list.appendChild(tag)

    }

</script>
```

### 5.对象（字典）

```javascript
info={
        name:"小A",
        age:18,
        sex:"man",
    }
    console.log("我是"+info.name+"，"+info.age+"我是"+info.sex)
    info.name="Man"
  
    delete info["age"]
    for(let key in info){
        //key=name/age data=info[name]
    }
```

