# BootStrap

### 1.下载

https://v3.bootcss.com/

### 2.引入

```html
<!--    开发版本-->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <!--    生产版本-->
<!--    <link rel="stylesheet" href="/static/plugins/bootstrap-3.4.1/css/bootstrap-theme.min.css">-->
```

### 3.复制组件代码并修改

### 4.栅格系统

## 栅格参数

通过下表可以详细查看 Bootstrap 的栅格系统是如何在多种屏幕设备上工作的。


|                       | 超小屏幕 手机 (<768px)     | 小屏幕 平板 (≥768px)                               | 中等屏幕 桌面显示器 (≥992px) | 大屏幕 大桌面显示器 (≥1200px) |
| --------------------- | -------------------------- | --------------------------------------------------- | ----------------------------- | ------------------------------ |
| 栅格系统行为          | 总是水平排列               | 开始是堆叠在一起的，当大于这些阈值时将变为水平排列C |                               |                                |
| `.container` 最大宽度 | None （自动）              | 750px                                               | 970px                         | 1170px                         |
| 类前缀                | `.col-xs-`                 | `.col-sm-`                                          | `.col-md-`                    | `.col-lg-`                     |
| 列（column）数        | 12                         |                                                     |                               |                                |
| 最大列（column）宽    | 自动                       | \~62px                                              | \~81px                        | \~97px                         |
| 槽（gutter）宽        | 30px （每列左右均有 15px） |                                                     |                               |                                |
| 可嵌套                | 是                         |                                                     |                               |                                |
| 偏移（Offsets）       | 是                         |                                                     |                               |                                |
| 列排序                | 是                         |                                                     |                               |                                |

分类：

* 响应式：

.col-lg- 1170px

.col-md- 970px

.col-sm- 750px

* 非响应式：

col-xs-

* 列偏移

```html
<div class="row">
  <div class="col-md-4">.col-md-4</div>
  <div class="col-md-4 col-md-offset-4">.col-md-4 .col-md-offset-4</div>
</div>
```

### 5.container

布局容器

Bootstrap 需要为页面内容和栅格系统包裹一个 `.container` 容器。我们提供了两个作此用处的类。注意，由于 `padding` 等属性的原因，这两种 容器类不能互相嵌套。

`.container` 类用于固定宽度并支持响应式布局的容器。

```html
<div class="container">
  ...
</div>
```

`.container-fluid` 类用于 100% 宽度，占据全部视口（viewport）的容器。

```html
<div class="container-fluid">
  ...
</div>
```

### 6.
