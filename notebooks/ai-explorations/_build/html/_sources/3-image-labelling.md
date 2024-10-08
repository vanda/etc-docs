# 3. Image Labelling

Also known as: multi-label classification, image keywords, image labels.

Not to be confused with: multi-class classification (see https://scikit-learn.org/stable/modules/multiclass.html#multiclass-classification )

## Problem

### Problem Statement

"Generate a relevant set of labels to describe the digital image of a cultural heritage artwork."

### Background

A fairly obvious issue not specific to cultural heritage, to generate relevant text keywords describing the main features
of the image. For cultural heritage objects this would ideally describe the object and the contents of the object, it would
be near impossible for it to give any other information not obtainable from the image such as the provenance of the object or
the place of production. 

### Related Problems

The following problems and this one are all broadly the same, the generation of text based on the image, and it could just
be considered a variation of length of text output. But there are major differences in approach between them, especially with
LLM combined with 

  * 2-image-classification
  * 4-image-captioning
  * 5-image-description

There are some differences though (for example, 

## Solutions


### Sample Implementations

### Leading Implementations

### Implementation Tracking

## Major Variations

  * 3/A - Restrict classification to that within a particular context (materials, techniques, place, etc)
  * 3/B - Restrict classification known to those within a particular vocabulary (AAT, TGN, Iconclass)
  * 3/C - Combine 2M2 and 2M3

## Problem Variations

### Major Variations

### Minor Variations

  * 3/a - Output the labels in multiple languages

### Type Specific Variations

  * 3/1 - Paintings Specific keywords
    
## Linkages

  * Keywords can then be used as part of with image classification, retrieval,
  * Keywords can be the base of 

## Projects 

### Cultural Heritage

To be done

### General

To be done

## Bibliography 

### Cultural Heritage

#### 2021

  * Milani, Federico, and Piero Fraternali, ‘A Dataset and a Convolutional Model for Iconography Classification in Paintings’, J. Comput. Cult. Herit., 14.4 (2021), p. 46:1-46:18, doi:10.1145/3458885

### General
