# Cultural Heritage Models (and others)

There is a sense with AI models announcements that it';s quite like markettinh toothpaste or razors, each time
there are some numbers and new desirable features with very maerkatable names, but what any of it means and how
you can compare one with another is a huge challenge. Some of this is just inherent in the complexity of what
is being described and needs to be unpacked as best of possible, which we try to break down below. And some of it
is just marketing, so good luck to you in makign sense of that!

The key points to look for are:

  * The organisation releasing the model (for ethical and licencing reasons)
  * The purpose of the model - i.e. is intented to turn text input into an image (text-to-image), to take queries and return text results (dialogue), to take an image and generate similiar images (image-to-image), and so on. 
  * The parameters of the model - crudely, the number of neurons (see more here - https://web.dev/articles/llm-sizes). Broadly, the bigger the better, but the downside of this increasing is the amount of memory/processing/storage resource needed to run it. The numbers tend to be indicative of size rather than exact counts, for example 2B models have about 2 billion parameters, about half the size of 4B models (obviously). Models are grouped into class sizes of: unknown size, ~1.5, ~3, ~7, 13, 35, 60, 70+ B parameters for comparision purposes. 
  * The training data size - The more data the model was trained on the better (but see below). This number often doesn't get quantified as precisely as the parameters as properitary models tend to keep it secret what they were trained on.
  * The training data duration (steps) - The longer the training the better ? Upto a point anyway. Quantified as steps. 
  * The training data quality - Becoming a more noted point (especially for reasons of copyright and diversity), how diverse/copyright free/high quality is the data it was trained on.
  * token count ?
  * Multi-lingual - Was the model trained on multi-lingual text (and images ?) and can it output multi-lingual results.
  * Release date - Fairly obviously,tThe model will not have been trained on any data from after this date which means questions on events after this will be answered differently from events prior.
  * Usage - How can the model be run, directly (e.g. llamafile), programatically (e.g. Python), via an API, etc. Depending on the problem you want to apply it to, a smaller model that is easier to get running may be a wiser choice than the huge models that need expensive computer resources.

Then there are some other architecture features that may be mentioned:

  * supervised fine-tuning
  * re-inforcement learning
  * context length/context window - the length of text (tokens) a model can hold in its memory at any time (see https://www.ibm.com/think/topics/context-window)


So for example if we look at a model on Hugging Face and break down the name:

  'meta-llama/Meta-Llama-3-8B'

  It's from Meta and it's a LLama model (version 3) which is a large-language model, this one has 8 billion (ish) parameters. All fairly obvious stuff.

Features that come up fairly often (and are specific to some particular challenges, e.g. text understanding or image
understanding)


Their are an overwheleming number of announcements about AI models each which some new feature or number seemingly
all important but u

## Model Setup

  * Layer Architecture
  * Training Data
  * Training Process
  * Refinement (new training data)

## Models trained from cultural heritage datasets.

## Transfer Learning

Models trained on another domain first and then fine-tuned for cultural heritage

| Name | Date| Paramaters | Description | Original Model | Notes | Link |

## Other models

There are thousands of different models of different sizes that have been created in recent years, and this is not an attempt to list them all (try https://huggingface.co/models for that). The ones below are probably the most commonly used:

### Large Language Models (LLM)

  * GPT
  * Llama
  * BERT
  * Claude Sonnet
  * Mistral
  * Gemini

### Text to Image 

   * Stable Diffusion
   * Dall-E
   * MidJourney
   * AlexNet
   * Inceptionv3

### Image to Text

  * LeNet-5
  * AlexNet
  * GoogLeNet
  * VGGNet
  * ResNet

### Vision Language Models (VLM)

  * Grok

## Transfer Learning

## Cultural Heritage Only

No large scale models exist at present, only smaller scale. 
