# Deploying Inference Services on Backend.ai (GUI Tutorial)

This tutorial provides a step-by-step guide on how to deploy and serve machine learning models for inference using the Backend.ai GUI. We will cover two common use cases:
1.  **Deploying a standard web application using FastAPI.**
2.  **Deploying a large language model (LLM) using the vLLM engine.**

This guide assumes you do not need to use a Dockerfile, as Backend.ai can manage the environment directly.

---

##  Prerequisites

Before you begin, ensure you have the following:
* A Backend.ai account with access to the GUI.
* Your application code and model files are ready and accessible (e.g., uploaded to the Backend.ai storage).
* Familiarity with the basic concepts of model serving and APIs.

---

## Part 1: Deploying a FastAPI Application (`demo-fastapi`)

This section will guide you through deploying a simple FastAPI application.

### Step 1: Create a New Service

1.  Navigate to the **Serving** tab in the Backend.ai GUI.
2.  Click on the **"Start Service"** button.

### Step 2: Configure the Service

1.  **Service Name**: Give your service a descriptive name, such as `demo-fastapi`.
2.  **Model Storage To Mount**: Select a model storage to mount.
3.  **Inference Runtime Variant**: Set inference runtime to `Custom`.
4.  **Environments / Version**: Select environment image. For FastAPI, a general Python 3.12+ image (e.g., `bai-repo:7080/bai/ngc-pytorch:25.01-pytorch2.6-py312-cuda12.8@x86_64`).
3.  **Resources**: Allocate the necessary CPU (`2 core`), Memory (`4 GB`), and GPU (`0 FGPU`) resources for your application. For a simple FastAPI demo, minimal resources are often enough.

### Step 3: Launch and Test

1.  Review your configuration and click **"Create"**.
2.  Backend.ai will provision the resources and start your service. Once the status is "HEALTHY", you can access the service endpoint provided in the GUI.
3.  Click on the endpoint URL to interact with your FastAPI application.

---

## Part 2: Deploying LLMs with vLLM

This section covers deploying large language models like `demo-gpt-oss` and `demo-gemma3-1b` using the high-performance vLLM engine. The process is similar to the FastAPI example but requires a GPU and a different start command.

### Step 1: Create and Configure the Service

1.  Follow **Step 1** from Part 1 to create a new service.
2.  **Service Name**: `demo-gpt-oss` or `demo-gemma3-1b`.
3.  **Model Storage To Mount**: Select a model storage to mount.
4.  **Inference Runtime Variant**: Set inference runtime to `Custom`.
5.  **Environments / Version**: Select a vllm 0.6.2 environment image. (e.g., `bai-repo:7080/bai/vllm:0.6.2-cuda12.1-ubuntu22.04@x86_64`).
4.  **Resources**: **Crucially, you must allocate a GPU.** The amount of GPU memory depends on the size of the model you are deploying.

### Step 2: Launch and Test the LLM Service

1.  Review your configuration and click **"Create"**.
2.  Backend.ai will provision the resources and start your service. Once the status is "HEALTHY", you can access the service endpoint provided in the GUI.
3.  This endpoint is an OpenAI-compatible API. You can interact with it using tools like `curl`, Python's `requests` library, or any OpenAI client library by pointing them to this new base URL.

**Example `curl` request:**
```bash
curl http://<your-backend.ai-endpoint-url>/v1/completions \
-H "Content-Type: application/json" \
-d '{
    "model": "<your-model-name>",
    "prompt": "Hello, my name is"
}'
```