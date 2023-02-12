Most of the code was taken from https://data-flair.training/blogs/python-based-project-image-caption-generator-cnn/
I changed some as my needs

# Table of Contents
* [Project Overview](#project-overview)
* [Project Demo](#project-demo)
* [Pre-requisites](#pre-requisites)
* [Project Structure](#project-structure)
* [Future Enhancements](#future-enhancements)
* [Installation](#installation)
* [Contact](#contact)


# Project Overview
This project is to practice computer vision, natual langauge processing to recognize the context of an image and describe them. In addition deploying it using streamlit.


# Project Demo


https://user-images.githubusercontent.com/77201365/195993136-0d37b272-8bf8-4c83-9a53-986fcd32d42a.mp4


![res2](https://user-images.githubusercontent.com/77201365/195993487-1f91bb80-abe1-4e23-876e-d511242c149f.png)


# Pre-requisites
Good knowledge of deep learning, keras, tensorflow, jupyter notebooks, and natural language processing.


# Project Structure

- data/
    - processed/
    - raw/
        - Flicker8k_Dataset
        - Flicker8k_Text

- models/
    - model_17.h5

- main.ipynb

- app.py

- generate_caption.py


# Installation

## First Option: use the GPU on anaconda

1. open your anaconda prompt

2. conda create --name tf_gpu_env

3. conda activate tf_gpu_env

4. conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0

5. conda install ipykernel

6. pip install tensorflow-gpu

7. pip install Pillow

8. conda install -c conda-forge ipywidgets

9. jupyter nbextension enable --py widgetsnbextension

10. pip install pandas


## Second Option: without anaconda

1. open your command line (cmd)

2. python -3 -m venv my-env

3. my-env\Scripts\activate

4. pip install -r requirements.txt


## Third Option: 

You can use your cpu, just install tensorflow and other libraries




# Future Enhancements
- [ ] Try Different Models and Pre-trained Models.
- [ ] Improve the Accuracy of the Captions.

# Contact

Ahmad Hammad [linked-in](https://www.linkedin.com/in/ahmad-hammad-057369203/)

