### 测序数据回帖基因组
#### 分析介绍

原始数据质控之后， 使用序列比对软件[BWA](http://bio-bwa.sourceforge.net/bwa.shtml)， 对有效的测序读段进行参考基因组比对。并进行比对结果统计。使用长读段比对模式，BWA-MEM得到BAM格式的最初比对结果。通过[Picard-Sortbam](https://broadinstitute.github.io/picard/)工具对比结果进行染色体位置排序，再用[Picard-Markduplicate](https://broadinstitute.github.io/picard/)工具去除重复读段。所得结果可以在多个层面上进行质量评估。

### 分析结果
#### mapping rate统计

有效的测序reads用基因组序列回贴软件bwa回贴回参考基因组，bwa使用长reads比对模式BWA-MEM得到BAM格式的最初比对结果，BAM文件用Picard-Sortbam工具对比对后结果进行染色体位置排序，再用Picard-Mark duplicate工具对重复的reads进行去除，最后使用排序后的BAM文件及去重后的BAM文件进行统计。通过对排序后的BAM文件及去重后的BAM文件进行统计，得出以下统计数据(详见附件：2.mapping——readsMappingReateStat.xlsx)：

**reads回贴参考基因组的回贴比率统计**

{{ add_xls(mappingRateStat) }}

>说明：
<br>Sample：样本名称
<br>Total mapping rate: 回帖到参考基因组的reads所占的比率
<br>Proper rate：reads1和reads2间距合适的reads所占的比率 
<br>Deduplicated rate：reads的去重率 
<br>Targeted rate：靶向率

#### 靶向效果评估

#### coverage基本信息

对于所有mapping到基因组上的reads统计不同靶向区域的平均覆盖度(详见附件：2.mapping——AllFile.mean.coverage.xlsx)。

{{ add_xls(targetRegionCovStat) }}

>说明：
<br>Sample：样本名称 
<br>Target region mean coverage：靶向区域平均reads覆盖度
<br>Std：标准差

#### Coverage by nX（多少乘）

对mapping后的reads进行覆盖度含量统计，统计结果如下图所示，图中横轴为覆盖数，纵轴为靶向区域碱基覆盖度百分比(详见附件：2.mapping——nX)。

{{ add_pngs(nXimages) }}
