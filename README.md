# mIHC Normalization Benchmark
2
 
3
This project presents a comparative study of normalization techniques for Multiplex Immunohistochemistry (mIHC) data. The objective is to evaluate how different normalization methods reduce batch effects, improve distribution consistency, and preserve biologically meaningful information in quantitative mIHC datasets.
4
 
5
## Evaluated Methods
6
- Z-score Normalization
7
- Mean Division (MeanDiv)
8
- ComBat
9
- MxNorm
10
- UniFORM
11
 
12
## Evaluation Metrics
13
- kBET Score
14
- Average χ² Statistic
15
- Average p-value
16
- Silhouette Score
17
- Peak Standard Deviation Improvement
18
- Wasserstein Distance Improvement
19
 
20
## Key Findings
21
- Z-score achieved the strongest statistical batch-effect correction.
22
- UniFORM demonstrated superior distribution alignment and sample integration.
23
- ComBat and MxNorm provided balanced performance across multiple criteria.
24
- No single method outperformed all others across every evaluation metric.
25
 
26
## Research Focus
27
This work highlights the challenges of normalization in chromogenic mIHC data and demonstrates that normalization should be treated as a multi-objective optimization problem where technical correction and biological preservation must be balanced.
28
 
29
## Authors
30
Imindu Dissanayaka
31
Centre for Machine Vision and Signal Analysis, University of Oulu, Finland
