README

This is bpopper3 (gtid) readme, go to https://github.com/brieucpopper/unsupLearning

The actual code is in the "code.ipynb" as a python notebook, and the code is commented if needed.

This has all the code to generate all the plots and results mentioned in the analysis.


You need a python conda env to run this


It is Python 3.9.18 with mostly sklearn and some libraries

Below is the environment.yml

name: MLenv
channels:
  - conda-forge
  - microsoft
  - defaults
dependencies:
  - appnope=0.1.3=pyhd8ed1ab_0
  - asttokens=2.4.0=pyhd8ed1ab_0
  - backcall=0.2.0=pyh9f0ad1d_0
  - backports=1.0=pyhd8ed1ab_3
  - backports.functools_lru_cache=1.6.5=pyhd8ed1ab_0
  - brotli=1.0.9=he49afe7_4
  - brotli-python=1.0.9=py39h7a8716b_9
  - ca-certificates=2023.7.22=h8857fd0_0
  - comm=0.1.4=pyhd8ed1ab_0
  - cycler=0.12.1=pyhd8ed1ab_0
  - debugpy=1.6.7=py39hcec6c5f_0
  - decorator=5.1.1=pyhd8ed1ab_0
  - exceptiongroup=1.1.3=pyhd8ed1ab_0
  - executing=1.2.0=pyhd8ed1ab_0
  - fonttools=4.44.0=py39ha09f3b3_0
  - freetype=2.10.4=h4cff582_1
  - giflib=5.2.1=hb7f2c08_3
  - idna=3.4=pyhd8ed1ab_0
  - importlib-metadata=6.8.0=pyha770c72_0
  - importlib_metadata=6.8.0=hd8ed1ab_0
  - ipykernel=6.25.2=pyh1050b4e_0
  - ipython=8.16.1=pyh31c8845_0
  - jedi=0.19.1=pyhd8ed1ab_0
  - joblib=1.3.2=pyhd8ed1ab_0
  - jpeg=9e=hb7f2c08_3
  - jupyter_client=8.4.0=pyhd8ed1ab_0
  - jupyter_core=5.4.0=py39h6e9494a_0
  - kiwisolver=1.4.4=py39hcec6c5f_0
  - lcms2=2.15=h29502cd_0
  - lerc=3.0=he9d5cce_0
  - libblas=3.9.0=19_osx64_openblas
  - libcblas=3.9.0=19_osx64_openblas
  - libcxx=14.0.6=h9765a3e_0
  - libdeflate=1.17=hb664fd8_1
  - libffi=3.4.4=hecd8cb5_0
  - libgfortran=5.0.0=13_2_0_h97931a8_1
  - libgfortran5=13.2.0=h2873a65_1
  - liblapack=3.9.0=19_osx64_openblas
  - libopenblas=0.3.24=openmp_h48a4ad5_0
  - libpng=1.6.39=h6c40b1e_0
  - libsodium=1.0.18=hbcb3906_1
  - libtiff=4.5.1=hcec6c5f_0
  - libwebp=1.3.2=hf6ce154_0
  - libwebp-base=1.3.2=h0dc2134_0
  - llvm-openmp=17.0.4=hb6ac08f_0
  - lz4-c=1.9.4=hf0c8a7f_0
  - matplotlib=3.5.3=py39h6e9494a_2
  - matplotlib-base=3.5.3=py39h03b9044_0
  - matplotlib-inline=0.1.6=pyhd8ed1ab_0
  - munkres=1.1.4=pyh9f0ad1d_0
  - ncurses=6.4=hcec6c5f_0
  - nest-asyncio=1.5.8=pyhd8ed1ab_0
  - numpy=1.23.5=py39hdfa1d0c_0
  - openssl=3.1.4=hd75f5a5_0
  - packaging=23.2=pyhd8ed1ab_0
  - pandas=1.5.3=py39hecff1ad_1
  - parso=0.8.3=pyhd8ed1ab_0
  - patsy=0.5.3=pyhd8ed1ab_0
  - pexpect=4.8.0=pyh1a96a4e_2
  - pickleshare=0.7.5=py_1003
  - pillow=9.4.0=py39hcec6c5f_1
  - pip=23.2.1=py39hecd8cb5_0
  - platformdirs=3.11.0=pyhd8ed1ab_0
  - pooch=1.8.0=pyhd8ed1ab_0
  - prompt-toolkit=3.0.39=pyha770c72_0
  - prompt_toolkit=3.0.39=hd8ed1ab_0
  - psutil=5.9.5=py39hdc70f33_1
  - ptyprocess=0.7.0=pyhd3deb0d_0
  - pure_eval=0.2.2=pyhd8ed1ab_0
  - pygments=2.16.1=pyhd8ed1ab_0
  - pyparsing=3.1.1=pyhd8ed1ab_0
  - pysocks=1.7.1=pyha2e5f31_6
  - python=3.9.18=h5ee71fb_0
  - python-dateutil=2.8.2=pyhd8ed1ab_0
  - python_abi=3.9=2_cp39
  - pytz=2023.3.post1=pyhd8ed1ab_0
  - pyzmq=24.0.1=py39hed8f129_1
  - readline=8.2=hca72f7f_0
  - requests=2.31.0=pyhd8ed1ab_0
  - scikit-learn=1.2.2=py39h151e6e4_1
  - scipy=1.10.1=py39h4c5e66d_2
  - seaborn=0.13.0=hd8ed1ab_0
  - seaborn-base=0.13.0=pyhd8ed1ab_0
  - setuptools=68.0.0=py39hecd8cb5_0
  - six=1.16.0=pyh6c4a22f_0
  - sqlite=3.41.2=h6c40b1e_0
  - stack_data=0.6.2=pyhd8ed1ab_0
  - statsmodels=0.14.0=py39h5b4affa_2
  - threadpoolctl=3.2.0=pyha21a80b_0
  - tk=8.6.12=h5d9f67b_0
  - tornado=6.3.3=py39hdc70f33_1
  - traitlets=5.11.2=pyhd8ed1ab_0
  - typing-extensions=4.8.0=hd8ed1ab_0
  - typing_extensions=4.8.0=pyha770c72_0
  - tzdata=2023c=h04d1e81_0
  - unicodedata2=15.1.0=py39hdc70f33_0
  - urllib3=2.0.7=pyhd8ed1ab_0
  - wcwidth=0.2.8=pyhd8ed1ab_0
  - wheel=0.38.4=py39hecd8cb5_0
  - xz=5.4.2=h6c40b1e_0
  - zeromq=4.3.4=h23ab428_0
  - zipp=3.17.0=pyhd8ed1ab_0
  - zlib=1.2.13=h4dc903c_0
  - zstd=1.5.5=hc035e20_0
  - pip:
      - beautifulsoup4==4.12.2
      - certifi==2023.7.22
      - charset-normalizer==3.3.1
      - soupsieve==2.5
prefix: /Users/brieucpopper/miniconda3/envs/MLenv
