# mIHC Normalization Benchmark

 

This project presents a comparative study of normalization techniques for Multiplex Immunohistochemistry (mIHC) data. The objective is to evaluate how different normalization methods reduce batch effects, improve distribution consistency, and preserve biologically meaningful information in quantitative mIHC datasets.

 

## Evaluated Methods

- Z-score Normalization

- Mean Division (MeanDiv)

- ComBat

- MxNorm

- UniFORM

 

## Evaluation Metrics

- kBET Score
  
- Average χ² Statistic

- Average p-value

- Silhouette Score

- Peak Standard Deviation Improvement

- Wasserstein Distance Improvement

 
## Key Findings

- Z-score achieved the strongest statistical batch-effect correction.
  
- UniFORM demonstrated superior distribution alignment and sample integration.
  
- ComBat and MxNorm provided balanced performance across multiple criteria.
  
- No single method outperformed all others across every evaluation metric.
  
 
## Research Focus

This work highlights the challenges of normalization in chromogenic mIHC data and demonstrates that normalization should be treated as a multi-objective optimization problem where technical correction and biological preservation must be balanced.

 
## Authors

Imindu Dissanayaka
31
Centre for Machine Vision and Signal Analysis, University of Oulu, Finland
