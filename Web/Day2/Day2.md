：after

在内容后面添加

例如

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .clearfix:after{
            content:"";
            display: block;
            clear: both;
        }
        .item{
            float: left;
        }
    </style>
</head>
<body>
<div class="clearfix">
    <div class="item">1</div>
    <div class="item">2</div>
    <div class="item">3</div>
</div>
</body>
</html>
```

固定定位fixed

对话框遮罩效果

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {
            margin: 0;
        }

        /*.clearfix:after{*/
        /*    content:"";*/
        /*    display: block;*/
        /*    clear: both;*/
        /*}*/
        /*.item{*/
        /*    float: left;*/
        /*}*/
        .dialog {
            position: fixed;
            left: 0;
            right: 0;
            top: 200px;
            margin: 0 auto;
            width: 250px;
            height: 150px;
            background-color: #ffffff;
            z-index: 1000;
        }

        .mask {
            background-color: #333333;
            opacity: 0.7;
            position: fixed;
            left: 0;
            right: 0;
            top: 0;
            bottom: 0;
            z-index: 999;
        }
    </style>
</head>
<body>
<!--<div class="clearfix">-->
<!--    <div class="item">1</div>-->
<!--    <div class="item">2</div>-->
<!--    <div class="item">3</div>-->
<!--</div>-->

<div style="height: 1000px">
<div>超文本标记语言（英语：HyperText Markup Language，简称：HTML）是一种用于创建网页的标准标记语言。

您可以使用 HTML 来建立自己的 WEB 站点，HTML 运行在浏览器上，由浏览器来解析。

在本教程中，您将学习如何使用 HTML 来创建站点。

HTML 很容易学习！相信您能很快学会它！</div>
    <div class="mask"></div>
    <div class="dialog"></div>
</div>
</body>
</html>
```

返回顶部

2.子绝父相

父布局 relative

子布局 absolute
