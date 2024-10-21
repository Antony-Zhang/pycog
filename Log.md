- **环境配置**
  - 设置py2.7环境，在终端中`cd`到项目根目录来安装依赖：`pip install numpy matplotlib theano=0.7`
    > Cpython单纯没安装成
  - 下载安装[mingw64](https://github.com/niXman/mingw-builds-binaries?tab=readme-ov-file)，并配置环境变量；下载安装[TeX Live](https://www.tug.org/texlive/windows.html#install)
- 逐步进行的分析
  - **模型训练**: 执行`cd examples`进入子目录，执行`python do.py models/romo train`，产生的文件保存在'examples\work\data'目录下
  - **模型State**: 执行`python do.py models/romo restingstate`，'examples\work\figs\romo\romo_restingstate.pdf'，并输出：
    ```
    => settings
      | dt:        0.5 ms
      | threshold: 0.0001
    Mean output: 0.189853
    Std. output: 0.056860
    ```
  - **训练曲线**: 执行`python do.py models/romo costs`，'examples\work\figs\romo\romo_costs.pdf'
  - **模型结构**: 执行`python do.py models/romo structure selectivity`， 'examples\work\figs\romo\romo_structure.pdf'
  - **测试**: 执行`python do.py models/romo run analysis/romo trials 100`生成1000个trial测试数据，并保存到'~\scratch\work\examples\romo\trials\romo_trials.pkl'中
  - 其他分析
    ```bash
    python do.py models/romo run analysis/romo psychometric # 在生成trials时会自动进行，计算平均accuracy并存于'examples\work\figs\romo\romo_psychometric.pdf'
    python do.py models/romo run analysis/romo sort   # 排序 ~\scratch\work\examples\romo\trials\romo_sorted.pkl
    python do.py models/romo run analysis/romo units  # examples\work\figs\romo\romo_unitxxx.pdf 
    ```
- 一次性复现论文图片: 进入`paper`子目录，执行`python all.py romo`,其中会包括模型训练、sort、units操作，最后执行`python fig_romo.py`来分析绘制，存于'paper\figs\fig_romo.pdf'
  > 在进行完前面的逐步分析后，也可直接执行`python fig_romo.py`，但需要在文件内额外设置'romo'的路径，否则报错找不到


  