# CSS样式

1.Css应用方式

```html
<div style="color:red" >中国联通</div>
```


## 外部样式表

当样式需要应用于很多页面时，外部样式表将是理想的选择。在使用外部样式表的情况下，你可以通过改变一个文件来改变整个站点的外观。每个页面使用 `<link>` 标签链接到样式表。 `<link>` 标签在（文档的）头部：

```html
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
```

浏览器会从文件 mystyle.css 中读到样式声明，并根据它来格式文档。

##### 内容居中

区域居中

自己要有宽度+margin: 0 auto;

例如

```css
.container{
    margin: 0 auto;
    width: 1226px;
}
```

垂直方向居中

文本+line-height

图片+边距

##### 浮动

如果存在浮动，那么加入



```html
    <div style="clear: both"></div>
```
