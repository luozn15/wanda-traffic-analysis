# Wanda 客流小程序
<img src="https://cloud.tsinghua.edu.cn/seafhttp/files/9ce86efe-c1b2-4971-8646-77cb063f8a8a/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190917213606.png" width = "500"></img>

本程序使用 *python3.7* 开发，使用
[pyinstaller](http://www.pyinstaller.org/) 
打包为可执行文件格式，双击运行

### 功能
计算商场在时段内的技术指标，绘制商铺的热力图
### 输入
- **客流数据.xlsx**，格式如 [模板.xlsx](https://cloud.tsinghua.edu.cn/f/7572aba4f61c4db9b52f/?dl=1) ， **必须** 含四个表单（sheet）：<p>      ---出入口及通道日客流数</p><p>      ---店铺日客流量</p><p>      ---出入口及通道日客流量</p><p>      ---分时段客流数</p>   
![sheets](https://cloud.tsinghua.edu.cn/seafhttp/files/0198d292-356f-434d-8bc2-d9554d231f48/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190917215828.png)
- **商场平面.dxf**，DXF文件由原DWG文件通过AutoCAD导出，原DWG文件参考 [模板.dwg](https://cloud.tsinghua.edu.cn/f/2b761eb824ae4dcf8b33/) ，版本不限，原始DWG文件 **必须** 包含两个清理过的独立图层：<p>      ---ID，包含店铺序号的文本，位置靠近在店铺轮廓中心</p><p>      ---Bounds，包含店铺轮廓，全为Polyline，弧线也用polyline拟合</p>  
![layouts](https://cloud.tsinghua.edu.cn/seafhttp/files/d322a506-7e3b-446e-8c9c-504e6def84e4/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190917220050.png)  
![layouts](https://cloud.tsinghua.edu.cn/seafhttp/files/96bfd789-daa0-4f55-836d-86e7924af156/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190917220137.png)  
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

> [操作视频](https://cloud.tsinghua.edu.cn/f/d29a1d41dcec4eeb9990/) [![操作视频](https://cloud.tsinghua.edu.cn/seafhttp/files/9ce86efe-c1b2-4971-8646-77cb063f8a8a/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190917213606.png)](https://cloud.tsinghua.edu.cn/f/d29a1d41dcec4eeb9990/)
### 下载
下载地址  
- Windows： [客流小程序](https://cloud.tsinghua.edu.cn/f/f4a83e589178415caa67/)，最后更新： 2019-09-17

- MacOS： [客流小程序](https://cloud.tsinghua.edu.cn/f/47ba1d3c4cf7408ea564/)，最后更新： 2019-09-19

### 依赖
执行源码时，Anaconda环境下额外依赖python库 *dxfgrabber*, *pyqt5*
```bash
pip install dxfgrabber
pip install pyqt5
```

### 开发者
@luozn15 罗子牛  
@datatraveler-01 熊鑫昌

<img src="/windows/logo-01.png" width = "50" height = "50" div align=right></img>
