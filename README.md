# Image Restoration using Matrix Completion Techniques

## Description of the Project
This project focuses on restoring corrupted images represented as matrices with missing pixel values. I will explore various matrix completion techniques such as mean / median / mode imputation, Singular Value Decomposition (SVD), and more advanced methods such as total variation image in-painting. The goal is to fill the missing pixels and evaluate which method yields the best restoration based on both visual quality and quantitative metrics like Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM).

## Clear Goals
- Successfully restore corrupted images by filling missing pixel values using various matrix completion techniques.
- Compare the effectiveness of basic statistical methods (mean, median, mode), matrix factorization, and autoencoders.
- Measure performance based on visual inspection and quantitative metrics (e.g., PSNR, SSIM).

## Data Collection
I will be using the publicly available image dataset CIFAR-10 for image collection. To simulate corrupted images, we will randomly remove pixel values, replacing them with placeholders (e.g., `NaN' or (0,0,0)). These datasets will serve as our training and testing ground for the various matrix completion techniques.

For all collected images from CIFAR-10, we will ensure that the images are the same resolution and size. 

## How We Plan on Modeling the Data
We will model the data using the following techniques:

1. **Mean, Median, Mode Imputation**: Use simple statistical methods to fill missing pixels based on neighboring pixel values.
2. **Singular Value Decomposition (SVD)**: Initialize unknown pixel values randomly. Alternate betwween using SVD to construct a low rank approximation of the image and filling in known pixel values afterwards. We repeat until convergence or a prespecified maximum number of iterations. 
3. **Total variation image in-painting**: Generates an image with the observed entries intact while filling the missing pixel values such that we have minimal total variation. Since the total variation objective is a convex functional, we can use standard interior-point methods from convex programming software to solve the problem. 

## Data Visualization
We plan to visualize the results through:
- **Side-by-Side Image Comparisons**: Display the original, corrupted, and restored images for each matrix completion method.
- **Quantitative Metric Plots**: Plot PSNR and SSIM scores to compare the performance of different methods.
- **Heatmaps**: Visualize the locations of missing pixels and their imputed values.
- **Interactive Visualizations**: Create interactive plots to allow the user to explore the impact of different matrix completion methods.

## Test Plan
We will divide the dataset into training and testing sets:
- **80% for Training**: This will be used to train models like matrix factorization and autoencoders.
- **20% for Testing**: This will serve as our evaluation set for the matrix completion methods. The corrupted version of this test set will not have the same corruption pattern as the training data to test generalization.
  
We will use cross-validation for parameter tuning, particularly for the matrix factorization (SVD) and total variation image in-painting models, to ensure they generalize well to unseen data.

## Timeline
### Week 1 (10/1 - 10/7)
- Submit the project proposal.
- Begin collecting datasets (CIFAR-10) and finalize the corruption process.

### Week 2 (10/8 - 10/14)
- Implement the data corruption process and prepare the dataset.
- Begin implementing basic matrix completion methods (mean, median, mode).

### Week 3 (10/15 - 10/21)
- Finalize the implementation of SVD matrix completion.
- Generate preliminary visualizations of corrupted and restored images.

### Week 4 (10/22 - 10/28)
- Implement total variation in-painting for matrix completion.
- Continue refining visualizations and collect initial results.

### Week 5 (10/29 - 11/4)
- Prepare for the midterm report and presentation.

### Midterm Report (Due 11/5)
- Submit README.md with preliminary visualizations, descriptions of data processing, modeling methods used so far, and preliminary results.
- Record and upload a 5-minute presentation summarizing the project progress.

### Week 6-7 (11/6 - 11/18)
- Further refine total variation in-painting model.
- Explore additional advanced techniques, if time permits.

### Week 8-9 (11/19 - 12/2)
- Test the models on the withheld test set.
- Finalize visualizations and prepare the final code repository.

### Week 10 (12/3 - 12/10)
- Finalize and submit the project report, including:
  - Instructions on how to build and run the code, using a `Makefile`.
  - Test code and a GitHub workflow for automating testing.
  - Final visualizations and results.

## Final Report (Due 12/10)
- Ensure that the `README.md` includes:
  - Instructions for building and running the project.
  - Testing code and automated workflow in the GitHub repo.
  - Detailed descriptions of the data processing and modeling steps.
  - Final visualizations and results demonstrating the success of the matrix completion methods.
