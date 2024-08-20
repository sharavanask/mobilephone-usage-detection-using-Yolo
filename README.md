# Mobile Phone Usage Detection System

This project aims to detect mobile phone usage using a deep learning model trained with the YOLOv8 architecture. The model has been trained on a custom dataset for 3 epochs and the best model weights are stored as `best.pt`.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)

## Introduction

Mobile phone usage detection is an essential task in various scenarios, such as monitoring driver behavior or ensuring productivity in work environments. This project uses a YOLOv8-based model to detect mobile phone usage in images and video streams.

## Dataset

The dataset used for training includes images labeled for the presence or absence of mobile phone usage. The dataset was structured as follows:

├── train
│ ├── images
│ └── labels
├── valid
│ ├── images
│ └── labels
├── test
│ ├── images
│ └── labels
└── export
the dataset can be annotated individuallly using robustflow or you can use public dataset present in the robustflow 


## Model

The model is based on the YOLOv8 architecture, a state-of-the-art object detection model known for its speed and accuracy. The model was trained for 3 epochs, and the best-performing weights were saved as `best.pt`.

## Installation

### Prerequisites

- Python 3.8 or later
- PyTorch
- Ultralytics YOLOv8
- OpenCV
- Other dependencies listed in `requirements.txt`

### Steps

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mobile-phone-usage-detection.git
cd mobile-phone-usage-detection
