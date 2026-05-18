Aus Solar Generation Forecasting

This repository implements an end-to-end pipeline for postcode-based solar generation forecasting in Australia. It includes data collection from NASA POWER, creation of postcode→reference mappings, weather scenario simulation, physical PV production calculations, and benchmarking of multiple time-series forecasting models.

**Project overview**
- End-to-end flow: postcode → lat/long → NASA POWER → preprocessing → simulation/training → 365-day forecasts.
- Data: the `data/` folder contains postcode and reference files (e.g. `postcodes/`, `volta_solar_reference_points.csv`, `postcode_to_ref_mapping.csv`, `postcode_to_solar_ref_lookup.csv`).
- Results: the `benchmark_results/` folder stores model outputs and evaluation files.

**Main notebooks (short summary)**
- [aus-solar-generation-forecasting.ipynb](aus-solar-generation-forecasting.ipynb): postcode normalization, clustering to create solar reference points, NASA data download and merge, feature engineering, and dataset preparation for HF.
- [solar_generation_simulation_pipeline.ipynb](solar_generation_simulation_pipeline.ipynb): `SolarGenerationSimulationPipeline` class — fetch hourly NASA POWER, simulate weather scenarios using 24h block sampling, compute hourly solar production and aggregate probabilistic forecasts (q0.1/q0.5/q0.9).
- [simulation_reorganized.ipynb](simulation_reorganized.ipynb): simulation benchmark and backtests across multiple years; physics sensitivity (soiling, degradation) analysis.
- [Step_6_benchmark_3_models.ipynb](Step_6_benchmark_3_models.ipynb): consolidate benchmark metrics from Chronos, TimesFM and Moirai; decision matrix for model selection.
- [Step_7_finetune_chronos.ipynb](Step_7_finetune_chronos.ipynb): fine-tune Chronos (AutoGluon TimeSeries) with known covariates, evaluate, and upload fine-tuned model to Hugging Face.
- [Step_8_ Full Forecasting Pipeline Implementation.ipynb](Step_8_%20%20Full%20Forecasting%20Pipeline%20Implementation.ipynb): `SolarForecastingPipeline` class — production-ready end-to-end pipeline for running forecasts given a postcode (fetch NASA, build covariates, call predictor, visualize results).
- [amazon_chronos-2.ipynb](amazon_chronos-2.ipynb): benchmark using `amazon/chronos-2` model (zero-shot and with covariates).
- [google_timesfm-2.5-200m-pytorch.ipynb](google_timesfm-2.5-200m-pytorch.ipynb): benchmark TimesFM 2.5 (PyTorch).
- [Salesforce_moirai-2.0-R-small.ipynb](Salesforce_moirai-2.0-R-small.ipynb): benchmark Moirai-2.0 R-small.

**Quick start**
1. Prepare data in Google Drive as used by the notebooks (e.g. `/content/drive/MyDrive/TT/data/`).
2. Recommended notebook order: `aus-solar-generation-forecasting.ipynb` → (create datasets) → `Step_7_finetune_chronos.ipynb` (optional fine-tuning) → `Step_6_benchmark_3_models.ipynb` (run benchmarks) → `Step_8_ Full Forecasting Pipeline Implementation.ipynb` (run end-to-end pipeline).
3. Install required libraries (each notebook contains `!pip install ...` cells). Typical packages: `transformers`, `datasets`, `gluonts`, `chronos-forecasting`, `autogluon.timeseries`, `timesfm`, `pandas`, `requests`.

**Notes / caveats**
- Notebooks are developed for Google Colab and use Google Drive paths. Update `lookup_path` / `result_folder_path` when running locally.
- When downloading many NASA POWER files, respect API rate limits and cache JSON responses to avoid repeated requests.

**Datasets & Fine-tuned Model**
- Dataset (processed daily dataset used for training): https://huggingface.co/datasets/codenhenhe/volta-solar-daily-v1
- Fine-tuned Chronos-2 model (uploaded to Hugging Face): https://huggingface.co/codenhenhe/chronos2-volta-solar-daily


