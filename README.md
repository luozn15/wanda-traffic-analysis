# Wanda 客流小程序
<img src="https://cloud.tsinghua.edu.cn/thumbnail/599aea4603294fbd8a8d/1024/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190917214752.png" width = "500"></img>

本程序使用 *python3.7* 开发，使用
[pyinstaller](http://www.pyinstaller.org/) 
打包为可执行文件格式，双击运行

### 功能
计算商场在时段内的技术指标，绘制商铺的热力图
### 输入
- **客流数据.xlsx**，格式如 [模板.xlsx](https://cloud.tsinghua.edu.cn/f/9daafe4d12b34b12b162/?dl=1) ， **必须** 含四个sheet：<p>      ---出入口及通道日客流数</p><p>      ---店铺日客流量</p><p>      ---出入口及通道日客流量</p><p>      ---分时段客流数</p>   
![sheets](https://cloud.tsinghua.edu.cn/thumbnail/09eb18afa0a340bf9e92/1024/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190917215828.png)
- **商场平面.dxf**，DXF文件由原DWG文件通过AutoCAD导出，原DWG文件参考 [模板.dwg](https://cloud.tsinghua.edu.cn/f/abcf3f7e56a9415197de/?dl=1) ，版本不限，原始DWG文件 **必须** 包含两个清理过的独立图层：<p>      ---ID，包含店铺序号的文本，位置靠近在店铺轮廓中心</p><p>      ---Bounds，包含店铺轮廓，全为Polyline，弧线也用polyline拟合</p>  
![layouts](https://cloud.tsinghua.edu.cn/thumbnail/5f6f44fbe6954add9476/1024/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190917220137.png)  
![layouts](https://cloud.tsinghua.edu.cn/thumbnail/4bcdf69b2c05461aa0ac/1024/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190917220050.png)  
- 部分需要输入的指标，包括：<p>---商场总建筑面积</p><p>---停车位数</p><p>---各主力店面积</p>  

### 输出
- *inds.csv* 文件，包含各种计算获得的技术指标
- *heat_xxxx-xx-xx_xxxx-xx-xx.jpg* 文件，所选时段内的商铺热力图
### 使用流程
1. **双击** 客流小程序.exe
2. **选择** 客流数据.xlsx，确认
3. **选择** 商场平面图.dxf，确认
4. 检查空值，每个日期与时段下的空值个数，确认无误，**继续**
5. **点选** 计算的开始日期（如要计算 2018-12-01 至 2018-12-15 的时间段，则选择 2018-12-01），继续
6. **点选** 计算的结束日期（如要计算 2018-12-01 至 2018-12-15 的时间段，则选择 2018-12-15），继续
7. 依表头 **输入** 需要的数据
8. **选择** 计算完成的指标的保存位置
9. 指标计算完成自动打开csv文件
10. 店铺热力图绘制完成自动打开jpg文件

> [操作视频](https://cloud.tsinghua.edu.cn/f/922207dd0dae49a794e7/) [![操作视频](https://cloud.tsinghua.edu.cn/thumbnail/f248cd9cce554a758c8f/1024/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190917213606.png)](https://cloud.tsinghua.edu.cn/f/922207dd0dae49a794e7/)
### 下载
下载地址  
- Windows版 [客流小程序](https://cloud.tsinghua.edu.cn/f/6e546f9db46440fb9986/?dl=1)，最后更新： 2019-09-17

- Macintosh版 [客流小程序](https://cloud.tsinghua.edu.cn/f/adfddf0ce35a41c1a2a0/?dl=1)，最后更新： 调试中，即将上线

### 依赖
执行源码时，依赖python库 *dxfgrabber*, *pyqt5*
```bash
pip install dxfgrabber
pip install pyqt5
```

### 开发者
@luozn15 罗子牛  
@datatraveler-01 熊鑫昌

<img src="/logo-01.png" width = "50" height = "50" div align=right></img>
