# Use an image with Miniconda installed
FROM continuumio/miniconda3

# Copy the environment.yml file from the .devcontainer directory to a temporary location in the container
COPY environment.yml /tmp/environment.yml

# Create the Conda environment using the copied file
RUN conda env create -f /tmp/environment.yml

# Set the newly created Conda environment as the default environment
ENV CONDA_DEFAULT_ENV=base

# Ensure that the Conda environment is activated whenever a shell is launched
RUN echo "conda activate base" > ~/.bashrc
ENV PATH /opt/conda/envs/base/bin:$PATH
