# 1. Foreground/Background Seperation

## Problem 

### Problem Statement

"Separate the foreground cultural heritage object from the background it is photographed against"

### Background

A common need in many different areas is to be able to distinguish in a photography the foreground from the background. In sport it might be to identify the ball, in medicine to identify ..., and in cultural heritage it is quite simple
to be able to seperate the artefact in the professionally photographed image from the backdrop. 

One use for this is to then be able to examine ...

The entirely manual process equivalent would be drawing around the cultural heritage as closely as possible with a * and cropping, then removing any extraneous background pixels by hand as much as can be 

## Related Problems

  * ?-object-recognition
  * 3-image-caption
  * 4-image-description
  * 5-image-

There are some differences though (for example, 

### Enables

  * Object colour based search - removing the background stops this colour being picked up, enabling only the colours of the pixels in the cultural heritage object to be indexed, enabling a "browse by cultural heritage object colour" functionality (
  * Background colour based search - obviously the opposite is also true, for anyone wanting to examine the popularity/changes over time in the background colour choice of museum object photography, by ignoring the cultural heritage object the pixels in the background itself could be indexed.

## Solutions 

### Sample Implementation

A worked example for applying foreground/background segementation to a cultural heritage object image - {doc}`./1/implementations/sample/1-fg-bg-seperation.ipynb`

### Leading Implementations

This is a personal intepretation of results.

| Date | Name | Model/Architecture | Training Dataset | Test Dataset | Origin | Strengths/Weakness | Notes |

### Implementation Tracking 

### Test Datasets

Please note this is a very small set of test image which might not be a fair test for any particular model. We would
welcome anyone else contributing results from any other different datasets if they indicate any particular strengths/weakness
in a model/architecture/training data that is not clear in the current implementation reviews (for cultural heritage in particular).

| Date | Name | Description | Size | Origin | Link |
| Aug 2024 | V&A Dogs 2024 | Image of dogs in various artworks (painting, sculpture, illustration) | 12 | V&A | |

## Variations 

### Major Variations

  * 1M1 - Foreground/Background Seperation in a gallery (or otherwise outside of studio photography)
    
### Minor Variations

None at present

## Narrower Variations

None at present

## Use Cases

## Complex Challenges

Particular artworks that would be very hard challenges for this problem. Objects with gaps/holes in particular are awkward.

  * 
    
## Projects (Cultural Heritage)

## Active

## 2024

### 2014

  * Cooper Hewitt Colour Search

## Bibliography (Cultural Heritage)

### 2024


## Bibliography (General)

## Relevant Datasets

MSCoCo

## Relevant Models

## 
